import random
import sys
import pygame
from pygame.locals import *

# Game Options
WIDTH = 1024
HEIGHT = 768
FONT = 'carlito'
FONT_SIZE = 72
BG_COLOUR = pygame.Color('0x584B53')
FONT_COLOUR = pygame.Color('0xFFBA0A')
SCORE_COLOUR = pygame.Color('0xF4F7F5')
END_SCREEN_COLOUR = pygame.Color('0x584B53')
VELOCITY = 180  # SHOULD BE MULTIPLE OF FPS
FPS = 60
WORDS_PER_SECOND = 0.5
WORD_FILE = './samples/sample_short_words.txt'
MIN_WORD_LENGTH = 4
MAX_WORD_LENGTH = 10
MAX_WORDS = 50
SOUND = True    # Will be set to False if issues opening audio files
VOLUME = 0.5    # Value between 0.0 and 1.0

# Game setup
pygame.init()
pygame.display.set_caption('Typing Trainer')

FramePerSec = pygame.time.Clock()

game_window = pygame.display.set_mode((WIDTH, HEIGHT))
game_window.fill(BG_COLOUR)

game_font = pygame.font.SysFont(FONT, FONT_SIZE)
score_font = pygame.font.SysFont(FONT, FONT_SIZE // 2)
end_screen_font = pygame.font.SysFont(FONT, FONT_SIZE)
title_font = pygame.font.SysFont(FONT, int(FONT_SIZE * 1.5))

try:
    success_sound = pygame.mixer.Sound('assets/success.ogg')
    mistake_sound = pygame.mixer.Sound('assets/mistake.ogg')
    missed_sound = pygame.mixer.Sound('assets/missed.ogg')
    success_sound.set_volume(VOLUME)
    mistake_sound.set_volume(VOLUME)
    missed_sound.set_volume(VOLUME)
except:
    SOUND = False

# Word class
class Word:
    def __init__(self, word):
        self.word = word
        self.size = game_font.size(self.word)
        self.x_pos = self.get_random_x_pos()
        self.y_pos = 0
        self.set_surface()

    def get_random_x_pos(self):
        return random.randrange(10, WIDTH - self.size[0] - 10, 50)

    def set_surface(self):
        self.surface = game_font.render(self.word, True, FONT_COLOUR)

    def update_y_pos(self):
        self.y_pos += VELOCITY // FPS

    def draw_text(self):
        game_window.blit(self.surface, (self.x_pos, self.y_pos))

    def update_word(self):
        if len(self.word) > 1:
            self.word = self.word[1:]
        else:
            self.word = " "
        self.set_surface()

# Read word file and create word list
def create_word_list():
    word_list = []
    try:
        with open(WORD_FILE) as f:
            words = f.readlines()
            for word in words:
                word = word.strip()
                if len(word) >= MIN_WORD_LENGTH and len(word) <= MAX_WORD_LENGTH:
                    word_list.append(word.upper())
    except:
        word_list = ['PANDA', 'GIRAFFE', 'DOG', 'CAT', 'ZEBRA', 'ELEPHANT']
    return word_list

# Move words down the screen and delete if hit the bottom
def move_word_and_delete(game_words):
    missed_words = 0
    for word in list(game_words):
        word.update_y_pos()
        if word.y_pos + word.size[1] >= HEIGHT:
            if SOUND:
                missed_sound.play()
            game_words.remove(word)
            missed_words += 1
        else:
            word.draw_text()
    return missed_words

# Add words to list
def add_words(cycle, game_words, num_words, total_chars, word_list):
    if cycle == FPS / WORDS_PER_SECOND or cycle == 0:
        new_word = Word(random.choice(word_list))
        game_words.append(new_word)
        cycle = 1
        num_words += 1
        total_chars += len(new_word.word)
    return cycle + 1, num_words, total_chars

# Check if typed letter is at start of word and update word
def check_letter_of_word(letter, game_words):
    for word in list(game_words):
        if letter == word.word[0].lower():
            word.update_word()
            if word.word == " ":
                if SOUND:
                    success_sound.play()
                game_words.remove(word)
            break
    else:
        if SOUND:
            mistake_sound.play()
        return 1
    return 0

# Write score info to screen
def write_score_info(remaining, missed, mistakes):
    score_font_size = score_font.size('Missed')[1]
    remaining_text_surface = score_font.render(f'Remaining: {remaining} / {MAX_WORDS}', True, SCORE_COLOUR)
    game_window.blit(remaining_text_surface, (5, 5))
    missing_text_surface = score_font.render(f'Missed: {missed}', True, SCORE_COLOUR)
    game_window.blit(missing_text_surface, (5, HEIGHT - score_font_size * 2))
    mistakes_text_surface = score_font.render(f'Mistakes: {mistakes}', True, SCORE_COLOUR)
    game_window.blit(mistakes_text_surface, (5, HEIGHT -  score_font_size))

def write_ending_score(mistakes, missed, total_chars):
    accuracy = (1 - (mistakes / total_chars)) * 100

    title_font_size = title_font.size(f'Well done!')
    missed_font_size = end_screen_font.size(f'Words Missed: {missed}')
    mistakes_font_size = end_screen_font.size(f'Mistakes: {mistakes}')
    accuracy_font_size = end_screen_font.size(f'Accuracy: {accuracy:.2f}%')
    instruction_font_size = score_font.size("Press 'ENTER' to play again or 'ESC' to quit")

    title_text_surface = title_font.render(f'Well done!', True, FONT_COLOUR)
    missed_text_surface = end_screen_font.render(f'Words Missed: {missed}', True, SCORE_COLOUR)
    mistakes_text_surface = end_screen_font.render(f'Mistakes: {mistakes}', True, SCORE_COLOUR)
    accuracy_text_surface = end_screen_font.render(f'Accuracy: {accuracy:.2f}%', True, SCORE_COLOUR)
    instruction_text_surface = score_font.render("Press 'ENTER' to play again or 'ESC' to quit", True, FONT_COLOUR)

    game_window.blit(title_text_surface, ((WIDTH // 2) - (title_font_size[0] // 2), 50))
    game_window.blit(missed_text_surface, ((WIDTH // 2) - (missed_font_size[0] // 2), HEIGHT // 2 - 50))
    game_window.blit(mistakes_text_surface, ((WIDTH // 2) - (mistakes_font_size[0] // 2), (HEIGHT // 2) + (missed_font_size[1]) - 50))
    game_window.blit(accuracy_text_surface, ((WIDTH // 2) - (accuracy_font_size[0] // 2), (HEIGHT // 2) + (2 * missed_font_size[1]) - 50))
    game_window.blit(instruction_text_surface, ((WIDTH // 2) - (instruction_font_size[0] // 2), HEIGHT - 50 - instruction_font_size[1]))


def write_title_screen():

    title_font_size = title_font.size('TYPING TRAINER')
    instruction_font_size = score_font.size("Press 'ENTER' to play or 'ESC' to quit")

    title_text_surface = title_font.render('TYPING TRAINER', True, FONT_COLOUR)
    instruction_text_surface = score_font.render("Press 'ENTER' to play or 'ESC' to quit", True, FONT_COLOUR)

    game_window.blit(title_text_surface, ((WIDTH // 2) - (title_font_size[0] // 2), 50))
    game_window.blit(instruction_text_surface, ((WIDTH // 2) - (instruction_font_size[0] // 2), HEIGHT - 50 - instruction_font_size[1]))


# Title Screen
def title_screen():
    game_over = True
    while game_over == True:
        game_window.fill(END_SCREEN_COLOUR)
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_over = False
                elif event.key == K_RETURN:
                    game()
        write_title_screen()
        pygame.display.update()
        FramePerSec.tick(FPS)
    pygame.quit()
    sys.exit()

# Game Loop
def game():
    playing = True
    cycle = 0
    missed = 0
    mistakes = 0
    word_list = create_word_list()
    game_words = []
    num_words = 0
    total_chars = 0
    while playing == True:
        # Event checking
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                try:
                    mistakes += check_letter_of_word(chr(event.key), game_words)
                except ValueError:
                    pass

        game_window.fill(BG_COLOUR)

        # Move words down the screen
        missed += move_word_and_delete(game_words)

        # Add words to word list at specific intervals, if less than max words
        if num_words < MAX_WORDS:
            cycle, num_words, total_chars = add_words(cycle, game_words, num_words, total_chars, word_list)
        elif len(game_words) == 0:
            playing = False
        # Update score
        remaining = MAX_WORDS - num_words + len(game_words)
        write_score_info(remaining, missed, mistakes)
        pygame.display.update()
        FramePerSec.tick(FPS)
    pygame.time.delay(500)
    end_screen(mistakes, missed, total_chars)

# End Screen
def end_screen(mistakes, missed, total_chars):
    game_over = True
    while game_over == True:
        game_window.fill(END_SCREEN_COLOUR)

        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_over = False
                elif event.key == K_RETURN:
                    game()
        write_ending_score(mistakes, missed, total_chars)
        pygame.display.update()
        FramePerSec.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    title_screen()
