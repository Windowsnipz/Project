import pygame
import os
import time
import sys

# Initialize pygame
pygame.init()

# Set the display
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
TEXT_SURFACE_WIDTH, TEXT_SURFACE_HEIGHT = int(SCREEN_WIDTH * 0.8), int(SCREEN_HEIGHT * 0.6)
text_surface = pygame.Surface((TEXT_SURFACE_WIDTH, TEXT_SURFACE_HEIGHT))
TEXT_SURFACE_X = (SCREEN_WIDTH - TEXT_SURFACE_WIDTH) // 2
TEXT_SURFACE_Y = ((SCREEN_HEIGHT - TEXT_SURFACE_HEIGHT) // 2) - 50
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zomboid: Rosewood Rising")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "spiffo.png")))

# Sets the game font (?)
font = pygame.font.SysFont("mspgothic", 20)

# Set the clock and frames per second
clock = pygame.time.Clock()
FPS = 60

# DEFINE COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def print_text(text, color=WHITE):
    x, y = 50, 50
    img = font.render(text, True, color) #Text images
    text_surface.blit(img, (x, y))
    WIN.blit(text_surface, (TEXT_SURFACE_X, TEXT_SURFACE_Y))

def title_screen():
    WIN.fill(BLACK)
    print_text("Press any key to start", color=WHITE)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def main():

    run = True
    while run:
        clock.tick(FPS)

        print_text("Hello, World!")

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ...
                    # TODO: Add a pause menu
                elif event.key == pygame.K_RETURN:
                    ...

        
        pygame.display.update()

    
    pygame.quit()

if __name__ == "__main__":
    main()