import time
import logging
from PIL import Image, ImageDraw, ImageFont
import curses

# Import the SSD1305 library
from drive import SSD1305

# Initialize display
disp = SSD1305.SSD1305()
disp.Init()
logging.info("clear display")
disp.clear()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)
padding = 0
top = padding
bottom = height - padding
x = 0
timeframe = 0.01
font = ImageFont.truetype('04B_08__.TTF', 8)

input_string = ""

def buffer(sec):
    disp.getbuffer(image)
    disp.ShowImage()
    time.sleep(sec)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

def linetext(content):
    draw.rectangle((0, 0, width, 8), outline=0, fill=0)  # Clear the line
    draw.text((x, top), content, font=font, fill=255)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(0)  # Set timeout to 0 for non-blocking behavior

    global input_string

    while True:
        key = stdscr.getch()

        if key != -1:
            if key == 27:  # ESC key
                #linetext(' ')  # Clear the line
                input_string = ""  # Reset input string
                buffer(timeframe)
            elif key == curses.KEY_BACKSPACE or key == 127:  # Backspace key
                if input_string:
                    input_string = input_string[:-1]  # Remove last character
                    linetext(input_string)
                    buffer(timeframe)
            elif len(input_string) >= 22 and len(input_string) % 22 == 0:
              input_string += '\n'  # Append newline character
              linetext(input_string)
              buffer(timeframe)
              #press the enter key so that i can type on the next line
              #key = ord('\n')

            else:
                key_char = chr(key) if key < 256 else f"Special key {key}"
                input_string += key_char
                linetext(input_string)
                buffer(timeframe)

        stdscr.refresh()

        if input_string and input_string[0] == curses.KEY_F1:  # Exit condition
            break

curses.wrapper(main)
