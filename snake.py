import pygame
import random
 
BLACK = (0, 0, 0) #! What is RGB? 
WHITE = (255, 255, 255)
YELLOW = (255, 196, 0)
LIGHT_YELLOW = (255, 220, 104)

# Width and Heigh of a block
block_width = 15
block_height = 15
# Margin between each block
block_margin = 3
# Set initial movement
x_change = 0
y_change = block_width + block_margin
# Snake initial length
snake_length = 10
# Initial food count
food_count = 7
 
 #!What is a class? When should we use class? Give an example.
class Block(pygame.sprite.Sprite): #! What is a sprite?
    """ Class to represent one block of the snake. """
    def __init__(self, x, y, color=WHITE): #! What is a constructor?
        super().__init__()
        # Draw a white block 
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
 
        # Set top left corner to match x, y
        self.rect = self.image.get_rect() #! What does get_rect() return?
        self.rect.x = x
        self.rect.y = y

class Food(Block):
    def __init__(self, x, y, color=YELLOW):
        super().__init__(x, y, color) #! What is this doing?
        self.frame = 0
        self.expired = False

    def update(self):
        self.frame = 1-self.frame #self.frame += 1
        if self.frame == 0:
            self.image.fill(YELLOW)
        else:
            self.image.fill(LIGHT_YELLOW)

pygame.init()

my_font = pygame.font.SysFont('ubuntumono.ttf', 50)
screen = pygame.display.set_mode([900, 900])
 
# Set the title of the window
pygame.display.set_caption('Snake')
 
snake_blocks = pygame.sprite.Group() #! What is a sprite group? Why do we use sprite groups?
food_blocks = pygame.sprite.Group()
 
# Create an initial snake
snake = []
for i in range(snake_length):
    x = 180 - (block_width + block_margin) * i
    y = 180
    block = Block(x, y)
    snake.append(block)
    snake_blocks.add(block)

# Create initial food
# TODO: make food expire and disappear after a while
for i in range(food_count):
    x = (block_width + block_margin)*random.randint(0, 50) #! What does random.randint do? What is this doing? 
    y = (block_width + block_margin)*random.randint(0, 50)
    block = Food(x, y, color=YELLOW)
    food_blocks.add(block)
 
clock = pygame.time.Clock()
done = False
 
# def start_game(): ...
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -(block_width + block_margin)
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (block_width + block_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -(block_height+ block_margin)
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (block_height+ block_margin)

    # Make movement
    tail = snake.pop() #! What does pop do to a list?
    snake_blocks.remove(tail)
 
    x = snake[0].rect.x + x_change
    y = snake[0].rect.y + y_change
    head = Block(x, y)
 
    snake.insert(0, head) #! What does insert(0, xx) do to a list?
    snake_blocks.add(head)

    # Detect if hit wall
    if snake[0].rect.x < 0 or snake[0].rect.x > 900 or snake[0].rect.y < 0 or snake[0].rect.y > 900:
        print("HIT WALL")
        break
    
    # Detect if hitting itself:
    hit = pygame.sprite.spritecollide(snake[0], snake, False)
    if len(hit) > 1: #! Why is this > 1 instead of > 0?
        print("HIT SELF")
        break
    
    # Detect if eating food
    hit = pygame.sprite.spritecollide(snake[0], food_blocks, True)
    if hit:
        x = snake[0].rect.x + x_change
        y = snake[0].rect.y + y_change
        head = Block(x, y)
        snake.insert(0, head)
        snake_blocks.add(head)

        # Add new food
        x = (block_width + block_margin)*random.randint(0, 50) 
        y = (block_width + block_margin)*random.randint(0, 50)
        block = Food(x, y, color=YELLOW)
        food_blocks.add(block)
    
    '''
    # Detect food expiration
    for food in food_blocks:
        if food.expired:
            food_blocks.remove(food)
    '''

    # Draw everything
    screen.fill(BLACK)
    
    food_blocks.update() #! What code does update() execute?
    snake_blocks.draw(screen)
    food_blocks.draw(screen)

    # Update the entire screen instead of calling pygame.display.update() after each drawing
    pygame.display.flip()
 
    # Pause
    clock.tick(5) # for every second, at least 10 frames should pass
    #! If I set clock.tick(20), does the animation get rougher of smoother?

img = my_font.render(f'Score: {len(snake)-snake_length}', True, WHITE)
textRect = img.get_rect()
textRect.center = (450, 450)
screen.blit(img, textRect)
pygame.display.update()

# TODO: press a key to restart
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        '''
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_r:
                start_game()
        '''


pygame.quit()