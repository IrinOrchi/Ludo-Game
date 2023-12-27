import pygame
import random

# Initialize Pygame
pygame.init()

# Define the screen size and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the positions of the 4 houses and the start position
HOUSE_POSITIONS = [(300, 300), (460, 300), (300, 460), (460, 460)]
START_POSITION = (350, 350)

# Define the positions of the squares
SQUARE_POSITIONS = [
    [(x, y) for x in range(20, 580, 40)] for y in range(20, 580, 40)
]

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define the Ludo board and dice classes
class Board:
    def __init__(self):
        self.squares = [None for _ in range(40)]
        self.houses = [0 for _ in range(4)]

    def draw(self, screen):
        # Draw the squares
        for i, square in enumerate(self.squares):
            pygame.draw.rect(
                screen,
                RED if square == 1 else (YELLOW if square == 2 else GREEN if square == 3 else BLUE if square == 4 else WHITE),
                pygame.Rect(20 + i % 10 * 40, 20 + i // 10 * 40, 40, 40),
            )

        # Draw the houses
        for i, house in enumerate(self.houses):
            pygame.draw.rect(
                screen,
                RED if house == 1 else (YELLOW if house == 2 else GREEN if house == 3 else BLUE if house == 4 else WHITE),
                pygame.Rect(HOUSE_POSITIONS[i][0] - 20, HOUSE_POSITIONS[i][1] - 20, 40, 40),
            )

class Dice:
    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self, screen):
        # Draw the dice value
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.value), 1, BLUE)
        screen.blit(text, (10, 10))

# Initialize the board and dice
board = Board()
dice = Dice()

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice.roll()

    # Update the board and dice positions
    dice.draw(screen)
    board.draw(screen)

    # Update the display
    pygame.display.flip()

    # Pause for a bit
    #time.sleep(0.1)

pygame.quit()