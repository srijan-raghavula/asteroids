import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)


    asteroidfield = AsteroidField()
    player = Player(x, y)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000
        for obj in updateable:
            obj.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
            if asteroid.is_colliding(player):
                print("Game Over!")
                sys.exit()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
