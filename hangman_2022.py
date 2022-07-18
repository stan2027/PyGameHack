import random
import pygame
from pygame.locals import *

vocab = open("vocab.txt", 'r')
content = vocab.readlines()
words = []
for w in content:
    words.append(w[0:len(w)-1])

target = random.choice(words).upper()
print("The target is: "+str(target))

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)
pygame.display.update()
pygame.display.set_caption("Hangman 2022")

def draw_hangman(chances):
    pygame.draw.line(screen, BLACK, (40, 50), (240, 50), width=5)
    pygame.draw.line(screen, BLACK, (40, 50), (40, 350), width=5)
    pygame.draw.line(screen, BLACK, (10, 350), (150, 350), width=5)
    pygame.draw.line(screen, BLACK, (140, 50), (140, 100), width=3)
    if chances > 0:
        pygame.draw.circle(screen, BLACK, (140, 130), 30, width=4)
    if chances > 1:
        pygame.draw.line(screen, BLACK, (140, 160), (140, 240), width=4)
    if chances > 2:
        pygame.draw.line(screen, BLACK, (140, 160), (100, 200), width=4)
    if chances > 3:
        pygame.draw.line(screen, BLACK, (140, 160), (180, 200), width=4)
    if chances > 4:
        pygame.draw.line(screen, BLACK, (140, 240), (100, 280), width=4)
    if chances > 5:
        pygame.draw.line(screen, BLACK, (140, 240), (180, 280), width=4)


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
game_font = pygame.font.SysFont('ubuntumono.ttf', 25)
guessed = {}
letter_rects = {}

for i in range(len(target)):
    guessed[i] = False

def draw_letters():
    for i in range(len(LETTERS)):
        text = game_font.render(LETTERS[i], True, BLACK)
        textRect = text.get_rect()
        if i < 13:
            textRect.center = (50+i*30, 400)
        else:
            textRect.center = (50+(i-13)*30, 450)
        letter_rects[LETTERS[i]] = textRect
        screen.blit(text, textRect)

def draw_word():
    for i in range(len(target)):
        if i < 6:
            start_x = 250+40*i
            end_x = start_x+30
            if guessed[i]:
                text = game_font.render(target[i], True, BLACK)
                textRect = text.get_rect()
                textRect.center = (start_x+15, 185)
                screen.blit(text, textRect)
            pygame.draw.line(screen, BLACK, (start_x, 200), (end_x, 200), width=3)
        else:
            start_x = 250+40*(i-6)
            end_x = start_x+30
            if guessed[i]:
                text = game_font.render(target[i], True, BLACK)
                textRect = text.get_rect()
                textRect.center = (start_x+15, 215)
                screen.blit(text, textRect)
            pygame.draw.line(screen, BLACK, (start_x, 230), (end_x, 230), width=3)


def verify_guess(letter): # if guess correct, return True, otherwise, return False
    if letter not in target:
        return False
    for i in range(len(target)):
        if target[i] == letter:
            guessed[i] = True
            print("Setting "+str(i)+" entry in guessed to be true")
            print(guessed)
    return True
        
CHANCES = 6
draw_hangman(CHANCES)
draw_letters()
draw_word()
pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            for i in range(len(LETTERS)):
                letter = LETTERS[i]
                if letter_rects[letter].collidepoint(event.pos):
                    player_guess = verify_guess(letter)
                    if not player_guess:
                        CHANCES -= 1
                        if CHANCES == 0:
                            print("You've lost, GG!")
                            running = False
                    elif player_guess and False not in guessed.values(): # Player guessed everything
                        print("Congratulatons, You've won!")
                        running = False
    screen.fill(WHITE)
    draw_hangman(CHANCES)
    draw_letters()
    draw_word()
    pygame.display.update()





            


pygame.quit()
