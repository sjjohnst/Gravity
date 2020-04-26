import pygame as py
import time
from vars import *

#GRAVITY CLASSES
class Box:

    def __init__(self, pos1, pos2, surf, vo=0):
        self.x = pos1[0]
        self.y = pos1[1]
        self.w = pos2[0] - pos1[0]
        self.h = pos2[1] - pos1[1]
        self.s_time = time.time()
        self.surf = surf
        self.vo = vo

    def display(self, current_time):
        py.draw.rect(self.surf, BLACK, (self.x, self.y, self.w, self.h))
        self.y += self.velocity(current_time)

    def velocity(self, current_time):
        t = current_time - self.s_time
        return G_Acceleration * t + self.vo
