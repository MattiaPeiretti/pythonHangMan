import sys
import random
import pygame
from tkinter import messagebox
import time

# COSTANTS
MIN_ASCII_VALUE = 97
MAX_ASCII_VALUE = 122

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500

BACKGROUND_COLOR = (0, 0, 0)
FOREGROUND_COLOR = (255, 255, 255)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 24)
myfont_big = pygame.font.SysFont('Comic Sans', 54)


nouns = [
    'people',
    'history',
    'way',
    'art',
    'world',
    'information',
    'map',
    'two',
    'family',
    'government',
    'health',
    'system',
    'computer',
    'meat',
    'year',
    'thanks',
    'music',
    'person',
    'reading',
    'method',
    'data',
    'food',
    'understanding',
    'theory',
    'law',
    'bird',
    'literature',
    'problem',
    'software',
    'control',
    'knowledge',
    'power',
    'ability',
    'economics',
    'love',
    'internet',
    'television',
    'science',
    'library',
    'nature',
    'fact',
    'product',
    'idea',
    'temperature',
    'investment',
    'area',
    'society',
    'activity',
    'story',
    'industry',
    'media',
    'thing',
    'oven',
    'community',
    'definition',
    'safety',
    'quality',
    'development',
    'language',
    'management',
    'player',
    'variety',
    'video',
    'week',
    'security',
    'country',
    'exam',
    'movie',
    'organization',
    'equipment',
    'physics',
    'analysis',
    'policy',
    'series',
    'thought',
    'basis',
    'boyfriend',
    'direction',
    'strategy',
    'technology',
    'army',
    'camera',
    'freedom',
    'paper',
    'environment',
    'child',
    'instance',
    'month',
    'truth',
    'marketing',
    'university',
    'writing',
    'article',
    'department',
    'difference',
    'goal',
    'news',
    'audience',
    'fishing',
    'growth',
    'income',
    'marriage',
    'user',
    'combination',
    'failure',
    'meaning',
    'medicine',
    'philosophy',
    'teacher',
    'communication',
    'night',
    'chemistry',
    'disease',
    'disk',
    'energy',
    'nation',
    'road',
    'role',
    'soup',
    'advertising',
    'location',
    'success',
    'addition',
    'apartment',
    'education',
    'math',
    'moment',
    'painting',
    'politics',
    'attention',
    'decision',
    'event',
    'property',
    'shopping',
    'student',
    'wood',
    'competition',
    'distribution',
    'entertainment',
    'office',
    'population',
    'president',
    'unit',
    'category',
    'cigarette',
    'context',
    'introduction',
    'opportunity',
    'performance',
    'driver',
    'flight',
    'length',
    'magazine',
    'newspaper',
    'relationship',
    'teaching',
    'cell',
    'dealer',
    'debate',
    'finding',
    'lake',
    'member',
    'message',
    'phone',
    'scene',
    'appearance',
    'association',
    'concept',
    'customer',
    'death',
    'discussion',
    'housing',
    'inflation',
    'insurance',
    'mood']

compliments = [
    'Good one!!',
    'Good!',
    'Well Done!',
    'Nice!',
    'Right!'
]


class stick_man:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color

    def draw_head(self):
        pygame.draw.circle(self.screen, self.color, (200, 60), 20, 1)

    def draw_body(self):
        pygame.draw.line(self.screen, self.color, (200, 80), (200, 160))

    def draw_left_arm(self):
        pygame.draw.line(self.screen, self.color, (200, 90), (170, 120))

    def draw_right_arm(self):
        pygame.draw.line(self.screen, self.color, (200, 90), (230, 120))

    def draw_left_leg(self):
        pygame.draw.line(self.screen, self.color, (200, 160), (230, 200))

    def draw_right_leg(self):
        pygame.draw.line(self.screen, self.color, (200, 160), (170, 200))


def sleep(sec):
    for _ in range(0, sec*1000):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
        time.sleep(0.001)


def draw_base(screen, FOREGROUND_COLOR):
    pygame.draw.line(screen, FOREGROUND_COLOR, (20, 20), (20, 300))
    pygame.draw.line(screen, FOREGROUND_COLOR, (20, 300), (80, 300))
    pygame.draw.line(screen, FOREGROUND_COLOR, (20, 20), (200, 20))
    pygame.draw.line(screen, FOREGROUND_COLOR, (200, 20), (200, 40))


def main():
    pygame.display.set_caption('Hang man')
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(BACKGROUND_COLOR)

    p = stick_man(screen, FOREGROUND_COLOR)

    errors = 0
    line1 = ''
    line2 = 'Please, select a letter: '
    line3 = 'Number of errors: '
    word = ''
    processed_word = '-'

    running = True
    while running:

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
        screen.fill(BACKGROUND_COLOR)

        if errors > 0:
            p.draw_head()

        if errors > 1:
            p.draw_body()

        if errors > 2:
            p.draw_left_arm()

        if errors > 3:
            p.draw_right_arm()

        if errors > 4:
            p.draw_left_leg()

        if errors > 5:
            p.draw_right_leg()
            pygame.display.flip()
            sleep(2)
            show_message_box(screen, 'GAME OVER!!')
            errors = 0

        else:
            if processed_word.find('-') == -1:
                show_message_box(screen, random.choice(compliments))
                word = ''
                errors = 0

            if word == '':
                word = generate_word()
                processed_word = word[0] + '-'*(len(word)-2) + word[len(word)-1]

            line1 = processed_word

            display_message(screen, line1, FOREGROUND_COLOR, (50, 320))
            display_message(screen, line2, FOREGROUND_COLOR, (50, 350))
            display_message(screen, line3 + str(errors), FOREGROUND_COLOR, (50, 380))

            line2 = 'Please, select a letter: '
            draw_base(screen, FOREGROUND_COLOR)
            pygame.display.flip()

            letter = ask_letter(screen, 80, 350)
            line2 = 'You selected the letter: ' + letter
            print(word)
            word = list(word)
            word[len(word)-1] = '1'
            word[0] = '1'

            if letter in word:
                letter_pos = [i for i, a in enumerate(word) if a == letter]
                processed_word = list(processed_word)
                for key in letter_pos:
                    processed_word[key] = letter
                    word[key] = '1'
                processed_word = ''.join(processed_word)
                line1 = processed_word

            else:
                errors += 1


def display_message(screen, message, color, pos=(50, 30)):
    text = myfont.render(message, False, color)
    screen.blit(text, pos)


def show_message_box(screen, message):
    pygame.event.pump()
    screen.fill((0, 0, 0))
    text = myfont_big.render(message, False, (255, 255, 255))
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.flip()

    sleep(3)
    screen.fill((0, 0, 0))
    pygame.display.flip()


def detect_pressed_key(screen, key_pressed_ascii):
    key_pressed = ""
    if key_pressed_ascii >= MIN_ASCII_VALUE and key_pressed_ascii <= MAX_ASCII_VALUE:
        key_pressed = chr(key_pressed_ascii)
        if key_pressed == "":
            pass
        else:
            return key_pressed
    else:

        return key_pressed


def ask_letter(screen, cord_x=50, cord_y=50):
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            if events.type == pygame.KEYDOWN:
                letter = detect_pressed_key(screen, events.key)
                running = False
    return letter


def generate_word():
    word = random.choice(nouns)
    return word


main()
