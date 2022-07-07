import pygame
from pygame.locals import *
import random
# ! Prerequisite: install PyGame
# !What is a module? What does an import statement do?

# Define colors in RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)

pygame.init()
w, h = 1000, 1000
screen = pygame.display.set_mode((w, h))
screen.fill(WHITE)
pygame.display.set_caption('Hangman')
my_font = pygame.font.SysFont('ubuntumono.ttf', 50) # !What is a file? What can we do with a file in Python?

pygame.display.update()

# Drawing on x-y coordinate based canva 
def draw_hangman(chances): #! What is a function? What is a parameter?
    # Frame
    pygame.draw.line(screen, BLACK, (100, 100), (500, 100), width=5) # !What is the data type of the coordinate pairs?
    pygame.draw.line(screen, BLACK, (100, 100), (100, 700), width=5)
    pygame.draw.line(screen, BLACK, (0, 700), (300, 700), width=5)
    pygame.draw.line(screen, BLACK, (100, 200), (200, 100), width=10)
    # Rope 
    pygame.draw.line(screen, BLACK, (300, 175), (300, 100), width=5)
    # Head
    pygame.draw.circle(screen, WHITE if chances < 1 else BLACK, (300, 250), 75, width=5)
    # Body
    pygame.draw.line(screen, WHITE if chances < 2 else BLACK, (300, 325), (300, 525), width=5)
    # Left Arm
    pygame.draw.line(screen, WHITE if chances < 3 else BLACK, (300, 325), (150, 400), width=5)
    # Right Arm
    pygame.draw.line(screen, WHITE if chances < 4 else BLACK, (300, 325), (450, 400), width=5)
    # Left Leg
    pygame.draw.line(screen, WHITE if chances < 5 else BLACK, (300, 525), (150, 600), width=5)
    # Right Leg
    pygame.draw.line(screen, WHITE if chances < 6 else BLACK, (300, 525), (450, 600), width=5)
    pygame.display.update()

LETTERS =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # !What is this data type?
RECTS = {} # ! What is this data structure? 

def draw_letters():
    for i in range(len(LETTERS)):
        letter = LETTERS[i]
        text = my_font.render(letter, True, BLACK)
        textRect = text.get_rect()
        RECTS[LETTERS[i]] = textRect
        if i < 13:
            textRect.center = (150+i*60, 800)
        else:
            textRect.center = (150+(i-13)*60, 900)
        screen.blit(text, textRect)
    pygame.display.update()


with open("vocab.txt") as f:
    vocab = f.read().split('\n')

word = random.choice(vocab) # TODO: add a list of words and randomly pick one
guessed = [False]*len(word) # ! What is this data structure? 

def draw_word(word, guessed):
    for i in range(len(word)):
        start = 550+i*55
        end = start+40
        if i < 7:
            if guessed[i]:
                text = my_font.render(word[i], True, BLACK)
                textRect = text.get_rect()
                textRect.center = (start+10, 275)
                screen.blit(text, textRect)
            pygame.draw.line(screen, BLACK, (start, 300), (end, 300), width=4)
        else:
            if guessed[i]:
                text = my_font.render(word[i], True, BLACK)
                textRect = text.get_rect()
                textRect.center = (start+10-7*55, 375)
                screen.blit(text, textRect)
            pygame.draw.line(screen, BLACK, (start-7*55, 400), (end-7*55, 400), width=4)
    pygame.display.update()

def verify_guess(word, guessed, guess):
    if not guess in word:
        print("You guessed wrong with "+guess)
        return False
    for i in range(len(word)):
        if word[i] == guess:
            print("You guessed "+word[i]+" correctly")
            guessed[i] = True
    return True


running = True # ! What is this data type?
chances = 6 # ! What is this data type?
ending_word = "YOU WIN"

while running: # ! What is this loop? Difference for and while loops?
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN: 
            for letter in LETTERS:
                if RECTS[letter].collidepoint(event.pos):
                    if verify_guess(word, guessed, letter):
                        if not (False in guessed):
                                print("YOU WIN")
                                running = False
                                break
                    else:
                        chances -= 1
                        if chances == 0:
                            ending_word = "YOU LOSE"
                            print("YOU LOSE")
                            running = False
                            break
                else:
                    print("You clicked outside")

    draw_letters()
    draw_hangman(chances)
    draw_word(word, guessed)

ending_page = True
# TODO: design and implement an ending page
screen.fill(WHITE)
img = my_font.render(ending_word, True, BLACK)
textRect = img.get_rect()
textRect.center = (500, 500)
screen.blit(img, textRect)
pygame.display.update()

while ending_page:
    for event in pygame.event.get():
        if event.type == QUIT:
            ending_page = False

pygame.quit()

