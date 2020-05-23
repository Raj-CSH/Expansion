import random
import sys

import pygame as pg

import expansion as xp
from expansion import callbacks, colors, utils

def main():
    pg.init()
    xp.enable_multiprocessing(4) 

    LENGTH = 500
    COLOR_INSTRUCTION = colors.ColorB()
    EPOCHS = 0
    DIR = '500x500_random_single_point'
    FILE_NAME = '500x500_random_single_point'
    IMAGE_FORMAT = 'png'
    VIDEO_FORMAT = 'mp4'
    FPS = 60
    OFFSET = (0, 0)
    TICK = 60

    rand_x = random.randint(0, LENGTH)
    rand_y = random.randint(0, LENGTH)

    point = xp.ColoredPoint(LENGTH, (rand_x, rand_y), (1., 1., 1.), COLOR_INSTRUCTION)
    handler = xp.ColoredPointHandler(LENGTH, [point])

    cbs = [callbacks.Print(), 
                callbacks.Sample(DIR, IMAGE_FORMAT), 
                callbacks.PygameGUI(LENGTH, (LENGTH, LENGTH), OFFSET, TICK)]

    timer = utils.Timer(handler.simulate, True)
    timer(epochs=EPOCHS, callbacks=cbs)

    utils.stitch(DIR, FILE_NAME, FPS, (LENGTH, LENGTH), VIDEO_FORMAT)

if __name__ == '__main__':
    main()
