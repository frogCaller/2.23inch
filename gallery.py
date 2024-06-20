# Show saved drawings on display

import time
import sys
import os
import glob
import platform
from PIL import Image
from drive import SSD1305 

# Initialize display
disp = SSD1305.SSD1305()
disp.Init()
disp.clear()

width = disp.width
height = disp.height

image_folder = "Saved"
file_extension = ".png"

# Use glob to find all PNG files in the folder
file_paths = glob.glob(os.path.join(image_folder, '*' + file_extension))
file_paths.sort()

try:
    while True:
        for n in file_paths:
            # Open and resize the image
            picture = Image.open(n).resize((width, height)).convert('1')

            # Display the image on the OLED display
            disp.clear()
            disp.getbuffer(picture)
            disp.ShowImage()

            # Close the image to free up resources
            picture.close()

            # Wait for any key press to display the next frame
            if platform.system() == 'Windows':
                import msvcrt
                if msvcrt.kbhit():
                    if ord(msvcrt.getch()) == 27:  # Check if the key pressed is ESC
                        raise KeyboardInterrupt
            else:
                import termios
                import tty
                import sys

                def getkey():
                    fd = sys.stdin.fileno()
                    old_settings = termios.tcgetattr(fd)
                    try:
                        tty.setraw(fd)
                        ch = sys.stdin.read(1)
                    finally:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    return ch

                if getkey() == '\x1b':  # Check if the key pressed is ESC
                    raise KeyboardInterrupt

except KeyboardInterrupt:
    print("\n")
    print("Exiting the program...")

finally:
    disp.clear()
    sys.exit(0)
