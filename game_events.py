import pygame
import game_window

def handle_button_press_release(gamewindow):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamewindow.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamewindow.running = False
                elif event.key == pygame.K_F10:
                    gamewindow.fullscreen = not gamewindow.fullscreen
                elif event.key == pygame.K_LEFT:
                    gamewindow.pan_direction[0] = -1
                elif event.key == pygame.K_RIGHT:
                    gamewindow.pan_direction[0] = 1
                elif event.key == pygame.K_UP:
                    gamewindow.pan_direction[1] = -1
                elif event.key == pygame.K_DOWN:
                    gamewindow.pan_direction[1] = 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    gamewindow.zoomout()
                elif event.button == 5:  # Scroll down
                    gamewindow.zoomin()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    gamewindow.pan_direction[0] = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    gamewindow.pan_direction[1] = 0
def handle_panning(game_window):
    if game_window.pan_direction[0]==-1:
        game_window.pan_left()
    elif game_window.pan_direction[0]==1:
        game_window.pan_right()
    elif game_window.pan_direction[1]==-1:
        game_window.pan_up()
    elif game_window.pan_direction[1]==1:
        game_window.pan_down()

    # Check if the mouse is at the left edge of the screen
    if pygame.mouse.get_pos()[0] <= 0:
        # Pan left
        game_window.pan_left()
    if pygame.mouse.get_pos()[0] >= game_window.window_width-1: #->
        # Pan right
        game_window.pan_right()
    if pygame.mouse.get_pos()[1] >= game_window.window_height-1:
        # Pan down
        game_window.pan_down()
    if pygame.mouse.get_pos()[1] <= 0:
        # Pan up
        game_window.pan_up()
