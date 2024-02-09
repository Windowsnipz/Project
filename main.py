import pygame
import os
import time
import sys

# Initialize pygame
pygame.init()

# Set the display
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zomboid: Rosewood Rising")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "spiffo.png")))

# Sets the game font (?)
font = pygame.font.SysFont("Calibri", 20, bold=True)

# Set the frames per second
FPS = 60

# DEFINE COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Draw the text on the window
def printcool(text, delay=0.05):
    for i, char in enumerate(text):
        text_surface = font.render(char, True, WHITE)
        WIN.blit(text_surface, (50 + i * 10, 50))
        pygame.display.flip()
        time.sleep(delay)

def title_screen():
    WIN.fill(BLACK)
    title_text = font.render("Zomboid: Rosewood Rising", True, WHITE)
    WIN.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    start_text = font.render("Press any key to start", True, WHITE)
    WIN.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def draw_window():
    WIN.fill((0, 0, 0))


def main():
    clock = pygame.time.Clock()

    run = True
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()
        pygame.display.update()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()