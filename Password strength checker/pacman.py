import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Pac-Man Game")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Pac-Man settings
pacman_radius = 15
pacman_x = screen_width // 2
pacman_y = screen_height // 2
pacman_speed = 5

# Create a clock object
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)

    # Refresh the screen
    pygame.display.update()

    # Limit the frame rate
    clock.tick(30)

# Quit the game
pygame.quit()
