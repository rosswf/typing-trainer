import random
import pygame
from pygame.locals import *

# Constants
WIDTH = 1024
HEIGHT = 768
FONT = 'carlito'
FONT_SIZE = 36
BG_COLOUR = (255, 255, 255)
FONT_COLOUR = (0, 255, 255)
VELOCITY = 5
FPS = 60
WORDS_PER_SECOND = 1
WORD_FILE = 'words.txt'
MIN_WORD_LENGTH = 4
MAX_WORD_LENGTH = 8
WORD_LIST = ['HELLO', 'WORLD', 'APPLE', 'PEAR', 'BANANA', 'CAR', 'GRAPES']

# Game setup
pygame.init()

FramePerSec = pygame.time.Clock()

game_window = pygame.display.set_mode((WIDTH, HEIGHT))
game_window.fill(BG_COLOUR)

game_font = pygame.font.SysFont(FONT, FONT_SIZE)


# Word class
class Word:
    def __init__(self, word):
        self.word = word
        self.size = game_font.size(self.word)
        self.x_pos = self.get_random_x_pos()
        self.y_pos = 0
        self.surface = game_font.render(self.word, True, FONT_COLOUR)

    def get_random_x_pos(self):
        return random.randrange(10, WIDTH - self.size[0], 50)

    def update_y_pos(self):
        self.y_pos += VELOCITY

    def draw_text(self):
        game_window.blit(self.surface, (self.x_pos, self.y_pos))

# Read word file and create word list
def create_word_list():
    word_list = []
    with open(WORD_FILE) as f:
        words = f.readlines()
        for word in words:
            word = word.strip()
            if len(word) >= MIN_WORD_LENGTH and len(word) <= MAX_WORD_LENGTH:
                word_list.append(word.upper())
    return word_list

# Move words down the screen and delete if hit the bottom
def move_word_and_delete(game_words):
    for word in game_words:
        word.update_y_pos()
        if word.y_pos + word.size[1] >= HEIGHT:
            game_words.remove(word)
        else:
            word.draw_text()

def add_words(cycle, game_words):
    if cycle == FPS / WORDS_PER_SECOND or cycle ==0:
        game_words.append(Word(random.choice(word_list)))
        cycle = 1
    return cycle + 1

# Game Loop
playing = True
cycle = 0
word_list = create_word_list()
game_words = []
while playing:
    # Event checking
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
    game_window.fill(BG_COLOUR)

    # Move words down the screen
    move_word_and_delete(game_words)

    # Add words to word list at specific intervals
    cycle = add_words(cycle, game_words)

    pygame.display.update()
    FramePerSec.tick(FPS)
