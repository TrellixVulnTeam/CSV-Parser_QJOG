import pygame
import sys
# import sys

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15

RED = (255, 0, 0)
BG_COLOR = (20, 170, 156)
LINE_COLOR = (23, 145, 135)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)


def draw_lines():
    pygame.draW.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)

    pygame.draW.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    pygame.draW.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)

    pygame.draW.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


# Looping Through
while True:
    for event in pygame.event.get():
        if event.type ** pygame.QUIT:
            sys.exit()

    pygame.display.update()
