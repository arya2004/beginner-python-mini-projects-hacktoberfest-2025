import pygame
import random
import sys
import math
from typing import List, Tuple, Optional
from enum import Enum

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 25

GRID_X = 50
GRID_Y = 50

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (192, 192, 192)

RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 50)
CYAN = (50, 255, 255)
MAGENTA = (255, 50, 255)
ORANGE = (255, 165, 50)

BLOCK_COLORS = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE]

FPS = 60
INITIAL_FALL_SPEED = 800
FAST_FALL_SPEED = 50
MIN_MATCH = 4
LOCK_DELAY = 300
CLEAR_ANIMATION_DURATION = 400

SCORE_PER_BLOCK = 10
COMBO_MULTIPLIER = 1.5

def create_sound_effect(frequency: int, duration: int) -> pygame.mixer.Sound:
    try:
        sample_rate = 22050
        n_samples = int(duration * sample_rate / 1000)
        
        import numpy as np
        t = np.linspace(0, duration / 1000, n_samples)
        wave = np.sin(2 * np.pi * frequency * t)
        
        fade = np.linspace(1, 0, n_samples)
        wave = wave * fade * 0.3
        
        stereo_wave = np.column_stack((wave, wave))
        stereo_wave = (stereo_wave * 32767).astype(np.int16)
        
        sound = pygame.sndarray.make_sound(stereo_wave)
        return sound
    except:
        return None

CLEAR_SOUND = create_sound_effect(600, 200)
LOCK_SOUND = create_sound_effect(300, 150)
COMBO_SOUND = create_sound_effect(800, 250)

class BlockShape:
    
    SHAPES = {
        'I': [(0, 0), (0, 1), (0, 2), (0, 3)],
        'O': [(0, 0), (0, 1), (1, 0), (1, 1)],
        'T': [(0, 0), (0, 1), (0, 2), (1, 1)],
        'L': [(0, 0), (1, 0), (2, 0), (2, 1)],
        'J': [(0, 1), (1, 1), (2, 1), (2, 0)],
        'S': [(0, 1), (0, 2), (1, 0), (1, 1)],
        'Z': [(0, 0), (0, 1), (1, 1), (1, 2)],
        'DOT': [(0, 0)],
        'LINE': [(0, 0), (0, 1)],
    }
    
    @staticmethod
    def get_random_shape():
        return random.choice(list(BlockShape.SHAPES.keys()))
    
    @staticmethod
    def get_shape_coords(shape_name: str) -> List[Tuple[int, int]]:
        return BlockShape.SHAPES.get(shape_name, [(0, 0)])

class FallingBlock:
    
    def __init__(self, shape_name: str, color: Tuple[int, int, int], start_col: int = 4):
        self.shape_name = shape_name
        self.color = color
        self.row = 0
        self.col = start_col
        self.coords = BlockShape.get_shape_coords(shape_name)
        
    def get_block_positions(self) -> List[Tuple[int, int]]:
        return [(self.row + dr, self.col + dc) for dr, dc in self.coords]
    
    def move(self, dr: int, dc: int):
        self.row += dr
        self.col += dc
    
    def rotate_clockwise(self):
        self.coords = [(dc, -dr) for dr, dc in self.coords]
    
    def rotate_counterclockwise(self):
        self.coords = [(-dc, dr) for dr, dc in self.coords]

class GameBoard:
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        
    def is_valid_position(self, block: FallingBlock) -> bool:
        for row, col in block.get_block_positions():
            if row < 0 or row >= self.height or col < 0 or col >= self.width:
                return False
            if self.grid[row][col] is not None:
                return False
        return True
    
    def lock_block(self, block: FallingBlock):
        for row, col in block.get_block_positions():
            if 0 <= row < self.height and 0 <= col < self.width:
                self.grid[row][col] = block.color
    
    def find_matches(self) -> List[Tuple[int, int]]:
        visited = set()
        matches = []
        
        def flood_fill(row: int, col: int, color: Tuple[int, int, int]) -> List[Tuple[int, int]]:
            if (row, col) in visited:
                return []
            if row < 0 or row >= self.height or col < 0 or col >= self.width:
                return []
            if self.grid[row][col] != color:
                return []
            
            visited.add((row, col))
            connected = [(row, col)]
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                connected.extend(flood_fill(row + dr, col + dc, color))
            
            return connected
        
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] is not None and (row, col) not in visited:
                    color = self.grid[row][col]
                    group = flood_fill(row, col, color)
                    if len(group) >= MIN_MATCH:
                        matches.extend(group)
        
        return matches
    
    def clear_blocks(self, positions: List[Tuple[int, int]]):
        for row, col in positions:
            self.grid[row][col] = None
    
    def apply_gravity(self) -> bool:
        moved = False
        
        for col in range(self.width):
            write_row = self.height - 1
            
            for read_row in range(self.height - 1, -1, -1):
                if self.grid[read_row][col] is not None:
                    if write_row != read_row:
                        self.grid[write_row][col] = self.grid[read_row][col]
                        self.grid[read_row][col] = None
                        moved = True
                    write_row -= 1
        
        return moved
    
    def get_falling_distances(self) -> dict:
        distances = {}
        
        for col in range(self.width):
            empty_count = 0
            for row in range(self.height - 1, -1, -1):
                if self.grid[row][col] is None:
                    empty_count += 1
                elif empty_count > 0:
                    distances[(row, col)] = empty_count
        
        return distances
    
    def is_game_over(self) -> bool:
        return any(self.grid[0][col] is not None for col in range(self.width))
    
    def clear(self):
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]
    
    def setup_initial_blocks(self, num_rows: int = 4):
        for row in range(self.height - num_rows, self.height):
            for col in range(self.width):
                if random.random() < 0.8:
                    self.grid[row][col] = random.choice(BLOCK_COLORS)

