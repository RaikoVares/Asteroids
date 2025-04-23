

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, center = self.position, radius = self.radius, width=2)


    def update(dt)
        self.positsion += (self.velocity*dt)
