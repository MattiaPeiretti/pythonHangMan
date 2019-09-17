import sys
import random
import pygame
from tkinter import messagebox
import time
from nouns import nouns, compliments

# COSTANTS
MIN_ASCII_VALUE = 97
MAX_ASCII_VALUE = 122

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BACKGROUND_COLOR = (0, 0, 0)
FOREGROUND_COLOR = (255, 255, 255)

DELAY_COSTANT = 500 # custom costant

pygame.font.init() #font init

#defining the 3 main fonts, a small one, a medium, and a large...
myfont = pygame.font.SysFont('Comic Sans MS', 24)
myfont_big = pygame.font.SysFont('Comic Sans', 54)
myfont_small = pygame.font.SysFont('sans serif', 20)



class stick_man: #defining class for the stickman, with func(s) to draw all parts of the body..
    def __init__(self, screen, color):
        self.screen = screen #selecting screen surface
        self.color = color #selecting color of the stickman

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

def sleep(sec): #definig a sleep function
    # i made a custom function 'cause, using the built in one, the program freezes...
    # this way, instead, i loop thru the pygame events (process that takes around 0.0005 s), with a for loop
    # So that i can send the program 'to sleep' haha, without any problem... ;)
    for _ in range(0, sec*DELAY_COSTANT):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
        time.sleep(0.001)

def draw_base(screen, FOREGROUND_COLOR): #draws the basic components, the ones that are always present, like the hang or the credits
    pygame.draw.line(screen, FOREGROUND_COLOR, (20, 20), (20, 300))
    pygame.draw.line(screen, FOREGROUND_COLOR, (20, 300), (80, 300))
    pygame.draw.line(screen, FOREGROUND_COLOR, (20, 20), (200, 20))
    pygame.draw.line(screen, FOREGROUND_COLOR, (200, 20), (200, 40))
    display_message(screen, 'Program made by Mattia Peiretti - www.mattiapeiretti.com', FOREGROUND_COLOR, (10, WINDOW_HEIGHT - 50), myfont_small)
    display_message(screen, '09-2019', FOREGROUND_COLOR, (10, WINDOW_HEIGHT - 30), myfont_small)

def generate_screen(width, height, BACKGROUND_COLOR): #screen init
    screen = pygame.display.set_mode((width, height))
    screen.fill(BACKGROUND_COLOR)
    return screen

def generate_word(): #picks a random word from a list of nouns
    word = random.choice(nouns)
    return word

def generate_censured_word(word): #generates a censured version of the random word, eg. pizza become p---a
    processed_word = word[0] + '-'*(len(word)-2) + word[len(word)-1] #putting - instead of the letters in the center
    return processed_word

def display_message(screen, message, color, pos=(50, 30), font = myfont): # printing text on the screen surface
    text = font.render(message, False, color)
    screen.blit(text, pos)

def show_message_box(screen, message, showtime): #showing a messagebox, like a notification for the user
    screen.fill((0, 0, 0)) #filling screen black
    text = myfont_big.render(message, False, (255, 255, 255)) #rendering text
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)) #centering text in the center of the window
    screen.blit(text, text_rect) 
    pygame.display.flip() #updating screen

    sleep(showtime)
    screen.fill((0, 0, 0)) 
    pygame.display.flip() #updating screen

def get_char_from_ascii(screen, key_pressed_ascii): #converting ascii code to char var
    if key_pressed_ascii >= MIN_ASCII_VALUE and key_pressed_ascii <= MAX_ASCII_VALUE: #checking if it is a letter
        key_pressed = chr(key_pressed_ascii) #converting ascii num to char
        if not key_pressed == "":
            return key_pressed #returning letter as a string
    else:
        return '' #return a empty str if the pressed key is not a letter, but maybe a special char, like !@#$%^&* etc...

def ask_letter(screen, cord_x=50, cord_y=50): #waiting for user to input a letter
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            if events.type == pygame.KEYDOWN: #if a key gets pressed
                letter = get_char_from_ascii(screen, events.key) #returns letter from ascii value
                running = False #killing loop
    return letter





def main():
    screen = generate_screen(WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR) #Init the screen 
    person = stick_man(screen, FOREGROUND_COLOR) #Init person class

    #Just some vars
    errors = 0
    line1 = ''
    line2 = 'Please, select a letter: '
    line3 = 'Number of errors: '
    word = ''
    processed_word = '-'

    running = True
    while running: #loop...
        #checking for events during the loop, this prevents the window from freezing
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit() #killing program on close event

        if errors > 5: #checking if the max number of errors has been reached
            person.draw_right_leg() #drawing the last piece of the person
            pygame.display.flip() #updating the screen
            sleep(2) #delay of 2 sec to show the complete drawing of the person
            show_message_box(screen, 'GAME OVER!!', 3) #showing the gameover screen
            #init the two vars again \/
            word = ''
            errors = 0

        else: #if the max number of errors has not been reached, then
            if processed_word.find('-') == -1: #checking if the word still contains slots that need to be filled
                show_message_box(screen, random.choice(compliments), 3) #displaying a compliment to indicate that the user won
                word = ''
                errors = 0

            if word == '': #checking if word is not init
                word = generate_word() #generating a new random word
                processed_word = generate_censured_word(word) #generating a copy of the word with - instead of the letter in the center

            line1 = processed_word

            #displaying the 3 lines of text
            display_message(screen, line1, FOREGROUND_COLOR, (50, 320)) #word to guess
            display_message(screen, line2, FOREGROUND_COLOR, (50, 350)) #selected letter
            display_message(screen, line3 + str(errors), FOREGROUND_COLOR, (50, 380)) #num of errors

            line2 = 'Please, select a letter: '
            draw_base(screen, FOREGROUND_COLOR)
            pygame.display.flip() #updating the screen
            screen.fill(BACKGROUND_COLOR) #filling the screen black

            letter = ask_letter(screen, 80, 350) #asking for input
            if letter == '':
                show_message_box(screen, 'Please, insert only letters!', 2) #checking if the input consists of only letters
            line2 = 'You selected the letter: ' + letter
            print('[DEBUG] The word is: ' + ''.join(word))
            word = list(word) #changing word from str to list, so that every letter is accesible individually...
            word[len(word)-1] = word[0] = '1' # changing the first and last letter of the word to 1 so that even if the user input those letter, they will be counted as wrong

            if letter in word: #checking if the letter selected is in word
                letter_pos = [i for i, a in enumerate(word) if a == letter] #getting the posisiton of the letter(s) present in the word
                processed_word = list(processed_word) #changing processed_word from str to list, so that every letter is accesible individually...
                for key in letter_pos: #adding the selected letter to processed_word 
                    processed_word[key] = letter 
                    word[key] = '1' #setting the seleted letter to 1 in word so that the statement does not accept is as true if input a second time
                processed_word = ''.join(processed_word) #converting the word again into a str
                line1 = processed_word #setting processed_word to be displayed

            else:
                errors += 1 #incrementing errors if the selected letter is wrong

                if errors > 0:
                    person.draw_head()

                if errors > 1:
                    person.draw_body()

                if errors > 2:
                    person.draw_left_arm()

                if errors > 3:
                    person.draw_right_arm()

                if errors > 4:
                    person.draw_left_leg()

if __name__ == '__main__':
    main()