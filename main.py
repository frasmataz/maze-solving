#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy

maze = []

def openMaze(filename):
    thisfile = open(filename, "r")
    newMaze = []
    for line in thisfile:
        row = []
        for char in line:
            if char == '0':
                row.append(0)
            elif char == '1':
                row.append(1)
        newMaze.append(row)
    return newMaze

def printMaze(trail):
    for x in range(0, maze.shape[0]):
        for y in range(0, maze.shape[1]):
            try:    #If location appears in trail, draw arrow
                if trail[(x,y)] == "down":
                    print ('↓', end='', sep='')
                elif trail[(x,y)] == "left":
                    print ('←', end='', sep='')
                elif trail[(x,y)] == "up":
                    print ('↑', end='', sep='')
                elif trail[(x,y)] == "right":
                    print ('→', end='', sep='')
            except: #Else, draw maze tile
                if maze[x][y] == 0:
                    print (' ', end='', sep='')
                elif maze[x][y] == 1:
                    print ('█', end='', sep='')
        print('')

def clockwise(direction):
    if direction == "up":
        return "right"
    elif direction == "right":
        return "down"
    elif direction == "down":
        return "left"
    elif direction == "left":
        return "up"

def antiClockwise(direction):
    if direction == "up":
        return "left"
    elif direction == "left":
        return "down"
    elif direction == "down":
        return "right"
    elif direction == "right":
        return "up"

def getNextPos(pos, direction):
    if direction == "up":
        return [pos[0]-1,pos[1]]
    elif direction == "left":
        return [pos[0],pos[1]-1]
    elif direction == "down":
        return [pos[0]+1,pos[1]]
    elif direction == "right":
        return [pos[0],pos[1]+1]

def getNextPosVal(pos, direction):
    nextPos = getNextPos(pos, direction)
    return maze[nextPos[0],nextPos[1]]

maze = numpy.array(openMaze("hardmaze"))
printMaze(None)

entrance = None
exit = None

#Find entrance
pos = 0
for x in maze[0,:]:
    if x == 0:
        entrance = [0,pos]
    pos+=1

print ("Entrance:\t" + str(entrance))

#Find exit
pos = 0
for x in maze[maze.shape[0]-1,:]:
    if x == 0:
        exit = [maze.shape[0]-1,pos]
    pos+=1

print ("Exit:\t\t" + str(exit))

print ("Solving...")

#Set up status variables
found = False       #Am I at the exit?
pos = entrance      #Start at the entrance
direction = "down"  #Start facing down
trail = {}          #Clear the trail
steps = 0           #Clear step counter

#Hug the wall approach -- The 'robot' always hugs the wall to it's left.
while pos != exit:                                          #While not at exit
    trail[(pos[0],pos[1])] = direction                      #Add current position and direction to trail
    steps += 1                                              #Count step

    if getNextPosVal(pos,antiClockwise(direction)) == 0:    #Try to turn anti-clockwise and go
        pos = getNextPos(pos,antiClockwise(direction))
        direction = antiClockwise(direction)
    elif getNextPosVal(pos,direction) == 0:                 #Try to go forward
        pos = getNextPos(pos,direction)
    else:                                                   #Try to turn clockwise
        direction=clockwise(direction)

#Finished!
trail[(pos[0],pos[1])] = direction      #Add last step to trail
print("Solved!  Found the exit in " + str(steps) + " steps!")

printMaze(trail)
