import random
import pygame
from pygame.locals import *

WIDTH = 1024
HEIGHT = 768
FONT = 'carlito'
FONT_SIZE = 36
BG_COLOUR = (255, 255, 255)
VELOCITY = 5
FPS = 60
WORDS_PER_SECOND = 1

WORD_LIST = ['HELLO', 'WORLD', 'APPLE', 'PEAR', 'BANANA', 'CAR', 'GRAPES']

pygame.init()

FramePerSec = pygame.time.Clock()

game_window = pygame.display.set_mode((WIDTH, HEIGHT))
game_window.fill(BG_COLOUR)

game_font = pygame.font.SysFont(FONT, FONT_SIZE)

class Text:
    def __init__(self, word):
        self.word = word
        self.y_pos = 0
        self.surface = game_font.render(self.word, False, (0, 0, 0))
        self.get_random_x_pos()

    def get_random_x_pos(self):
        self.size = game_font.size(self.word)
        self.x_pos = random.randrange(0, WIDTH - self.size[0], 50)

    def update_y_pos(self):
        self.y_pos += VELOCITY

    def draw_text(self):
        game_window.blit(self.surface, (self.x_pos, self.y_pos))

playing = True
cycle = 0
my_words = []
while playing:
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
    game_window.fill(BG_COLOUR)

    for word in my_words:
        word.update_y_pos()
        word.draw_text()

    if cycle == FPS / WORDS_PER_SECOND or cycle == 0:
        my_words.append(Text(random.choice(WORD_LIST)))
        cycle = 1
    cycle += 1

    pygame.display.update()
    FramePerSec.tick(FPS)
