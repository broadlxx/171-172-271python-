import pygame
import random

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
yellow   = ( 255,   255, 0)
purple   = ( 255,   0, 255)
brown     = ( 125, 100, 100)

color_sheme=[black,white,green,red,yellow,purple,brown]



class Caterpillar:

    black    = (   0,   0,   0)
    white    = ( 255, 255, 255)
    green    = (   0, 255,   0)
    red      = ( 255,   0,   0)
    yellow   = ( 255,   255, 0)
    purple   = ( 255,   0, 255)
    brown     = ( 125, 100, 100)

    color_sheme=[black,white,yellow,red,purple]

    def __init__(self):
        self.s = random.randint(1,3)
        x = random.randrange(50,950)
        y = random.randrange(600,950)
        self.xcoord = x
        self.ycoord = y

      
    def draw_critter(self, screen):
        size=self.s
        x = self.xcoord
        y = self.ycoord
        pygame.draw.ellipse(screen,self.color_sheme[3], [x, y, 45*size, 40*size])
        pygame.draw.ellipse(screen,self.color_sheme[3], [x+40*size, y, 45*size, 40*size])
        pygame.draw.ellipse(screen,self.color_sheme[3], [x+80*size, y, 45*size, 40*size])
        pygame.draw.ellipse(screen,self.color_sheme[0], [x+10*size, y+6*size, 15*size, 10*size])
        pygame.draw.ellipse(screen,self.color_sheme[0], [x+10*size, y+24*size, 15*size, 10*size])
        pygame.draw.line(screen,self.color_sheme[0], (x+1, y+11), (x-10, y+9), 3)
        pygame.draw.line(screen,self.color_sheme[0], (x+1, y+25), (x-10, y+26), 3)

    def change_color(self):
        color = self.color_sheme[3]
        a = random.randint(0,4)
        while True:
            if a == 3:
                a = random.randint(0,4)
            else:
                self.color_sheme[3] = self.color_sheme[a]
                break
        self.color_sheme[a]=color


class Butterfly:

    black    = (   0,   0,   0)
    white    = ( 255, 255, 255)
    green    = (   0, 255,   0)
    red      = ( 255,   0,   0)
    yellow   = ( 255,   255, 0)
    purple   = ( 255,   0, 255)
    brown     = ( 125, 100, 100)

    color_sheme=[black,white,green,red,yellow,purple,brown]
    def __init__(self):
        m = random.randrange(50,950)
        n = random.randrange(50,500)
        self.mcoord = m
        self.ncoord = n


    def draw_critter(self,screen):
        m = self.mcoord
        n = self.ncoord
        pygame.draw.ellipse(screen,self.color_sheme[3], [m, n, 30, 150])
        pygame.draw.ellipse(screen,self.color_sheme[4],[m+28,n+15,70,120 ])
        pygame.draw.ellipse(screen,self.color_sheme[4],[m-68,n+15,70,120 ])
        pygame.draw.ellipse(screen,self.color_sheme[0], [m+8, n+10, 7.5, 11.25])
        pygame.draw.ellipse(screen,self.color_sheme[0], [m+16, n+10, 7.5, 11.25])
        pygame.draw.line(screen,self.color_sheme[0], (m+11, n+1), (m+9, n-10), 2)
        pygame.draw.line(screen,self.color_sheme[0], (m+18, n+1), (m+19, n-10), 2)

    def change_color(self):
        color = self.color_sheme[3]
        a = random.randint(0,6)
        while True:
            if a == 3:
                a = random.randint(0,6)
            else:
                self.color_sheme[3] = self.color_sheme[a]
                break
        self.color_sheme[a] = color





            
