

import pygame
import random
import math

#----------------------#
# Declaring variables  #
#----------------------#
WIDTH, HEIGHT = 600, 600
ROWS, COLUMNS = 25, 25
BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CAPTION = "SnakeGame"
FPS = 20
clock = pygame.time.Clock()

#setting the dimensions of the game screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)

def main():

    #defining position of snake
    block_length = WIDTH // ROWS
    block_height = HEIGHT // ROWS
    
    x = block_length * (COLUMNS // 2)
    y = block_height * (ROWS // 2)

    x_change = 0
    y_change = 0

    #defining position of snacks to be created
    x_snack = random.randrange(0, COLUMNS) * block_length
    y_snack = random.randrange(0, ROWS) * block_height
    
    run = True
    while run:

        #Creating a black background with white grids.
        SCREEN.fill(BLACK)
        drawGrid(SCREEN)

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_length
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_length
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_height
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_height
                    x_change = 0


        x += x_change
        y += y_change

        #Creating the snake
        pygame.draw.rect(SCREEN, BLUE, [x, y, block_length, block_height])

        #creating the snack
        pygame.draw.ellipse(SCREEN, BLUE, [x_snack, y_snack, block_length, block_height])

        pygame.display.update()
        clock.tick(FPS)

        # game ends when user hits border
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            run = False

        
        
    pygame.quit()
    
def drawGrid(surface):
    #determing the length of each box on x-axis
    xgridSpace = WIDTH // COLUMNS
    #and y-axis
    ygridSpace = HEIGHT // ROWS

    x, y = 0, 0

    #draw columns
    for i in range(COLUMNS-1):

        x += xgridSpace
        pygame.draw.line(surface, WHITE, (x, 0), (x, HEIGHT))

    
    for i in range(ROWS-1):

        y += ygridSpace
        pygame.draw.line(surface, WHITE, (0, y), (WIDTH, y))

    
if __name__ == "__main__":
    main()

