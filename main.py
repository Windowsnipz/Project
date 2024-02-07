import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False