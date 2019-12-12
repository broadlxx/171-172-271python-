# Import the library of functions called 'pygame'
import sys, pygame
 
# Define a function that will draw a snowman at a certain location
def draw_snowman(screen, x, y, size):
        pygame.draw.ellipse(screen,white,[0.35*size+x,0+y,size/4,size/4])
        pygame.draw.ellipse(screen,white,[0.23*size+x,0.20*size+y,size/2,size/2])
        pygame.draw.ellipse(screen,white,[0+x,0.65*size+y,size,size])

def draw_snowmen(screen, x, y, size=100):
    if size < 20:
        return
    else:
        draw_snowman(screen, x, y, size)
        draw_snowmen(screen, x+size, y, size-10)

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
black = [ 0, 0, 0]
white = [255,255,255]
blue = [ 0, 0,255]
green = [ 0,255, 0]
red = [255, 0, 0]

# Set the height and width of the screen
size=[1150,500]
screen=pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done=False
clock = pygame.time.Clock()


while done==False:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # Clear the screen and set the screen background
    screen.fill(black)

    # Draw Snowman at a particular location
    draw_snowmen(screen,10,200,100)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Tidy up
pygame.quit ()
