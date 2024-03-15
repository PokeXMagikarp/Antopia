# currently working on scrolling


import pygame
import os
import game_window
import game_events


date_last_updated="21/01/2024"

print (f"""
       game created by Sam Bruce
       
       last updated {date_last_updated}
       """)


def main():
    # Initialize pygame
    pygame.init()
    # initialise the game window
    w1=game_window.gamewindow()
    pygame.display.set_caption("My Game")
    # Create a clock object
    clock = pygame.time.Clock()
    # # Load and set the background image
    w1.screen_load_background("oxygen_not_included.jpg")
    # Game loop
    while w1.running:
        # set clock tick
        clock.tick(60)
        # Handle events
        game_events.handle_button_press_release(w1)
        game_events.handle_panning(w1)
        # Update game state
        w1.update_game_window()
        # Draw game objects and UI elements here
        # pygame.display.flip()  # Update the display
    # Quit the game
    pygame.quit()

main()