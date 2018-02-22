from datetime import datetime
from time import sleep

from ws281x_whatcolorisit.strip import initialize_strip
from ws281x_whatcolorisit.whatcolorisit import current_color

DISTRIBUTE = True


def distribute_color(strip, r, g, b, sleep_time=0.01):
    for i in range(strip.numPixels()):
        strip.setPixelColorRGB(i, r, g, b)
        strip.show()
        sleep(sleep_time)


def main():
    # initialize strip
    strip = initialize_strip()
    while True:
        # determine current color
        color = current_color(datetime.now().time())
        if DISTRIBUTE:
            # distribute color slowly across all pixels
            distribute_color(strip, int(color.r), int(color.g), int(color.b))
        else:
            # set color on all pixels
            for i in range(strip.numPixels()):
                strip.setPixelColorRGB(
                    i, int(color.r),
                    int(color.g), int(color.b)
                )
        strip.show()
        sleep(0.5)


if __name__ == '__main__':
    main()
