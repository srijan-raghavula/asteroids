from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', (self.position.x, self.position.y), self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        positive_angle = self.velocity.rotate(angle)
        negative_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = positive_angle * 1.2
        asteroid_2.velocity = negative_angle * 1.2
