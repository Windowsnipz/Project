import pygame
import os

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zomboid: Rosewood Rising")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "spiffo.png")))

FPS = 60
HEART = pygame.image.load(os.path.join("Assets", "heart.png"))
HEART_EMPTY = pygame.image.load(os.path.join("Assets", "heart_empty.png"))
HEART_HALF = pygame.image.load(os.path.join("Assets", "heart_half.png"))
hearts = [(HEART, (360, 400)), (HEART, (390, 400)), (HEART, (420, 400)), 
          (HEART_HALF, (450, 400)), (HEART_EMPTY, (480, 400))]

def draw_window():
    WIN.fill((0, 0, 0))
    for heart, pos in hearts:
        WIN.blit(heart, pos)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        draw_window()
    
    
    pygame.quit()


if __name__ == "__main__":
    main()