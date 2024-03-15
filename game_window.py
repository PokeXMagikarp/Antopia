import pygame
import os

class background:
    def __init__(self,width = 800,height = 400):
        self.width=width
        self.height=height
        self.image_path=""
        self.background_image=""
        self.background_rect=(1,1)


    def load_background(self,image):
        # Load and set the background image
        # this function will take a .jpg file and load it. make sure that the file is located in the backgrounds folder in game files.
        print("loading background...")
        self.image_path = os.path.join("images", "backgrounds", image)
        self.background_image = pygame.image.load(self.image_path)
        

class gamewindow:
    def __init__(self,window_width = 800,window_height = 400,fullscreen=False):
        self.zoom_factor=1
        self.running=True
        self.pan_direction=[0,0]
        self.window_width = int(window_width*self.zoom_factor)
        self.window_height = int(window_height*self.zoom_factor)
        self.screen_pos_y=160
        self.screen_pos_x=200
        self.screen_right_max=160
        self.screen_left_max=0
        self.screen_down_max=200
        self.screen_up_max=0
        self.fullscreen=fullscreen
        self.window = pygame.display.set_mode((window_width, window_height))
        self.window_rect=self.window.get_rect()
        self.pan_speed = 15
        self.default_delay=100 #milliseconds
        self.background=background
        self.zoom_center=self.window.get_rect().center

    def update_background_size(self,width,height):
        self.background.width=width
        self.background.height=height
    def screen_load_background(self,image):
        # Load and set the background image
        # this function will take a .jpg file and load it. make sure that the file is located in the backgrounds folder in game files.
        print("loading background...")
        print(image)
        self.background.load_background(self.background,image)
        self.update_background_size(self.screen_pos_x,self.screen_pos_y)
    def pan_left(self):
        # Pan left
        self.screen_pos_x=max(self.screen_pos_x-self.pan_speed,self.screen_left_max)
        pygame.time.delay(self.default_delay)
        print(f"screen_pos_x == {self.screen_pos_x}")
    def pan_right(self):
        # Pan right
        self.screen_pos_x=min(self.screen_pos_x+self.pan_speed,self.screen_right_max)
        pygame.time.delay(self.default_delay)
        print(f"screen_pos_x == {self.screen_pos_x}")
    def pan_up(self):
        #pan up
        self.screen_pos_y=max(self.screen_pos_y-self.pan_speed,self.screen_up_max)
        pygame.time.delay(self.default_delay)
        print(f"screen_pos_y == {self.screen_pos_y}")
    def pan_down(self):
        # Pan down
        self.screen_pos_y=min(self.screen_pos_y+self.pan_speed,self.screen_down_max)
        pygame.time.delay(self.default_delay)
        print(f"screen_pos_y == {self.screen_pos_y}")
    
    
    def zoom(self):
        """
        Zooms in or out of a Pygame surface around a specified center point.
        
        Args:
            surface (pygame.Surface): Surface to zoom.
            zoom_factor (float): Zoom factor. Values greater than 1 zoom in, values less than 1 zoom out.
            center (tuple): Coordinates (x, y) of the center point for zooming.
            
        Returns:
            pygame.Surface: Zoomed surface.
        """
        self.zoom_center=(pygame.mouse.get_pos())
        width, height = self.background.background_image.get_size()
        new_width = int(width * self.zoom_factor)
        new_height = int(height * self.zoom_factor)
        scaled_surface = pygame.transform.scale(self.background.background_image, (new_width, new_height))
        
        dx = (new_width - width) // 2
        dy = (new_height - height) // 2
        rect = scaled_surface.get_rect(center=(self.zoom_center[0], self.zoom_center[1]))
        
        return scaled_surface, rect
    
    
    
    def zoomin(self):
        #zoom window in
        print("zoomin")
        self.zoom_factor /= 1.1  # Zoom in
        self.window.fill((255, 255, 255))
        # zoomed_image, zoomed_rect = self.zoom()
        # self.window.blit(zoomed_image, zoomed_rect)
        # pygame.display.flip()
    def zoomout(self):
        #zoom window out
        print("zoomout")
        self.zoom_factor *= 1.1  # Zoom out
        self.window.fill((255, 255, 255))
        # zoomed_image, zoomed_rect = self.zoom()
        # self.window.blit(zoomed_image, zoomed_rect)
        # pygame.display.flip()
    def update_game_window(self):
        if self.fullscreen:
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        elif not self.fullscreen:
            self.window = pygame.display.set_mode((self.window_width, self.window_height))
        # Render graphics
        self.background.background_rect = (-self.screen_pos_x,-self.screen_pos_y)
        zoomed_image, zoomed_rect = self.zoom()
        self.window.blit(zoomed_image, zoomed_rect)
        self.window.blit(self.background.background_image, self.background.background_rect)
        # Update the display
        pygame.display.flip()
    def update_zoom_and_positioning(self):
        center=[1,1]
        self.background.image_rect = self.background.get_rect(center=self.window.get_rect().center)
        self.center=center