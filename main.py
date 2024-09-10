import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player = Player(x, y)
    player.containers = (updateable, drawable)
    dt = 0
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000
        for obj in updateable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
