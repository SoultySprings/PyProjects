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
    bext.clear()

    logos = []
    for i in range(numberOfLogos):
        logos.append({COLOR: random.choice(colors),
                      X: random.randint(1, width-4),
                      Y: random.randint(1, height-4),
                      DIR: random.choice(directions)})
        if logos[-1][X] %2 == 1:
            logos[-1][X]-=1

    cornerBounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            originalDirection = logo[DIR]

            if logo[X] == 0 and logo[Y] == 0 :
                logo[DIR] = downright
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == height-1 :
                logo[DIR] = upright
                cornerBounces += 1
            elif logo[X] == width-3 and logo[Y] == 0 :
                logo[DIR] = downleft
                cornerBounces += 1
            elif logo[X] == width-3 and logo[Y] == height-1 :
                logo[DIR] = upleft
                cornerBounces += 1


            elif logo[X] == 0 and logo[DIR] == upleft :
                logo[DIR] = upright
            elif logo[X] == width-3 and logo[DIR] == downleft :
                logo[DIR] = downright


            elif logo[X] == width-3 and logo[DIR] == upright :
                logo[DIR] = upleft
            elif logo[X] == width-3 and logo[DIR] == downright :
                logo[DIR] = downleft


            elif logo[Y] == 0 and logo[DIR] == upleft :
                logo[DIR] = downleft
            elif logo[Y] == 0 and logo[DIR] == upright :
                logo[DIR] = downright


            if logo[DIR] != originalDirection :
                logo[COLOR] - random.choice(colors)


            if logo[DIR] == upright :
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == upleft :
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == downright :
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == downleft :
                logo[X] -= 2
                logo[Y] += 1

        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bouncs : ', cornerBounces, end='')

        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0,0)

        sys.stdout.flush()
        time.sleep(pause_amount)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('')
        print('Bouncing DVD logo!')
        sys.exit()

