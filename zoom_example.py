import pygame

def zoom(surface, zoom_factor, center):
    """
    Zooms in or out of a Pygame surface around a specified center point.
    
    Args:
        surface (pygame.Surface): Surface to zoom.
        zoom_factor (float): Zoom factor. Values greater than 1 zoom in, values less than 1 zoom out.
        center (tuple): Coordinates (x, y) of the center point for zooming.
        
    Returns:
        pygame.Surface: Zoomed surface.
    """
    width, height = surface.get_size()
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)
    scaled_surface = pygame.transform.scale(surface, (new_width, new_height))
    
    dx = (new_width - width) // 2
    dy = (new_height - height) // 2
    rect = scaled_surface.get_rect(center=(center[0] + dx, center[1] + dy))
    
    return scaled_surface, rect

# Example usage:
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load an example image
image = pygame.image.load("example_image.jpg")
image_rect = image.get_rect(center=screen.get_rect().center)

# Initial zoom factor and center
zoom_factor = 1.0
zoom_center = screen.get_rect().center

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                zoom_factor *= 1.1  # Zoom in
            elif event.key == pygame.K_o:
                zoom_factor /= 1.1  # Zoom out
    
    # Clear screen
    screen.fill((255, 255, 255))
    
    # Zoom the image
    zoomed_image, zoomed_rect = zoom(image, zoom_factor, zoom_center)
    
    # Draw the zoomed image
    screen.blit(zoomed_image, zoomed_rect)
    
    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
