"""
 Snake Game template, using classes.
 
 Derived from:
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249

import pygame
import random

 
# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

 
# Screen size
height = 800
width = 600

 
# Margin between each segment
segment_margin = 3
 
# Set the width and height of each snake segment
segment_width = min(height, width) / 40 - segment_margin
segment_height = min(height, width) / 40 - segment_margin
 
# Set initial speed
x_change = segment_width + segment_margin
y_change = 0
position=[ i for i in range(0, 600, 15)]

class Snake():
    """ Class to represent one snake. """

    # Constructor
    def __init__(self):
        #Initialize food
        self.food = Food()
        self.Sfoodlists = self.food.foodlists
        self.Sfoodlist = self.food.foodlist
        #Initialize obstavle
        self.obstavle = Obstacle()
        self.Sobstavleslist = self.obstavle.obstacleslist
        self.Sobstavlelist = self.obstavle.obstaclelist

        self.segments = []
        self.spriteslist = pygame.sprite.Group()
        for i in range(15):
            x = (segment_width + segment_margin) * 30 - (segment_width + segment_margin) * i
            y = (segment_height + segment_margin) * 2
            segment = Segment(x, y)
            self.segments.append(segment)
            self.spriteslist.add(segment)

        #Initialization of hostile snakes
        self.opposition = []
        self.oppositionlist = pygame.sprite.Group()
        for i in range(10):
            x = (segment_width + segment_margin) * 25 - (segment_width + segment_margin) * i
            y = (segment_height + segment_margin) * 30
            oppose = OpposeSegment(x, y)
            self.opposition.append(oppose)
            self.oppositionlist.add(oppose)
    #Moving direction of AI
    def AI_move(self):
        # Figure out where new segment will be
        global x_oppose_change, y_oppose_change
        direction = random.randint(0,3)

        #Judging whether to collide with obstacles
        oppose_obstacles_hit_list = pygame.sprite.spritecollide(self.opposition[0], self.Sobstavlelist,False)
        if oppose_obstacles_hit_list != []:
            if (self.opposition [0].rect.x-oppose_obstacles_hit_list[0].rect.x > 0):
                direction = random.choice([2,3])
            elif (self.opposition [0].rect.x-oppose_obstacles_hit_list[0].rect.x < 0):
                direction = random.choice([2,3])
            else:
                direction = random.choice([0,1])

        #Determine the player`s snake location and movement of the computer snake.
        if (self.segments[0].rect.x-self.opposition [0].rect.x >= 0) and (self.segments[0].rect.y-self.opposition [0].rect.y >= 0):
            direction = random.choice([0,3])
        if (self.segments[0].rect.x-self.opposition [0].rect.x > 0) and (self.segments[0].rect.y-self.opposition [0].rect.y < 0):
            direction = random.choice([0,2])
        if (self.segments[0].rect.x-self.opposition [0].rect.x < 0) and (self.segments[0].rect.y-self.opposition [0].rect.y > 0):
            direction = random.choice([1,3])
        if (self.segments[0].rect.x-self.opposition [0].rect.x <= 0) and (self.segments[0].rect.y-self.opposition [0].rect.y <= 0):
            direction = random.choice([1,2])

        #Judging whether a snake is on the edge
        if (self.opposition [0].rect.x < 0) or (self.opposition [0].rect.x > 600):
            direction = random.choice([2,3])
        if (self.opposition [0].rect.y < 0) or (self.opposition [0].rect.y > 600):
            direction = random.choice([0,1])
        if (self.opposition [0].rect.x < 0) and (self.opposition [0].rect.y < 0):
            direction = random.choice([0,3])
        if (self.opposition [0].rect.x < 0) and (self.opposition [0].rect.y > 600):
            direction = random.choice([0,2])
        if (self.opposition [0].rect.x > width - segment_width) and (self.opposition [0].rect.y < 0):
            direction = random.choice([1,3])
        if (self.opposition [0].rect.x > width - segment_width) and (self.opposition [0].rect.y > 600):
            direction = random.choice([1,2])

        #The Moving Direction of Snake
        if direction == 0:
            x_oppose_change,y_oppose_change = self.moveRight()
        if direction == 1:
            x_oppose_change,y_oppose_change = self.moveLeft()
        if direction == 2:
            x_oppose_change,y_oppose_change = self.moveUp()
        if direction == 3:
            x_oppose_change,y_oppose_change = self.moveDown()

        x = self.opposition[0].rect.x + x_oppose_change
        y = self.opposition[0].rect.y + y_oppose_change

        # Don't move off the screen
        # At the moment a potential move off the screen means nothing happens, but it should end the game
        # if 0 <= x < width - segment_width and 0 <= y <=height - segment_height:

            # Insert new segment into the list
        oppose = OpposeSegment(x, y)
        self.opposition.insert(0, oppose)
        self.oppositionlist.add(oppose)
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
        oppose_old_segment = self.opposition.pop()
        self.oppositionlist.remove(oppose_old_segment)

    def moveRight(self):
        return (segment_width + segment_margin),0
    def moveLeft(self):
        return (segment_width + segment_margin)*-1,0
    def moveUp(self):
        return 0,(segment_width + segment_margin)*-1
    def moveDown(self):
        return 0,(segment_width + segment_margin)

    def move(self):
        global old_segment
        # Figure out where new segment will be
        x = self.segments[0].rect.x + x_change
        y = self.segments[0].rect.y + y_change
        
        # Don't move off the screen
        # At the moment a potential move off the screen means nothing happens, but it should end the game
        # if 0 <= x < width - segment_width and 0 <= y <=height - segment_height:
        
        # Insert new segment into the list
        segment = Segment(x, y)
        self.segments.insert(0, segment)
        self.spriteslist.add(segment)
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
        old_segment = self.segments.pop()
        self.spriteslist.remove(old_segment)
        self.eat()
        self.coll()

    def eat(self):
        #player`s snake eat food
        global score
        hit_list = pygame.sprite.spritecollide(self.segments[0], self.Sfoodlist,True)
        if hit_list  != []:
            self.Sfoodlists.remove(hit_list[0])
            score +=10
            self.replenish()
            self.grow()

    def grow(self):
        #player`s snake grow
        global old_segment
        self.spriteslist.add(old_segment)
        self.segments.insert(-1, old_segment)

    def replenish(self):
        #When the player's snake eats the food, replenish the food.
        self.food = Food()
        Sfoodlist = self.food.foodlist
        self.Sfoodlist = Sfoodlist
        Sfoodlists = self.food.foodlists
        self.Sfoodlists = Sfoodlists
        for seg in self.segments:
            hitlist = pygame.sprite.spritecollide(seg, self.Sfoodlist, False)
            if hitlist != []:
                self.replenish()

    def coll(self):
        global score,game_ended
        #Determine whether the player's snake is out of bounds.
        if (self.segments[0].rect.x < 0) or (self.segments[0].rect.x > width - segment_width) or (self.segments[0].rect.y < 0) or (self.segments[0].rect.y > 600):
            game_ended = True

        #Determine whether the player's snake collided with obstacles.
        obstacles_hit_list = pygame.sprite.spritecollide(self.segments[0], self.Sobstavlelist,True)
        if obstacles_hit_list != []:
            game_ended = True
        #Judging whether a player's snake collides with itself
        for i in self.segments[1:]:
            if (self.segments[0].rect.x == i.rect.x) and (self.segments[0].rect.y == i.rect.y):
                game_ended = True
        #Determine whether a player's snake collides with an enemy snake
        oppose_hit_list = pygame.sprite.spritecollide(self.segments[0], self.oppositionlist ,True)
        if oppose_hit_list !=[]:
            game_ended = True

class Obstacle():
    #Obstacle formation
    def __init__(self):
        self.obstacleslist = []
        self.obstaclelist = pygame.sprite.Group()# for f in range(50):
        o = 0
        while o != 10:
            o += 1
            x = random.choice([i for i in range(0, 600, 15)])
            y = random.choice([i for i in range(0, 600, 15)])
            # print(x,y)
            if (x==255 or x==270 or x==285 or x==300 or x==315 or x==330 or x==345 or x==360 or x==375 or x==390 or x==405 or x==420 or x==450 or x==465) and (y == 30):
                o -= 1
                continue
            Obstacleitem = Obstacles(x, y)
            self.obstacleslist.append(Obstacleitem)
            self.obstaclelist.add(Obstacleitem)

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, ox, oy):
        # Call the parent's constructor
        super().__init__()
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(GREEN)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = ox
        self.rect.y = oy

class OpposeSegment(pygame.sprite.Sprite):
    """ Class to represent one segment of a snake. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill((10,50,255))

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of a snake. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
 
        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Food():
    #food formation
    def __init__(self):
        self.foodlists = []
        self.foodlist = pygame.sprite.Group()

        # for f in range(50):
        x = random.choice([i for i in range(0, 600, 15)])
        y = random.choice([i for i in range(0, 600, 15)])
        fooditem = Food_item(x, y)
        self.foodlists.append(fooditem)
        self.foodlist.add(fooditem)

