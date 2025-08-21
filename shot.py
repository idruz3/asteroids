from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt