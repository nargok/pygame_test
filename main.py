import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()
    (w, h) = (500, 637)
    (x, y) = (w/2, h/2)

    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()

    pygame.display.set_caption("Pygame Test")
    bg = pygame.image.load("akasaka.jpg").convert_alpha()
    rect_bg = bg.get_rect()
    player = pygame.image.load("yuusya_game.png").convert_alpha()
    rect_player = player.get_rect()
    rect_player.center = (x, y)

    while(True):
        screen.fill((0, 0, 0, 0))
        screen.blit(bg, rect_bg)
        screen.blit(player, rect_player)
        pygame.time.wait(10)
        pygame.display.update()
        x += 1
        y += 1
        rect_player.center = (x, y)
        if x > w:
            x = 0
        if y > h:
            y = 0

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