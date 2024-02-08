import pygame
import os
import time

from helpers import printcool, start_game
from story_paths.story_path1 import path1

# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zomboid: Rosewood Rising")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "spiffo.png")))

text_font = pygame.font.SysFont("Calibri", 20, bold=True)

FPS = 60
HEART_WIDTH, HEART_HEIGHT = 40, 40

HEART = pygame.image.load(os.path.join("Assets", "heart.png"))
HEART_EMPTY = pygame.image.load(os.path.join("Assets", "heart_empty.png"))
HEART_HALF = pygame.image.load(os.path.join("Assets", "heart_half.png"))

hearts = [(HEART, (350, 400)), (HEART, (380, 400)), (HEART, (410, 400)), 
          (HEART, (440, 400)), (HEART, (470, 400))]
health = 10

# Update the hearts based on the health
def get_hearts(health):
    hearts = []
    for i in range(5):
        x = 360 + (30 * i) # x position
        y = 400
        if health > i * 2 + 1:
            hearts.append((HEART, (x, y)))
        elif health > i * 2:
            hearts.append((HEART_HALF, (x, y)))
        else:
            hearts.append((HEART_EMPTY, (x, y)))
    return hearts
    
# Draw the text on the window
def draw_text(text, font, color, x, y):
    for i in range(1, len(text) + 1):
        img = font.render(text[:i], True, color)
        WIN.blit(img, (x, y))
        pygame.display.update()
        time.sleep (0.05)

def draw_window():
    WIN.fill((0, 0, 0))
    hearts = get_hearts(health)
    for heart, pos in hearts:
        WIN.blit(heart, pos)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:


        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        draw_window()
        draw_text("Zomboid: Rosewood Rising, welcome to the game based on Project Zomboid!", text_font, (255, 255, 255), 100, 200)
        pygame.display.update()
    
    
    pygame.quit()


if __name__ == "__main__":
    main()