import pygame
import os
import time
import sys

# Initialize pygame
pygame.init()

# Set the display
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
TEXT_SURFACE_WIDTH, TEXT_SURFACE_HEIGHT = int(SCREEN_WIDTH * 0.8), int(SCREEN_HEIGHT * 0.6)
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zomboid: Rosewood Rising")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "spiffo.png")))

# Sets the game font (?)
font = pygame.font.SysFont("Times New Roman", 20, bold=False)

# Set the frames per second
FPS = 60

# DEFINE COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)

# Function to display text with animation


def draw_window(text_surface, text_surface_x, text_surface_y):
    WIN.fill((BLACK))
    WIN.blit(text_surface, (text_surface_x, text_surface_y))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    # Creates a surface to draw text on
    text_surface = pygame.Surface((TEXT_SURFACE_WIDTH, TEXT_SURFACE_HEIGHT))
    # Calculate position to center text surface
    text_surface_x = (SCREEN_WIDTH - TEXT_SURFACE_WIDTH) // 2
    text_surface_y = (SCREEN_HEIGHT - TEXT_SURFACE_HEIGHT) // 2


    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        
        printcool("Zomboid: Rosewood Rising", text_surface)
        draw_window(text_surface, text_surface_x, text_surface_y)

    
    pygame.quit()

if __name__ == "__main__":
    main()