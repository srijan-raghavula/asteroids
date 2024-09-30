import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    def draw(self, screen):
        pass
    def update(self, dt):
        pass
    def is_colliding(self, cs):
        dist = self.position.distance_to(cs.position)
        if dist > self.radius + cs.radius:
            return False
        return True
