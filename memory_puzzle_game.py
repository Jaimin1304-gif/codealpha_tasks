# MEMORY PUZZLE GAME

import asyncio
import platform
import pygame
import random
import time
from pyodide.http import pyfetch
from js import console

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CARD_SIZE = 100
GRID_SIZE = 4  # 4x4 grid (16 cards, 8 pairs)
MARGIN = 10
FPS = 60
TIME_LIMIT = 60  # 60 seconds

# Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Puzzle Game")
font = pygame.font.Font(None, 36)

# Card class
class Card:
    def __init__(self, value, x, y):
        self.value = value
        self.rect = pygame.Rect(x, y, CARD_SIZE, CARD_SIZE)
        self.flipped = False
        self.matched = False

# Create cards
def create_cards():
    values = list(range(8)) * 2  # 8 pairs
    random.shuffle(values)
    cards = []
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x = MARGIN + j * (CARD_SIZE + MARGIN)
            y = MARGIN + i * (CARD_SIZE + MARGIN) + 50  # Offset for timer
            cards.append(Card(values[i * GRID_SIZE + j], x, y))
    return cards

# Game variables
cards = create_cards()
first_card = None
second_card = None
lock_board = False
matches_found = 0
start_time = None
game_over = False
game_won = False

async def main():
    global first_card, second_card, lock_board, matches_found, start_time, game_over, game_won
    clock = pygame.time.Clock()
    start_time = time.time()

    while True:
        if game_over or game_won:
            break

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and not lock_board and not game_over:
                pos = pygame.mouse.get_pos()
                for card in cards:
                    if card.rect.collidepoint(pos) and not card.flipped and not card.matched:
                        card.flipped = True
                        if not first_card:
                            first_card = card
                        elif first_card != card:
                            second_card = card
                            lock_board = True

        # Check for matches
        if first_card and second_card:
            if first_card.value == second_card.value:
                first_card.matched = second_card.matched = True
                matches_found += 1
                first_card = second_card = None
                lock_board = False
                if matches_found == 8:  # All pairs found
                    game_won = True
            else:
                await asyncio.sleep(1)  # Delay to show non-matching cards
                first_card.flipped = second_card.flipped = False
                first_card = second_card = None
                lock_board = False

        # Check time limit
        elapsed_time = time.time() - start_time
        if elapsed_time > TIME_LIMIT:
            game_over = True

        # Draw
        screen.fill(WHITE)
        
        # Draw timer
        time_left = max(0, TIME_LIMIT - elapsed_time)
        timer_text = font.render(f"Time: {int(time_left)}s", True, BLACK)
        screen.blit(timer_text, (10, 10))

        # Draw cards
        for card in cards:
            if card.flipped or card.matched:
                pygame.draw.rect(screen, BLUE, card.rect)
                text = font.render(str(card.value), True, WHITE)
                text_rect = text.get_rect(center=card.rect.center)
                screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, GRAY, card.rect)

        # Draw game over or win message
        if game_over:
            text = font.render("Game Over! Time's up!", True, RED)
            screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        elif game_won:
            text = font.render("You Won! All pairs found!", True, BLUE)
            screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(1.0 / FPS)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())