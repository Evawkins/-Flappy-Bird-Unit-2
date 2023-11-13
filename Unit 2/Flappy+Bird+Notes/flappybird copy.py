# Importing Pygame and Initialization
import pygame
pygame.init()

# Creating a Game Window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Eva\'s Game')

# Function to draw a dark purple triangle
def draw_triangle(x, y):
    pygame.draw.polygon(screen, (128, 0, 128), [(x, y), (x + 25, y + 50), (x - 25, y + 50)])

# Function to draw bullets
def draw_bullets(bullets):
    for bullet in bullets:
        pygame.draw.rect(screen, (0, 0, 255), bullet)

# Initial position of the triangle
triangle_x = 150
triangle_y = 150

# List to store bullets
bullets = []

# A Simple Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((178, 217, 255))  # Fill the screen with white color

    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 50, 50))  # Draw a red rectangle

    draw_triangle(triangle_x, triangle_y)  # Draw a dark purple triangle at the current position

    draw_bullets(bullets)  # Draw bullets

    pygame.display.flip()  # Update the display

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        triangle_x -= 5
    if keys[pygame.K_RIGHT]:
        triangle_x += 5
    if keys[pygame.K_UP]:
        triangle_y -= 5
    if keys[pygame.K_DOWN]:
        triangle_y += 5
    if keys[pygame.K_SPACE]:
        # Shoot a bullet when spacebar is pressed
        bullet = pygame.Rect(triangle_x - 5, triangle_y - 10, 10, 10)
        bullets.append(bullet)

    # Update bullet positions
    for bullet in bullets:
        bullet.y -= 10

    # Remove bullets that go off-screen
    bullets = [bullet for bullet in bullets if bullet.y > 0]

    pygame.time.delay(30)

pygame.quit()
