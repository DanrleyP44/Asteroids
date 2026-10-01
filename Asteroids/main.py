import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    new_asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
