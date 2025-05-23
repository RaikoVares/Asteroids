import pygame
import random

from circle_shape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, color = "white", center = self.position, radius = self.radius, width=2)


    def update(self, dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = velocity1 * 1.2

            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = velocity2 * 1.2

