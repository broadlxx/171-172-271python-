"""
 Animating multiple objects using a list.
 based on Sample Python/Pygame Programs
 Simpson College Computer Science
 
"""

# Import libraries 'pygame' and 'random'
import pygame
import random

def recolour_snowflake(s):
    s[1]=random.choice(color)
    return s
def keep_snowflake(d):
    delete_number=15
    choose=random.randrange(0,30)
    if choose != delete_number:
        return d


# Initialize the game engine
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED   = [255, 0, 0]

color=[WHITE,GREEN,RED]

# Set the height and width of the screen
SIZE = [400, 400]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")

# Create an empty list
snow_list = []

# Loop 100 times and add a snow flake in a random x,y position
for i in range(100):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    c = random.choice(color)
    snow_list.append([[x, y],c])

clock = pygame.time.Clock()
step=0
# Loop until the user clicks the close button.
done = False
while snow_list != []:

    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    step = step+1
    if step == 10:
        step=0
        snow_list = list(map(recolour_snowflake, snow_list))

    snow_list = list(filter(keep_snowflake, snow_list))


    # Process each snow flake in the list
    for i in range(len(snow_list)):

        # Draw the snow flake
        pygame.draw.circle(screen, snow_list[i][1], snow_list[i][0], 2)

        # Move the snow flake down one pixel
        snow_list[i][0][1] += random.randrange(1,4)


        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][0][1] > 400:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][0][1] = y
            # Give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0][0] = x

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)

# If you forget this line, the program will 'hang' on exit.
pygame.quit()
