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
font = pygame.font.SysFont("Times New Roman", 20, bold=True)

# Set the frames per second
FPS = 60

# DEFINE COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)

# Draw the text on the text_surface
def printcool(text, text_surface, delay=0.05):
    text_surface.fill(RED)  # Clear the text surface
    x, y = 0, 0  # Initialize blitting position
    next_char_time = pygame.time.get_ticks() + delay * 1000  # Calculate time for the next character
    for char in text:
        if pygame.time.get_ticks() >= next_char_time:
            text_render = font.render(char, True, WHITE)
            text_surface.blit(text_render, (x, y))  # Blit at the current position
            x += text_render.get_width() + 1  # Increment x position
            next_char_time = pygame.time.get_ticks() + delay * 1000  # Update time for the next character
            pygame.display.update()  # Update the display after rendering each character

    

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

def draw_window(text_surface, text_surface_x, text_surface_y):
    WIN.fill((BLACK))
    WIN.blit(text_surface, (text_surface_x, text_surface_y))
    text_surface.fill(RED)
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