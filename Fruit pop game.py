import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Popping Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load fruit images
apple_img = pygame.image.load('apple.png')
apple_img = pygame.transform.scale(apple_img, (50, 50))

# Game variables
fruit_list = []
fruit_speed = 5
score = 0
font = pygame.font.Font(None, 36)

# Fruit class
class Fruit:
    def __init__(self):
        self.image = apple_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = 0

    def update(self):
        self.rect.y += fruit_speed
        if self.rect.y > HEIGHT:
            fruit_list.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for fruit in fruit_list:
                if fruit.rect.collidepoint(event.pos):
                    fruit_list.remove(fruit)
                    score += 1

    # Add new fruit
    if random.randint(1, 100) > 98:
        fruit_list.append(Fruit())

    # Update and draw fruits
    for fruit in fruit_list:
        fruit.update()
        fruit.draw(screen)

    # Draw score
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()