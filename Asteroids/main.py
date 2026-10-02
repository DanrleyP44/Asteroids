import sys

import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
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

    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)

    text_font = pygame.font.SysFont("Arial", 20)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    score = 0


    while True:
        dt = clock.tick(60) / 1000
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)


        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(ast):
                    log_event("asteroid_shot")
                    shot.kill()
                    ast.split()
                    if ast.radius <= ASTEROID_MIN_RADIUS:
                        score += SM_ASTEROID_PT
                    else:
                        score += LG_ASTEROID_PT


        screen.fill("black")
        text_score = f"Score: {score}"
        draw_text(text_score, text_font, (255, 255, 255), 0, 0)
        draw_text("Life: 3", text_font, (255, 255, 255), 1210, 0)

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()






if __name__ == "__main__":
    main()
