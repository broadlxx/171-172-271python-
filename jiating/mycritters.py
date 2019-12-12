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
    def __init__(self):
        self.s = random.randint(1,3)
        self.colour = random.choice(color_sheme)
        x = random.randrange(50,950)
        y = random.randrange(600,950)
        self.xcoord = x
        self.ycoord = y


    def draw_critter(self, screen):
        size=self.s
        color=self.colour
        x = self.xcoord
        y = self.ycoord
        pygame.draw.ellipse(screen,red, [x, y, 40*size, 45*size])
        pygame.draw.ellipse(screen,red, [x, y+40*size, 40*size, 45*size])
        pygame.draw.ellipse(screen,red, [x, y+80*size, 40*size,45*size])
        pygame.draw.ellipse(screen,black, [x+6*size, y+10*size, 10*size, 15*size])
        pygame.draw.ellipse(screen,black, [x+24*size, y+10*size, 10*size, 15*size])
        pygame.draw.line(screen,black, (x+11, y+1), (x+9, y-10), 3)
        pygame.draw.line(screen,black, (x+25, y+1), (x+26, y-10), 3)



class Butterfly:
    def __init__(self):
        m = random.randrange(50,950)
        n = random.randrange(50,500)
        self.mcoord = m
        self.ncoord = n


    def draw_critter(self,screen):
        m = self.mcoord
        n = self.ncoord
        pygame.draw.ellipse(screen,red, [m, n, 30, 150])
        pygame.draw.ellipse(screen,yellow,[m+28,n+15,70,120 ])
        pygame.draw.ellipse(screen,yellow,[m-68,n+15,70,120 ])
        pygame.draw.ellipse(screen,black, [m+8, n+10, 7.5, 11.25])
        pygame.draw.ellipse(screen,black, [m+16, n+10, 7.5, 11.25])
        pygame.draw.line(screen,black, (m+11, n+1), (m+9, n-10), 2)
        pygame.draw.line(screen,black, (m+18, n+1), (m+19, n-10), 2)
            
            
