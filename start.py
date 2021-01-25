import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import os
from PIL import Image


# Raspberry Pi pin configuration:
RST = None
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
fps = 25
PATH = 'img/'

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()

time_sta = time.time()
try:
    while True:
        # Current Time
        time_cur = time.time()
        # Calculate the right frame to display
        frame = int((time_cur - time_sta) * fps) + 1
        filename = 'img' + str(frame) + '.bmp'
        # Load image and convert to 1 bit color.
        image = Image.open(os.path.join(PATH,filename)).convert('1')
        disp.image(image)
        disp.display()
except:
    # Clear Display
    print(os.path.join(PATH,filename))
    disp.clear()
    disp.display()
