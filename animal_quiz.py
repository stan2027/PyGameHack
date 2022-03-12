import pygame
from pygame.locals import *
import os
import random

RED = (255, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)

pygame.init()
w, h = 1000, 1000
screen = pygame.display.set_mode((w, h))
running = True

# load assets
asset_dir = "assets/images/"
all_image_filenames = list(os.listdir('assets/images/'))
all_images = [pygame.image.load(asset_dir+filename) for filename in all_image_filenames]
my_font = pygame.font.SysFont('ubuntumono.ttf', 50)

def process_name(filename): # convert filename into human readable animal name
    return " ".join(filename.split('_'))
    

def setup_quiz():
    # pick a random image
    choice = random.randint(0, len(all_images)-1)
    img = all_images[choice]
    img =  pygame.transform.rotozoom(img, 0, 0.7)
    img.convert()
    
    # pick animal names
    right_name = process_name(all_image_filenames[choice])
    wrong_name = process_name(all_image_filenames[(choice+1)%len(all_images)]) #TODO: randomize the wrong name pick
    right_name_img = my_font.render(right_name, True, GRAY)
    wrong_name_img = my_font.render(wrong_name, True, GRAY)
    return img, right_name_img, wrong_name_img

def get_rect(_img, x, y):
    _rect = _img.get_rect()
    _rect.center = x, y
    return _rect


moving = False
img, right_name_img, wrong_name_img = setup_quiz()
rect = get_rect(img, w//2, h//2)
right_name_rect = get_rect(right_name_img, w//2, h//6)
wrong_name_rect = get_rect(wrong_name_img, w//2, 5*h//6)

right_img = my_font.render("RIGHT", True, GRAY)
right_rect = get_rect(right_img, w//2, h//2)
next_img = my_font.render("NEXT", True, GRAY)
next_rect = get_rect(next_img, 9*w/10, 9*h/10)

screen.fill(WHITE)
screen.blit(img, rect)
screen.blit(next_img, next_rect)
screen.blit(right_name_img, right_name_rect)
screen.blit(wrong_name_img, wrong_name_rect)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN: # if clicking down on the image
            if rect.collidepoint(event.pos):
                moving = True
            elif next_rect.collidepoint(event.pos): # next stage!
                img, right_name_img, wrong_name_img = setup_quiz()
                rect = get_rect(img, w//2, h//2)
                right_name_rect = get_rect(right_name_img, w//2, h//6)
                wrong_name_rect = get_rect(wrong_name_img, w//2, 5*h//6)
                screen.fill(WHITE)
                screen.blit(img, rect)
                screen.blit(next_img, next_rect)
                screen.blit(right_name_img, right_name_rect)
                screen.blit(wrong_name_img, wrong_name_rect)
                pygame.display.update()

        elif event.type == MOUSEBUTTONUP:
            moving = False
            if rect.colliderect(right_name_rect):
                screen.blit(right_img, right_rect)
                pygame.display.update()
            # TODO: if dropping on the wrong name, show "WRONG" in the centre

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
            screen.fill(WHITE)
            screen.blit(img, rect)
            screen.blit(next_img, next_rect)
            screen.blit(right_name_img, right_name_rect)
            screen.blit(wrong_name_img, wrong_name_rect)
            pygame.display.update()

pygame.quit()