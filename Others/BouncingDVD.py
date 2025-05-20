#Code as visible in earlier computers, the infamous bouncing DVD has been recreated in the following program

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires bext module in order to run, install and try again.')
    sys.exit()

width, height = bext.size()

width -= 1

numberOfLogos = 5
pause_amount = 0.2

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

upright = 'ur'
upleft = 'ul'
downright = 'dr'
downleft = 'dl'
directions = ['upright', 'upleft', 'downright', 'downleft']

COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
