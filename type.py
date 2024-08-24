import os
import time
from PIL import Image, ImageDraw, ImageFont
import curses
from drive import SSD1305

# Initialize display
disp = SSD1305.SSD1305()
disp.Init()
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
MAX_LINES = 4

def buffer(sec):
    disp.getbuffer(image)
    disp.ShowImage()
    time.sleep(sec)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

def linetext(content, line_number):
    draw.rectangle((0, line_number * 8, width, (line_number + 1) * 8), outline=0, fill=0)  # Clear the line
    draw.text((x, line_number * 8), content, font=font, fill=255)

def wrap_text(text, line_length):
    wrapped_lines = []
    lines = text.split('\n')  # Split text into lines based on newline characters

    for line in lines:
        current_line = ""
        for char in line:
            if len(current_line) < line_length:
                current_line += char
            else:
                wrapped_lines.append(current_line)
                current_line = char

        if current_line:
            wrapped_lines.append(current_line)

    return wrapped_lines

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(0)  # Set timeout to 0 for non-blocking behavior

    global input_string
    current_line = 0

    # Open the file in append mode
    with open("type.txt", "a") as f:
        while True:
            key = stdscr.getch()

            if key != -1:
                if key == 27:  # ESC key
                    input_string = ""  # Reset input string
                    current_line = 0
                    buffer(timeframe)
                elif key == curses.KEY_BACKSPACE or key == 127:  # Backspace key
                    if input_string:
                        input_string = input_string[:-1]  # Remove last character
                        wrapped_lines = wrap_text(input_string, 22)
                        start_line = max(0, len(wrapped_lines) - MAX_LINES)
                        for i, line in enumerate(wrapped_lines[start_line:]):
                            linetext(line, i)
                        current_line = len(wrapped_lines) - 1
                        buffer(timeframe)
                        f.seek(0)
                        f.truncate()  # Clear the file content before writing new content
                        f.write(input_string)
                elif key == curses.KEY_ENTER or key == 10:  # Enter key
                    input_string += '\n'
                    current_line += 1
                    f.write('\n')  # Write the newline character to the file
                else:
                    key_char = chr(key) if key < 256 else f"Special key {key}"
                    input_string += key_char
                    wrapped_lines = wrap_text(input_string, 22)
                    start_line = max(0, len(wrapped_lines) - MAX_LINES)
                    for i, line in enumerate(wrapped_lines[start_line:]):
                        linetext(line, i)
                    current_line = len(wrapped_lines) - 1
                    buffer(timeframe)
                    f.write(key_char)  # Write the character to the file

            stdscr.refresh()

            if input_string and input_string[0] == curses.KEY_F1:  # Exit condition
                break

curses.wrapper(main)
