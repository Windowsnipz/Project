import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zomboid: Rosewood Rising")
pygame.display.set_icon(pygame.image.load("Assets/spiffo.png"))


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    
    
    pygame.quit()


if __name__ == "__main__":
    main()