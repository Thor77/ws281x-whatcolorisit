from datetime import datetime
from time import sleep

from ws281x_whatcolorisit.strip import initialize_strip
from ws281x_whatcolorisit.whatcolorisit import current_color


def main():
    # initialize strip
    strip = initialize_strip()
    while True:
        # set strip to current color
        color = current_color(datetime.now().time())
        for i in range(strip.numPixels()):
            strip.setPixelColorRGB(
                i, int(color.r),
                int(color.g), int(color.b)
            )
        strip.show()
        sleep(0.5)


if __name__ == '__main__':
    main()
