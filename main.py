import pygame
from pygame.locals import *
import sys

def main():
    # print("hello pygame!")
    pygame.init()
    screen = pygame.display.set_mode((500, 637))

    pygame.display.set_caption("Pygame Test")
    bg = pygame.image.load("akasaka.jpg").convert_alpha()
    rect_bg = bg.get_rect()

    while(True):
        screen.fill((0, 0, 0, 0))
        screen.blit(bg, rect_bg)
        pygame.time.wait(30)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()