import pygame
import sys
import os
from pygame import freetype
import webbrowser
squares = []
walls = []
running = True



class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.a = [x1, y1]
        self.b = [x2, y2]

    def display(self, screen):
        #pygame.draw.rect(screen, (255, 0, 0), (self.a[0], self.a[1], self.b[0] - self.a[0], self.b[1] - self.a[1]))
        pygame.draw.line(screen, (255, 255, 255), self.a, self.b, 2)



class Square:
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        walls.append(Wall(self.x, self.y, self.x + self.width, self.y))
        walls.append(Wall(self.x, self.y, self.x, self.y + self.height))
        walls.append(Wall(self.x + self.width, self.y + self.height, self.x, self.y + self.height))
        walls.append(Wall(self.x + self.width, self.y, self.x + self.width, self.y + self.height))


    def draw(self, screen):
        '''


        '''
        pygame.draw.rect(screen, pygame.Color("red"), (self.x, self.y, self.width, self.height))





#Pygame setup
pygame.init()
#Pygame display setup
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Life Map Editor")
pygame.display.set_icon(pygame.image.load("6718080.png"))
#Open the map file if not already opened:
if (len(sys.argv) - 1) != 0:
    if os.path.isfile(str(sys.argv[1])):
        webbrowser.open(str(sys.argv[1]))
    else:
        print("File not found. Defaulting to Map1.txt")
        webbrowser.open("Map1.txt")
else:
    webbrowser.open("Map1.txt")
#Run Loop
while running:
    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
    #Flush out old squares and walls
    win.fill(pygame.Color("black"))
    squares.clear()
    walls.clear()
    
    
    #Get new data from Map file (or running arguments)
    if (len(sys.argv) - 1) != 0:
        RawMap = open(str(sys.argv[1]))
    else:
        RawMap = open("Map1.txt","r")
    RawMap = RawMap.read().splitlines()
    finalMap = []   
    #Parse new data
    for i in RawMap:
        tempTab = i.split(",")
        newTab  = []
        for i in tempTab:
            if i != '':
                newTab.append(int(i))
        finalMap.append(newTab)
    #Lastly, reload squares
    for i in finalMap:
        try:
            squares.append(Square(i[0],i[1],i[2],i[3]))
        except:
            None
    for square in squares:
        square.draw(win)
    for wall in walls:
        wall.display(win)
    pygame.time.Clock().tick(30)
    pygame.display.update()