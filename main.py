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
          (HEART, (450, 400)), (HEART, (480, 400))]
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
    

def draw_window():
    WIN.fill((0, 0, 0))
    hearts = get_hearts(health)
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