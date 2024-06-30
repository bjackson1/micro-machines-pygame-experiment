import sys, pygame, math
from pygame.constants import K_RIGHT
pygame.init()

size = width, height = 1200, 800
window = pygame.display.set_mode(size)
background = pygame.image.load("./crayon-canyon.png").convert()
car = pygame.image.load("./car-sprite.png").convert()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

x, y = 0, 0
min_x = -background.get_height() + size[1]
min_y = -background.get_width() + size[0]

# speed = [0, 0]
speed = 2
map_position = [0, 0]
car_rect = car.get_rect()
angle = 180
black = 0, 0, 0

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

clock = pygame.time.Clock()
frame_rate = 30

def redraw():
    rotated_car = pygame.transform.rotate(car, angle)
    window.blit(background, map_position)
    window.blit(rotated_car, car_rect)
    pygame.display.flip()

def calculat_new_xy(old_rect, speed, angle_in_radians):
    new_x = old_rect.top + (speed * math.cos(angle_in_radians))
    new_y = old_rect.left + (speed * math.sin(angle_in_radians))
    old_rect.top = new_x
    old_rect.left = new_y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        speed = min(speed + 1, 8)

    if keys[pygame.K_DOWN]:
        speed = max(speed - 1, 0)

    if keys[pygame.K_RIGHT]:
        angle = angle - 0.1

        if angle < 0:
            angle = angle + 360

    if keys[pygame.K_LEFT]:
        angle = angle + 0.1

        if angle > 360:
            angle = angle - 360

    if car_rect.left < 0 or car_rect.right > width:
        speed = 0

        if car_rect.left < 0:
            car_rect.left = 0

        if car_rect.right > width:
            car_rect.right = width

    if car_rect.top < 0 or car_rect.bottom > height:
        speed = 0

        if car_rect.top < 0:
            car_rect.top = 0

        if car_rect.bottom > height:
            car_rect.bottom = height

    # car_rect = car_rect.move(speed)
    calculat_new_xy(car_rect, speed, angle)
    redraw()

    clock.tick(frame_rate)
