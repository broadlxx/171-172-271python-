print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249

import pygame
import random

i=0

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
yellow   = ( 255,   255, 0)
purple   = ( 255,   0, 255)

color = [green]

class caterpillar:
    def __init__(self):
        x = random.randrange(0,1000)
        self.face_xcoord = x
        self.face_ycoord = 250
        self.body = segment_queue()
        self.food = food_list()
        self.comsumption = 0
        self.y_new = 0
        t = random.randrange(0,2)
        if t == 0:
            self.travel_direction = 'left'
        else:
            self.travel_direction = 'right'


    def draw_caterpillar(self,screen):
        self.draw_face(screen)
        self.draw_body(screen)
        self.draw_food(screen)


    def draw_face(self, screen):
        y_new = self.y_new
        x = self.face_xcoord
        y = self.face_ycoord
        pygame.draw.ellipse(screen,red,[x, y-y_new, 40, 45+y_new])
        pygame.draw.ellipse(screen,black,[x+6, y+10-y_new, 10, 15])
        pygame.draw.ellipse(screen,black,[x+24, y+10-y_new, 10, 15])
        pygame.draw.line(screen,black, (x+11, y-y_new), (x+9, y-10-y_new), 3)
        pygame.draw.line(screen,black, (x+24, y-y_new), (x+26, y-10-y_new), 3)


    def draw_body(self, screen):
        #traverse the segment queue
        current_node = self.body.head
        while current_node is not None:
            current_node.draw_segment(screen)
            current_node = current_node.next


    def draw_food(self, screen):
        #traverse the segment queue
        current_node = self.food.head
        while current_node is not None:
            current_node.draw_fooditem(screen)
            current_node = current_node.next


    def grow(self):  #This function is to add caterpillar's body.
        global i

        i+=1

        x = self.face_xcoord #facilitate x
        y = self.face_ycoord

        if self.travel_direction== 'left':
            if i==1:
                self.body.addSegment(x-35,y)#Introducing facilitate x, y coordinates into addsegment
            else:
                self.body.addSegment(x-35*i,y)#

        else:
            if i==1:
                self.body.addSegment(x+40,y)
            else:
                self.body.addSegment(x+35*i,y)

        return


    def reverse(self):#The function of this function is to turn the caterpillar to the boundary when the caterpillar reaches its boundary.
        n  =  1
        node  =  self.body.head#When the caterpillar turns, its head turns.
        if self.travel_direction  ==  'right':
            while node != None:
                xcoord  =  node.xcoord
                node  =  node.next
                n += 1
            self.face_xcoord  =  self.face_xcoord + 35*n
            self.travel_direction  =  'left'
        else:
            while node != None:
                xcoord  =  node.xcoord
                node  =  node.next
                n += 1
            self.face_xcoord  =  self.face_xcoord - 35*n
            self.travel_direction  =  'right'

        b  =  None#When the caterpillar turns, it turns to the body.
        t  =  self.body.head
        while t != None:
            a  =  t.next
            t.next  =  b
            b  =  t
            t  =  a
        self.body.last	=	self.body.head
        self.body.head	=	b
        return



    def move_forward(self):# This function can move caterpillars forward.
        if self.travel_direction == 'left':
            self.face_xcoord = self.face_xcoord+2
            current_node = self.body.head
            while current_node is not None:
                current_node.xcoord = current_node.xcoord+2
                current_node = current_node.next

        elif self.travel_direction == 'right':
            self.face_xcoord = self.face_xcoord-2
            current_node = self.body.head
            while current_node is not None:
                current_node.xcoord = current_node.xcoord-2
                current_node = current_node.next

        if self.face_xcoord >=960 or self.face_xcoord <= 1:
            self.reverse()

        food1 = self.food.head
        while food1 != None:
            node = self.food.head
            if abs(self.face_xcoord - food1.xcoord)<5:
                self.comsumption += 1
                if node == food1:
                    self.food.head = self.food.head.next
                while node!= None:
                    if node.next == food1:
                        node.next = node.next.next
                        self.food.length -= 1
                    else:
                        node = node.next

            food1 = food1.next
            self.moult()


    def drop_food(self): # This function can display food.
        x=random.randrange(0, 960)
        y=self.face_ycoord
        self.food.addfood(x,y)
        return

    def moult(self):#This function can make caterpillars change the body.
        if self.comsumption >= 15:
            color[0] = yellow
        if self.comsumption >= 30:
            color[0] = black
            self.y_new = 20
            node2 = self.body.head
            while node2 is not None:
                node2.y_new = 20
                node2 = node2.next
        return



class segment_queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.length == 0

    def addSegment(self, x, y):
        node = body_segment(x,y)
        node.next	=	None
        if self.length == 0:
            self.head = self.last=node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1
        return

class body_segment:  
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y
        self.y_new = 0
        self.next = None

    def draw_segment(self, screen):
        y_new =  self.y_new
        x = self.xcoord
        y = self.ycoord
        pygame.draw.ellipse(screen,color[0],[x, y-y_new, 35, 40+y_new])
        pygame.draw.line(screen,black, (x+8, y+35), (x+8, y+45), 3)
        pygame.draw.line(screen,black, (x+24, y+35), (x+24, y+45), 3)



class food_list:
    def __init__(self):
        self.length = 0
        self.head = None

    def isEmpty(self):
        return self.length == 0

    def addfood(self, x, y):

        node=food_item(x,y)

        node.next	=	None
        if self.length==0:
            self.head=self.last=node
        else:
            last=self.last
            last.next=node
            self.last=node
        self.length=self.length+1

class food_item:
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y
        self.next = None

    def draw_fooditem(self, screen):
        x = self.xcoord
        y = self.ycoord
        pygame.draw.ellipse(screen,yellow,[x, y, 15, 15])


