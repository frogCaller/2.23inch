## MAKE SURE TO INSTALL FORTUNE
## sudo apt install fortune -y

import time
import os
import logging
from PIL import Image, ImageDraw, ImageFont
import curses
import subprocess
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

def buffer(sec):
    disp.getbuffer(image)
    disp.ShowImage()
    time.sleep(sec)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

def linetext(content):
    for i in range(1, len(content) + 1):
        draw.rectangle((0, 0, width, 8), outline=0, fill=0)  # Clear the line
        draw.text((x, top), content[:i], font=font, fill=255)
        disp.getbuffer(image)
        disp.ShowImage()
        time.sleep(timeframe)

def wrap_text(text, line_length):
    wrapped_lines = []
    words = text.split()
    current_line = ""

    for word in words:
        if len(current_line) + len(word) <= line_length:
            current_line += word + " "
        else:
            wrapped_lines.append(current_line.strip())
            current_line = word + " "

    # Append the last line
    if current_line:
        wrapped_lines.append(current_line.strip())

    return wrapped_lines[:3]  # Limit to 3 lines max

def get_fortune():
    while True:
        # Run the fortune command and capture its output
        result = subprocess.run(['fortune'], stdout=subprocess.PIPE)
        fortune_text = result.stdout.decode('utf-8').strip()

        # Check if fortune text is longer than 64 characters
        if len(fortune_text) <= 64:
            # Wrap text to fit within OLED width (22 characters per line, 3 lines)
            wrapped_text = "\n".join(wrap_text(fortune_text, 22))
            return wrapped_text

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(100)  # Refresh every 100ms

    while True:
        key = stdscr.getch()

        fortune = get_fortune()
        linetext(fortune)
        buffer(timeframe)
        time.sleep(4)

        if key == 27:  # ESC key
            break

# Initialize curses and run the main function
curses.wrapper(main)
