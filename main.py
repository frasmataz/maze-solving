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

def printMaze(direction):
    for y in maze:
        for x in y:
            if x == 3:
                if direction == "down":
                    print ('↓', end='', sep='')
                elif direction == "left":
                    print ('←', end='', sep='')
                elif direction == "up":
                    print ('↑', end='', sep='')
                elif direction == "right":
                    print ('→', end='', sep='')
            if x == 1:
                print ('█', end='', sep='')
            elif x == 0:
                print (' ', end='', sep='')
            elif x == 2:
                print ('+', end='', sep='')
        print('')

maze = numpy.array(openMaze("maze"))
printMaze(None)

entrance = None
exit = None

#find entrance
pos = 0
for x in maze[0,:]:
    if x == 0:
        entrance = [0,pos]
    pos+=1

print ("Entrance:\t" + str(entrance))

#find exit
pos = 0
for x in maze[maze.shape[0]-1,:]:
    if x == 0:
        exit = [maze.shape[0]-1,pos]
    pos+=1

print ("Exit:\t\t" + str(exit))

#hug the wall
found = False
pos = entrance
direction = "down"
trail = []

while found == False:
    trail.append(pos)
    if pos == exit:
        found = True
    else:
        #maze[pos[0],pos[1]] = 3
        #printMaze(direction)
        #print
        #maze[pos[0],pos[1]] = 0
        if direction == "down":
            if maze[pos[0],pos[1]+1] == 0:
                pos = [pos[0],pos[1]+1]
                direction = "right"
            elif maze[pos[0]+1,pos[1]] == 0:
                pos = [pos[0]+1,pos[1]]
            else:
                direction = "left"
        elif direction == "left":
            if maze[pos[0]+1,pos[1]] == 0:
                pos = [pos[0]+1,pos[1]]
                direction = "down"
            elif maze[pos[0],pos[1]-1] == 0:
                pos = [pos[0],pos[1]-1]
            else:
                direction = "up"
        elif direction == "up":
            if maze[pos[0],pos[1]-1] == 0:
                pos = [pos[0],pos[1]-1]
                direction = "left"
            elif maze[pos[0]-1,pos[1]] == 0:
                pos = [pos[0]-1,pos[1]]
            else:
                direction = "right"
        elif direction == "right":
            if maze[pos[0]-1,pos[1]] == 0:
                pos = [pos[0]-1,pos[1]]
                direction = "up"
            elif maze[pos[0],pos[1]+1] == 0:
                pos = [pos[0],pos[1]+1]
            else:
                direction = "down"

for t in trail:
    maze[t[0],t[1]] = 2

printMaze(None)
