import pygame
import random
import sys

pygame.init()

#  game window
screen_width = 800
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fruit Catcher Game")

# given colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (150, 75, 0)
RED = (255, 80, 80)
YELLOW = (255, 220, 80)
GREEN = (80, 255, 100)
ORANGE = (255, 165, 0)
PURPLE = (180, 100, 255)

# list of fruit colors
fruit_colors = [RED, YELLOW, GREEN, ORANGE, PURPLE]

#  the game clock
clock = pygame.time.Clock()

# Set up fonts
font = pygame.font.Font(None, 40)
big_font = pygame.font.Font(None, 72)

# Basket 
basket_width = 100
basket_height = 20
basket_x = screen_width // 2 - basket_width // 2
basket_y = screen_height - 60
basket_speed = 10

# Fruit settings
fruit_radius = 20
fruits_list = []  # This will store all the falling fruits
last_fruit_time = pygame.time.get_ticks()
time_between_fruits = 1500  # Time in milliseconds
fruit_fall_speed = 3

# Games variables
score = 0
lives = 3
high_score = 0
game_over = False

# to draw text on the screen
def draw_text(text, font_size, color, x, y, centered=True):
    font_obj = pygame.font.Font(None, font_size)
    text_surface = font_obj.render(text, True, color)
    text_rect = text_surface.get_rect()
    
    if centered:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
        
    screen.blit(text_surface, text_rect)

# to create a new fruit
def create_fruit():
    new_fruit = {
        "x": random.randint(fruit_radius, screen_width - fruit_radius),
        "y": -fruit_radius,
        "color": random.choice(fruit_colors),
        "speed": fruit_fall_speed + random.random() * 2
    }
    return new_fruit

#  to move a fruit down the screen
def move_fruit(fruit):
    fruit["y"] += fruit["speed"]

# and to draw a fruit on the screen
def draw_fruit(fruit):
    pygame.draw.circle(screen, fruit["color"], (int(fruit["x"]), int(fruit["y"])), fruit_radius)

# to reset the game
def reset_game():
    global score, lives, fruits_list, fruit_fall_speed, time_between_fruits, game_over
    score = 0
    lives = 3
    fruits_list = []
    fruit_fall_speed = 3
    time_between_fruits = 1500
    game_over = False

# game loop
running = True

while running:
    # Fill the screen with a dark blue color
    screen.fill((BLACK))
    
    # Check for events
    for event in pygame.event.get():
        # the user clicks  X button - quit the game
        if event.type == pygame.QUIT:
            running = False
            
        # If the game is over and then user presses R - restart the game
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:  
                reset_game()
    
    # Get which keys are currently pressed
    keys = pygame.key.get_pressed()
    
    # Move the basket in game 
    if not game_over:
        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket_x += basket_speed
    
    # Make sure the basket doesn't go off the screen
    if basket_x < 0:
        basket_x = 0
    if basket_x > screen_width - basket_width:
        basket_x = screen_width - basket_width
    
    # Create a new fruit if enough time has passed
    current_time = pygame.time.get_ticks()
    if not game_over and current_time - last_fruit_time > time_between_fruits:
        fruits_list.append(create_fruit())
        last_fruit_time = current_time
    
    # Update and draw all fruits
    i = 0
    while i < len(fruits_list):
        fruit = fruits_list[i]
        move_fruit(fruit)
        draw_fruit(fruit)
        
        # Check if the fruit was caught by the basket
        fruit_caught = False
        fruit_missed = False
        
        # Check if the fruit is at the same height as the basket
        if basket_y < fruit["y"] + fruit_radius < basket_y + basket_height:
            # Check if the fruit is above the basket horizontally
            if basket_x < fruit["x"] < basket_x + basket_width:
                # The fruit was caught!
                fruits_list.pop(i)
                score += 1
                fruit_caught = True
                
                # Make the game harder every 5 points
                if score % 5 == 0:
                    fruit_fall_speed += 0.5
                    time_between_fruits = max(400, time_between_fruits - 50)
        
        # Check if the fruit fell off the screen
        elif fruit["y"] > screen_height + fruit_radius:
            fruits_list.pop(i)
            lives -= 1
            fruit_missed = True
            
            # Check if the game is over
            if lives <= 0:
                game_over = True
                # Update high score if needed
                if score > high_score:
                    high_score = score
        
        # Only move to the next fruit if we didn't remove this one
        if not fruit_caught and not fruit_missed:
            i += 1
    
    # Draw the basket
    pygame.draw.rect(screen, BROWN, (basket_x, basket_y, basket_width, basket_height))
    pygame.draw.rect(screen, WHITE, (basket_x, basket_y, basket_width, basket_height), 2)
    
    # Draw the score and lives
    draw_text(f"Score: {score}", 36, WHITE, 20, 20, False)
    draw_text(f"Lives: {lives}", 36, WHITE, screen_width - 150, 20, False)
    draw_text(f"High Score: {high_score}", 36, YELLOW, screen_width // 2, 20)
    
    # If the game is over, show the game over screen
    if game_over:
        draw_text("GAME OVER", 72, RED, screen_width // 2, screen_height // 2 - 40)
        draw_text(f"Score: {score}", 48, WHITE, screen_width // 2, screen_height // 2 + 20)
        draw_text(" R to restart", 36, YELLOW, screen_width // 2, screen_height // 2 + 80)  # <-- updated text
    
    # Update the display
    pygame.display.flip()
    
    #  game speed
    clock.tick(60)

# for Quiting the game
pygame.quit()
sys.exit()
