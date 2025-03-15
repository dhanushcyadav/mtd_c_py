import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1200, 800  # Width and height of the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Drawing Line at Column 1000')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fill the background with white
screen.fill(WHITE)

# Draw a vertical line at column 1000
line_x = 1000  # X-coordinate for the vertical line
pygame.draw.line(screen, BLACK, (line_x, 0), (line_x, height), 1)

# Update the display
pygame.display.flip()

# Wait for a quit event
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
