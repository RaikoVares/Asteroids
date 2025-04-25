import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable_gp = pygame.sprite.Group()
    drawable_gp = pygame.sprite.Group()
    asteroids_gp = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()


    Player.containers = (updatable_gp, drawable_gp)
    Asteroid.containers = (updatable_gp, drawable_gp, asteroids_gp)
    AsteroidField.containers = (updatable_gp)
    Shot.containers = (updatable_gp, drawable_gp, player_shots)

    player = Player(x = SCREEN_WIDTH / 2, 
                    y = SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable_gp.update(dt)

        for item in drawable_gp:
            item.draw(screen)

        for asteroid in asteroids_gp:
            if player.circle_collision(asteroid):
                print("Game over!")
                sys.exit()
            
        pygame.display.flip()

        time_passed = clock.tick(60)
        dt = time_passed / 1000


if __name__ == "__main__":
    main()
