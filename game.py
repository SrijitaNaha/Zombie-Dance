import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
ZOMBIE_SIZE = 200

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the zombie images
zombie_images = [
    pygame.image.load('zombie1.png'),
    pygame.image.load('zombie2.png'),
    pygame.image.load('zombie3.png'),
    pygame.image.load('zombie4.png'),
]
for i in range(len(zombie_images)):
    zombie_images[i] = pygame.transform.scale(zombie_images[i], (ZOMBIE_SIZE, ZOMBIE_SIZE))

# Set up the zombie's starting position and image
zombie_x, zombie_y = WIDTH / 2, HEIGHT / 2
current_zombie_image = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_zombie_image = (current_zombie_image + 1) % len(zombie_images)

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    # Move the zombie based on the keys being pressed
    if keys[pygame.K_UP]:
        zombie_y -= 5
    if keys[pygame.K_DOWN]:
        zombie_y += 5
    if keys[pygame.K_LEFT]:
        zombie_x -= 5
    if keys[pygame.K_RIGHT]:
        zombie_x += 5

    # Fill the screen with black to clear the previous frame
    screen.fill((0, 0, 0))

    # Draw the zombie at its current position
    screen.blit(zombie_images[current_zombie_image], (zombie_x, zombie_y))

    # Flip the display to make the changes visible
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)