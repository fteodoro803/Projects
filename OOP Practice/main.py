import pygame
import time
import math
from utils import scale_image, blit_rotate_center

GRASS = scale_image(pygame.image.load('images/grass.jpg'), 2.5)
TRACK = scale_image(pygame.image.load('images/track.png'), 0.9)
TRACK_BORDER = scale_image(pygame.image.load('images/track-border.png'), 0.9)

RED_CAR = scale_image(pygame.image.load('images/red-car.png'), 0.55)
GREEN_CAR = scale_image(pygame.image.load('images/green-car.png'), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Race')
FPS = 60


class AbstractCar:
    def __init__(self, max_velocity, rotation_velocity):
        self.img = self.IMG
        self.max_velocity = max_velocity
        self.velocity = 0
        self.rotation_velocity = rotation_velocity
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
        self.forward = True

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_velocity
        elif right:
            self.angle -= self.rotation_velocity

    def move_forward(self):
        self.velocity = min(self.velocity + self.acceleration, self.max_velocity)
        self.move()

    def reduce_speed(self):
        self.velocity = max(self.velocity - self.acceleration, 0)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        y = math.cos(radians) * self.velocity
        x = math.sin(radians) * self.velocity

        if self.forward:
            self.y -= y
            self.x -= x
        else:
            self.y += y
            self.x += x

    def draw(self, window):
        blit_rotate_center(window, self.img, (self.x, self.y), self.angle)


class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)


def draw(window, images, player_car):
    for img, pos in images:
        window.blit(img, pos)
    player_car.draw(window)
    pygame.display.update()


# MAIN
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
player_car = PlayerCar(4, 4)

run = True
while run:
    clock.tick(FPS)

    draw(WIN, images, player_car)

    keys = pygame.key.get_pressed()  # Keys Pressed

    # Exit Case
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if keys[pygame.K_ESCAPE]:
            run = False
            break

    # Movement
    # Rotation
    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)

    # Forward/Backward
    moved = False

    if keys[pygame.K_w]:
        moved = True
        player_car.forward = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.forward = False
        player_car.move_forward()

    # Speed Reduction
    if moved == False:
        player_car.reduce_speed()