class Game:
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Color Block Puzzle")
        self.clock = pygame.time.Clock()
        
        pygame.mixer.init()
        self.sounds = self.load_sounds()
        
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        self.board = GameBoard(GRID_WIDTH, GRID_HEIGHT)
        self.current_block: Optional[FallingBlock] = None
        self.next_block: Optional[FallingBlock] = None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.paused = False
        
        self.fall_timer = 0
        self.fall_speed = INITIAL_FALL_SPEED
        self.fast_falling = False
        self.lock_timer = 0
        self.is_locking = False
        
        self.combo_count = 0
        self.clearing_blocks = []
        self.clear_animation_timer = 0
        self.is_clearing = False
        
        self.board.setup_initial_blocks(num_rows=4)
        
        self.spawn_new_block()
        self.generate_next_block()
    
    def load_sounds(self):
        sounds = {}
        try:
            sounds['clear'] = self.generate_beep(800, 0.1)
            sounds['lock'] = self.generate_beep(400, 0.05)
            sounds['combo'] = self.generate_beep(1000, 0.15)
            sounds['move'] = self.generate_beep(300, 0.02)
        except:
            sounds = {'clear': None, 'lock': None, 'combo': None, 'move': None}
        return sounds
    
    def generate_beep(self, frequency, duration):
        sample_rate = 22050
        n_samples = int(round(duration * sample_rate))
        
        buf = []
        max_sample = 2047
        for s in range(n_samples):
            t = float(s) / sample_rate
            envelope = min(1.0, (n_samples - s) / (n_samples * 0.1))
            value = int(round(max_sample * envelope * math.sin(2 * math.pi * frequency * t)))
            buf.append([value, value])
        
        try:
            import numpy as np
            buf_array = np.array(buf, dtype=np.int16)
            sound = pygame.sndarray.make_sound(buf_array)
            return sound
        except:
            return None
    
    def play_sound(self, sound_name):
        if sound_name in self.sounds and self.sounds[sound_name]:
            try:
                self.sounds[sound_name].play()
            except:
                pass
    
    def generate_next_block(self):
        shape = BlockShape.get_random_shape()
        color = random.choice(BLOCK_COLORS)
        self.next_block = FallingBlock(shape, color)
    
    def spawn_new_block(self):
        if self.next_block:
            self.current_block = self.next_block
            self.current_block.row = 0
            self.current_block.col = GRID_WIDTH // 2 - 1
        else:
            shape = BlockShape.get_random_shape()
            color = random.choice(BLOCK_COLORS)
            self.current_block = FallingBlock(shape, color)
        
        self.generate_next_block()
        
        if not self.board.is_valid_position(self.current_block):
            self.game_over = True
    
    def move_block(self, dr: int, dc: int) -> bool:
        if self.current_block is None:
            return False
        
        self.current_block.move(dr, dc)
        
        if not self.board.is_valid_position(self.current_block):
            self.current_block.move(-dr, -dc)
            return False
        
        return True
    
    def rotate_block(self, clockwise: bool = True):
        if self.current_block is None:
            return
        
        if clockwise:
            self.current_block.rotate_clockwise()
        else:
            self.current_block.rotate_counterclockwise()
        
        if not self.board.is_valid_position(self.current_block):
            if clockwise:
                self.current_block.rotate_counterclockwise()
            else:
                self.current_block.rotate_clockwise()
    
    def lock_and_check(self):
        if self.current_block is None:
            return
        
        self.play_sound('lock')
        
        self.board.lock_block(self.current_block)
        self.current_block = None
        self.is_locking = False
        self.lock_timer = 0
        
        self.apply_all_gravity()
        
        self.check_for_matches()
    
    def apply_all_gravity(self):
        while self.board.apply_gravity():
            pass
    
    def check_for_matches(self):
        matches = self.board.find_matches()
        
        if matches:
            self.clearing_blocks = matches
            self.is_clearing = True
            self.clear_animation_timer = 0
            self.combo_count += 1
        else:
            if self.combo_count > 0:
                self.combo_count = 0
            self.spawn_new_block()
    
    def finish_clearing(self):
        self.play_sound('clear')
        
        self.board.clear_blocks(self.clearing_blocks)
        
        base_score = len(self.clearing_blocks) * SCORE_PER_BLOCK
        combo_bonus = int(base_score * (COMBO_MULTIPLIER ** (self.combo_count - 1)))
        self.score += combo_bonus
        self.lines_cleared += len(self.clearing_blocks)
        
        if self.combo_count > 1:
            self.play_sound('combo')
        
        new_level = self.lines_cleared // 50 + 1
        if new_level > self.level:
            self.level = new_level
            self.fall_speed = max(100, INITIAL_FALL_SPEED - (self.level - 1) * 50)
        
        self.clearing_blocks = []
        self.is_clearing = False
        
        self.apply_all_gravity()
        
        self.check_for_matches()
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    return False
                
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.restart()
                    continue
                
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                
                if self.paused:
                    continue
                
                elif event.key == pygame.K_LEFT:
                    if self.move_block(0, -1):
                        self.play_sound('move')
                elif event.key == pygame.K_RIGHT:
                    if self.move_block(0, 1):
                        self.play_sound('move')
                elif event.key == pygame.K_DOWN:
                    self.fast_falling = True
                
                elif event.key == pygame.K_UP or event.key == pygame.K_z:
                    self.rotate_block(clockwise=True)
                elif event.key == pygame.K_x:
                    self.rotate_block(clockwise=False)
                
                elif event.key == pygame.K_SPACE:
                    while self.move_block(1, 0):
                        pass
                    self.is_locking = False
                    self.lock_and_check()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.fast_falling = False
        
        return True
    
    def update(self, dt: int):
        if self.game_over or self.paused:
            return
        
        if self.is_clearing:
            self.clear_animation_timer += dt
            if self.clear_animation_timer >= CLEAR_ANIMATION_DURATION:
                self.finish_clearing()
            return
        
        if self.is_locking:
            self.lock_timer += dt
            if self.lock_timer >= LOCK_DELAY:
                self.lock_and_check()
            return
        
        current_speed = FAST_FALL_SPEED if self.fast_falling else self.fall_speed
        self.fall_timer += dt
        
        if self.fall_timer >= current_speed:
            self.fall_timer = 0
            
            if not self.move_block(1, 0):
                self.is_locking = True
                self.lock_timer = 0
    
    def draw_block(self, row: int, col: int, color: Tuple[int, int, int], 
                   offset_x: int = 0, offset_y: int = 0, alpha: int = 255):
        x = GRID_X + col * BLOCK_SIZE + offset_x
        y = GRID_Y + row * BLOCK_SIZE + offset_y
        
        block_surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        block_surface.set_alpha(alpha)
        
        pygame.draw.rect(block_surface, color, (0, 0, BLOCK_SIZE, BLOCK_SIZE))
        
        pygame.draw.rect(block_surface, WHITE, (0, 0, BLOCK_SIZE, BLOCK_SIZE), 2)
        pygame.draw.rect(block_surface, DARK_GRAY, (2, 2, BLOCK_SIZE - 4, BLOCK_SIZE - 4), 1)
        
        self.screen.blit(block_surface, (x, y))
    
    def draw_board(self):
        grid_rect = pygame.Rect(GRID_X, GRID_Y, 
                                 GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE)
        pygame.draw.rect(self.screen, DARK_GRAY, grid_rect)
        
        for i in range(GRID_WIDTH + 1):
            x = GRID_X + i * BLOCK_SIZE
            pygame.draw.line(self.screen, GRAY, (x, GRID_Y), 
                             (x, GRID_Y + GRID_HEIGHT * BLOCK_SIZE), 1)
        
        for i in range(GRID_HEIGHT + 1):
            y = GRID_Y + i * BLOCK_SIZE
            pygame.draw.line(self.screen, GRAY, (GRID_X, y), 
                             (GRID_X + GRID_WIDTH * BLOCK_SIZE, y), 1)
        
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if self.board.grid[row][col] is not None:
                    if (row, col) in self.clearing_blocks:
                        progress = self.clear_animation_timer / CLEAR_ANIMATION_DURATION
                        alpha = int(255 * (1 - progress))
                        scale = 1 + 0.5 * math.sin(progress * math.pi)
                        offset = int((BLOCK_SIZE * scale - BLOCK_SIZE) / 2)
                        
                        x = GRID_X + col * BLOCK_SIZE - offset
                        y = GRID_Y + row * BLOCK_SIZE - offset
                        size = int(BLOCK_SIZE * scale)
                        
                        block_surface = pygame.Surface((size, size))
                        block_surface.set_alpha(alpha)
                        color = self.board.grid[row][col]
                        pygame.draw.rect(block_surface, color, (0, 0, size, size))
                        pygame.draw.rect(block_surface, WHITE, (0, 0, size, size), 2)
                        
                        glow_color = tuple(min(255, c + 100) for c in color)
                        pygame.draw.rect(block_surface, glow_color, (2, 2, size - 4, size - 4), 1)
                        
                        self.screen.blit(block_surface, (x, y))
                    else:
                        self.draw_block(row, col, self.board.grid[row][col])
        
        if self.current_block:
            for row, col in self.current_block.get_block_positions():
                if 0 <= row < GRID_HEIGHT:
                    if self.is_locking:
                        progress = self.lock_timer / LOCK_DELAY
                        brightness = 1.0 + 0.5 * math.sin(progress * math.pi * 4)
                        color = tuple(min(255, int(c * brightness)) for c in self.current_block.color)
                        self.draw_block(row, col, color)
                    else:
                        self.draw_block(row, col, self.current_block.color)
    
    def draw_ui(self):
        ui_x = GRID_X + GRID_WIDTH * BLOCK_SIZE + 40
        
        score_text = self.font_medium.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (ui_x, 50))
        
        level_text = self.font_medium.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(level_text, (ui_x, 100))
        
        lines_text = self.font_small.render(f"Cleared: {self.lines_cleared}", True, WHITE)
        self.screen.blit(lines_text, (ui_x, 150))
        
        if self.combo_count > 1:
            combo_text = self.font_medium.render(f"COMBO x{self.combo_count}!", True, YELLOW)
            self.screen.blit(combo_text, (ui_x, 200))
        
        next_text = self.font_small.render("Next:", True, WHITE)
        self.screen.blit(next_text, (ui_x, 280))
        
        if self.next_block:
            preview_y = 310
            for dr, dc in self.next_block.coords:
                self.draw_block(0, 0, self.next_block.color, 
                              ui_x + dc * BLOCK_SIZE, preview_y + dr * BLOCK_SIZE)
        
        controls_y = 420
        controls = [
            "Controls:",
            "← → Move",
            "↓ Soft drop",
            "↑/Z Rotate",
            "Space Hard drop",
            "P Pause",
            "Q Quit"
        ]
        
        for i, text in enumerate(controls):
            control_text = self.font_small.render(text, True, LIGHT_GRAY)
            self.screen.blit(control_text, (ui_x, controls_y + i * 25))
    
    def draw(self):
        self.screen.fill(BLACK)
        
        self.draw_board()
        self.draw_ui()
        
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(200)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            game_over_text = self.font_large.render("GAME OVER", True, RED)
            score_text = self.font_medium.render(f"Final Score: {self.score}", True, WHITE)
            restart_text = self.font_small.render("Press R to Restart or Q to Quit", True, WHITE)
            
            self.screen.blit(game_over_text, 
                             (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 200))
            self.screen.blit(score_text, 
                             (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 280))
            self.screen.blit(restart_text, 
                             (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 340))
        
        if self.paused and not self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            paused_text = self.font_large.render("PAUSED", True, YELLOW)
            self.screen.blit(paused_text, 
                             (SCREEN_WIDTH // 2 - paused_text.get_width() // 2, 250))
        
        pygame.display.flip()
    
    def restart(self):
        self.board.clear()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.paused = False
        self.fall_timer = 0
        self.fall_speed = INITIAL_FALL_SPEED
        self.combo_count = 0
        self.lock_timer = 0
        self.is_locking = False
        self.clearing_blocks = []
        self.clear_animation_timer = 0
        self.is_clearing = False
        
        self.board.setup_initial_blocks(num_rows=4)
        
        self.spawn_new_block()
        self.generate_next_block()
    
    def run(self):
        running = True
        
        while running:
            dt = self.clock.tick(FPS)
            
            running = self.handle_input()
            self.update(dt)
            self.draw()
        
        pygame.quit()
        sys.exit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()