class Food_item(pygame.sprite.Sprite):
    def __init__(self, fx, fy):
        # Call the parent's constructor
        super().__init__()
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(RED)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = fx
        self.rect.y = fy

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface() #req'd when function moved into MyLibrary
    screen.blit(imgText, (x,y))

 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create a 600x600 sized screen
screen = pygame.display.set_mode([width, height])
 
# Set the title of the window
pygame.display.set_caption('Snake Game')
 
# Create an initial snake
my_snake = Snake()


clock = pygame.time.Clock()
done = False
game_ended = False
score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
        # Set the direction based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)

    # move snake one step
    my_snake.AI_move()
    my_snake.move()

    
    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)
    my_snake.spriteslist.draw(screen)
    my_snake.oppositionlist.draw(screen)
    my_snake.Sfoodlist.draw(screen)
    my_snake.Sobstavlelist.draw(screen)

    pygame.draw.rect(screen,(100,100,100),[0, 600, 600, 200])
    # create a Font object from the system fonts create a Font object from the system fonts
    font = pygame.font.SysFont("comicsansms", 48)
    # create an image (Surface) of the text create an image (Surface) of the text
    text = font.render('Score = ' + str(score), True, (255, 0, 0))
    # # get the bounding box for the image get the bounding box for the image
    textrect = text.get_rect()
    # set the position set the position
    textrect.centerx = 200
    textrect.centery = 700
    # blit (copy) the image onto the screen blit (copy) the image onto the screen
    screen.blit(text, textrect)

    if game_ended:
        screen2 = pygame.display.set_mode([width, height])
        screen2.fill(BLACK)
        print_text(font, 100, 550, "G A M E   O V E R")
    
    # Flip screen
    pygame.display.flip()
 
    # Pause
    clock.tick(5)

pygame.quit()
