# currently working on scrolling


import pygame
import os



date_last_updated="14/01/2024"

print (f"""
       game created by Sam Bruce
       
       last updated {date_last_updated}
       """)




# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 400
screen_pos_y=160
screen_pos_x=200
screen_right_max=160
screen_left_max=0
screen_down_max=200
screen_up_max=0
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My Game")

# Set global variables
pan_speed = 15
default_delay=100 #milliseconds



# Load and set the background image
image_path = os.path.join("images", "backgrounds", "oxygen_not_included.jpg")
background_image = pygame.image.load(image_path)
background_rect = background_image.get_rect()
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Update game state

    # Render graphics
    background_rect = (-screen_pos_x,-screen_pos_y)
    window.blit(background_image, background_rect)
    # Draw game objects and UI elements here


    # Check if the mouse is at the left edge of the screen
    if pygame.mouse.get_pos()[0] <= 0:
        # Pan left
        # Update your game logic here to move the game elements to the left
        screen_pos_x=max(screen_pos_x-pan_speed,screen_left_max)
        pygame.time.delay(default_delay)
        print(f"screen_pos_x == {screen_pos_x}")
    if pygame.mouse.get_pos()[0] >= window_width-1:
        # Pan right
        screen_pos_x=min(screen_pos_x+pan_speed,screen_right_max)
        pygame.time.delay(default_delay)
        print(f"screen_pos_x == {screen_pos_x}")
        # Update your game logic here to move the game elements to the right
    if pygame.mouse.get_pos()[1] >= window_height-1:
        # Pan down
        screen_pos_y=min(screen_pos_y+pan_speed,screen_down_max)
        pygame.time.delay(default_delay)
        print(f"screen_pos_y == {screen_pos_y}")
        # Update your game logic here to move the game elements down
    if pygame.mouse.get_pos()[1] <= 0:
        # Pan up
        screen_pos_y=max(screen_pos_y-pan_speed,screen_up_max)
        pygame.time.delay(default_delay)
        print(f"screen_pos_y == {screen_pos_y}")
        # Update your game logic here to move the game elements up
    # Draw game objects and UI elements here

    pygame.display.flip()  # Update the display

# Quit the game
pygame.quit()