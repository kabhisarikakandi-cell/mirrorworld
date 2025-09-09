import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mirror World in Pygame")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player settings
player_size = 40
player_speed = 5
player = pygame.Rect(200, 300, player_size, player_size)

# Mirror player (opposite side of screen)
mirror = pygame.Rect(WIDTH - 200 - player_size, 300, player_size, player_size)

# Game loop
while True:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= player_speed
        mirror.y += player_speed  # opposite movement
    if keys[pygame.K_DOWN]:
        player.y += player_speed
        mirror.y -= player_speed
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
        mirror.x += player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
        mirror.x -= player_speed

    # Draw dividing line (mirror boundary)
    pygame.draw.line(screen, (0, 0, 0), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 3)

    # Draw players
    pygame.draw.rect(screen, BLUE, player)   # Normal player
    pygame.draw.rect(screen, RED, mirror)    # Mirror player

    # Update screen
    pygame.display.flip()
    clock.tick(60)