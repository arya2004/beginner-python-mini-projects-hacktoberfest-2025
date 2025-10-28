import pygame as pg
from sys import exit
import random
pg.init()

screen = pg.display.set_mode((1000,600))
pg.display.set_caption('Combat Sequence')

class Character:
    def __init__(self, name, health, max_health, attack_power, defense):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.defense = defense

    def has_not_been_defeated(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def attack(self, other, dice_number):
        if dice_number is not None:
            damage = (self.attack_power * (dice_number+1)) - other.defense
            if damage < 0: damage = 0
            other.take_damage(damage)

class Player(Character):
    def choose_attack(self):
        return "basic_attack"
    
class Bot(Character):
    def choose_attack(self):
        return "basic_attack"
    

player_char = Player("Knight", health=450, max_health=450, attack_power=30, defense=3)
bot_char = Bot("Ninja", health=450, max_health=450, attack_power=24, defense=3)

damage_texts = []
player_img = pg.image.load('./Images/knight.png')
player_img = pg.transform.scale(player_img, (150, 150))
player_rect = player_img.get_rect(topleft=(200, 250))

bot_img = pg.image.load('./Images/Ninja.png')  
bot_img = pg.transform.scale(bot_img, (150, 150))
bot_rect = bot_img.get_rect(topleft=(600, 250))

player_attack_img = pg.image.load('./Images/knight.png')
player_attack_img = pg.transform.scale(player_attack_img, (150, 150))

bot_attack_img = pg.image.load('./Images/Ninja.png')
bot_attack_img = pg.transform.scale(bot_attack_img, (150, 150))

attack_anim = None

dice_images = []
for i in range(1, 7):
    img = pg.image.load(f'./Images/Dice/DICE_{i}.png')
    img = pg.transform.scale(img, (50, 50))
    dice_images.append(img)

font = pg.font.SysFont('timesnewroman', 30)
health_font = pg.font.SysFont('timesnewroman', 20)
turn = 0
clock = pg.time.Clock()
def show_damage(amount, pos):
    text_surface = font.render(f"-{amount}", True, (255, 255, 0)) 
    damage_texts.append([text_surface, pos, pg.time.get_ticks()])

def draw_health(character, pos, size=(150, 20), is_player = True):
    border_rect = pg.Rect(pos[0]-2, pos[1]-2, size[0]+4, size[1]+4)
    pg.draw.rect(screen, (0, 0, 0), border_rect)

    bg_rect = pg.Rect(pos[0]+2, pos[1]+2, size[0]-4, size[1]-4)
    pg.draw.rect(screen, (100, 100, 100), bg_rect)
    
    health_ratio = character.health / character.max_health

    if is_player:
        fg_rect = pg.Rect(pos[0]+2 + (size[0]-4)*(1 - health_ratio), pos[1]+2, (size[0]-4)*health_ratio, size[1]-4)
    else:
        fg_rect = pg.Rect(pos[0]+2, pos[1]+2, (size[0]-4)*health_ratio, size[1]-4)

    pg.draw.rect(screen, (255, 0, 0), fg_rect)
    
    health_text = health_font.render(f"{character.health}/{character.max_health}", True, (255, 255, 255))
    screen.blit(health_text, (pos[0] + 5, pos[1] +20))
    name_text = font.render(character.name, True, (255, 255, 255))
    screen.blit(name_text, (pos[0], pos[1] - 35))

roll_button = pg.Rect(450, 500, 150, 50)  
button_color = (200, 255, 200) 
hover_color = (150, 220, 150)
button_text = font.render("Roll Dice?", True, (0,0,0))

dice_number = None  
rolling = False     
roll_start_time = 0

bot_dice_number = None
bot_roll_start_time = 0

phase = "player_wait"
#MAIN LOOP
while True:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            pg.quit()
            exit()
        if events.type == pg.MOUSEBUTTONDOWN:
            if phase == "player_wait":
                phase = "player_roll"
                roll_start_time = pg.time.get_ticks()
    
    mouse_pos = pg.mouse.get_pos()
    if roll_button.collidepoint(mouse_pos):
        current_color = hover_color
    else:
        current_color = button_color

    if phase == "player_wait":
        pass  

    elif phase == "player_roll":
        elapsed = pg.time.get_ticks() - roll_start_time
        if elapsed >= 1500:
            dice_number = random.randint(0, 5)  
            phase = "player_attack"
        else:
            dice_number = random.randint(0, 5)  

    elif phase == "player_attack":
        start_pos = player_rect.topleft
        end_pos = (bot_rect.x - 50, bot_rect.y)
        attack_anim = ["player", start_pos, end_pos, pg.time.get_ticks(),True]
        phase = "animating_attack"

    elif phase == "bot_wait":
        elapsed = pg.time.get_ticks() - bot_roll_start_time
        if elapsed >= 1500:
            bot_dice_number = random.randint(0, 5)
            phase = "bot_attack"
        else:
            bot_dice_number = random.randint(0, 5)

    elif phase == "bot_attack":
        start_pos = bot_rect.topleft
        end_pos = (player_rect.x + 50, player_rect.y)
        attack_anim = ["bot", start_pos, end_pos, pg.time.get_ticks(),False]
        phase = "animating_attack"
        
    elif phase == "game_over":
        if player_char.has_not_been_defeated():
            result_text = font.render("Player Wins!", True, (0, 255, 0))
        else:
            result_text = font.render("Enemy Wins!", True, (255, 0, 0))
        screen.blit(result_text, (400, 300))
        pg.display.update()
        pg.time.delay(3000)
        pg.quit()
        exit()
        

    screen.fill((45, 54, 176)) 

    draw_health(player_char, (50, 50), is_player=True)
    draw_health(bot_char, (800, 50), is_player=False)

    pg.draw.rect(screen, current_color, roll_button)
    screen.blit(button_text, (roll_button.x+5, roll_button.y+10))
    
    if dice_number is not None:
        screen.blit(dice_images[dice_number], (120, 400))
    if bot_dice_number is not None:
        screen.blit(dice_images[bot_dice_number], (820, 400))
    current_time = pg.time.get_ticks()

    for dt in damage_texts[:]:  
        screen.blit(dt[0], dt[1])
        if current_time - dt[2] > 1500:  
            damage_texts.remove(dt)
            
    if attack_anim is not None:
        current_time = pg.time.get_ticks()
        elapsed = current_time - attack_anim[3]
        t = min(elapsed / 500, 1)

        x = attack_anim[1][0] + (attack_anim[2][0] - attack_anim[1][0])*t
        y = attack_anim[1][1] + (attack_anim[2][1] - attack_anim[1][1])*t

        if attack_anim[0] == "player":
            screen.blit(player_attack_img, (x, y))
            screen.blit(bot_img, bot_rect)
        else:
            screen.blit(bot_attack_img, (x, y))
            screen.blit(player_img, player_rect)

        if t >= 1:
            if attack_anim[0] == "player":
                damage_done = (player_char.attack_power * (dice_number+1)) - bot_char.defense
                bot_char.take_damage(damage_done)
                show_damage(damage_done, (bot_rect.x + 50, bot_rect.y - 20))
                phase = "bot_wait" if bot_char.has_not_been_defeated() else "game_over"
                bot_roll_start_time = pg.time.get_ticks()
            else:
                damage_done = (bot_char.attack_power * (bot_dice_number+1)) - player_char.defense
                player_char.take_damage(damage_done)
                show_damage(damage_done, (player_rect.x + 50, player_rect.y - 20))
                phase = "player_wait" if player_char.has_not_been_defeated() else "game_over"
            attack_anim = None
    else:
        screen.blit(player_img, player_rect)
        screen.blit(bot_img, bot_rect)
    pg.display.update()
    clock.tick(60)