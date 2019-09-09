import sys
import random
import pygame
from tkinter import messagebox


#COSTANTS
MIN_ASCII_VALUE = 97 
MAX_ASCII_VALUE = 122

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500

BACKGROUND_COLOR=(0,0,0)
FOREGROUND_COLOR=(255,255,255)

pygame.font.init()               
myfont = pygame.font.SysFont('Comic Sans MS', 24)


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




class stick_man:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color

    def draw_head(self):
        pygame.draw.circle(self.screen, self.color, (200, 60), 20, 1)
    
    def draw_body(self):
        pygame.draw.line(self.screen, self.color ,(200, 80), (200, 160))
        
    def draw_left_arm(self):
        pygame.draw.line(self.screen, self.color ,(200, 90), (170, 120))

    def draw_right_arm(self):
        pygame.draw.line(self.screen, self.color ,(200, 90), (230, 120))

    def draw_left_leg(self):
        pygame.draw.line(self.screen, self.color ,(200, 160), (230, 200))

    def draw_right_leg(self):
        pygame.draw.line(self.screen, self.color ,(200, 160), (170, 200))

def draw_base(screen, FOREGROUND_COLOR):
    pygame.draw.line(screen, FOREGROUND_COLOR,(20,20),(20,300))
    pygame.draw.line(screen, FOREGROUND_COLOR,(20,300),(80,300))
    pygame.draw.line(screen, FOREGROUND_COLOR,(20,20),(200,20))
    pygame.draw.line(screen, FOREGROUND_COLOR,(200,20),(200,40))


def main():
    pygame.display.set_caption('Hang man') 
    screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    screen.fill(BACKGROUND_COLOR)

    p = stick_man(screen, FOREGROUND_COLOR)
    draw_base(screen, FOREGROUND_COLOR)
    key_pressed = ""

  
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_base(screen, FOREGROUND_COLOR)
    
        p.draw_head()
        p.draw_body()

        #word = generate_word()

        #letter = ask_letter(screen, 80, 350)     

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                 sys.exit()
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

def ask_letter(screen, cord_x = 50, cord_y = 50):
    text_insert_letter = myfont.render('Please insert a letter:', False, FOREGROUND_COLOR)
    running = True
    while running:
        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                 sys.exit()
            if events.type == pygame.KEYDOWN:
                letter = detect_pressed_key(screen, events.key)
                text_insert_letter = myfont.render('Please insert a letter: ' + letter, False, FOREGROUND_COLOR)
                running = False
    screen.blit(text_insert_letter,(cord_x,cord_y))
    return letter
               

def generate_word():
    word = random.choice(nouns)
    length = len(word)
    first_letter = word[0]
    last_letter = word[length-1]
    return word
    




main()

