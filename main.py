import pygame as py
import time, sys
from classes import *
from vars import *

py.init()
window = py.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = py.time.Clock()

def box_border(pos1, pos2, color):
    x = pos1[0]
    y = pos1[1]
    w = pos2[0] - x
    h = pos2[1] - y
    py.draw.rect(window, color, (x,y,w,h), 1)

def new_object():
    x = int(input("X position: "))
    y = int(input("Y position: "))
    w = int(input("Width (m): "))
    h = int(input("Height (m): "))
    if x < 0 or y < 0 or x > DISPLAY_WIDTH or y > DISPLAY_HEIGHT:
        print("position out of bound")
    pos1 = (x,y)
    pos2 = (x+w,y+h)
    vo = int(input("initial velocity (m/s): "))
    item = Box(pos1, pos2, window, vo)
    return item

def main():

    items = []
    drawing = False
    
    while True:

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos1 = py.mouse.get_pos()
                    drawing = True

            if event.type == py.MOUSEBUTTONUP:
                pos2 = py.mouse.get_pos()
                drawing = False
                box = Box(pos1, pos2, window)
                items.append(box)

            if event.type == py.KEYDOWN:

                if event.key == py.K_RETURN:
                    items.append(new_object())
            
        window.fill(WHITE)

        if drawing == True:
            pos2 = py.mouse.get_pos()
            box_border(pos1, pos2, BLUE)
        
        for item in items:
            if item.y > DISPLAY_HEIGHT + item.h:
                items.remove(item)
                del item
                continue
            item.display(time.time())

        py.display.update()
        clock.tick(FPS)
        
main()
