# 128x32 Pixel Canvas

import time
import datetime
import sys
import os
import pygame
from PIL import Image, ImageDraw, ImageFont
from drive import SSD1305

# Initialize SSD1305 display
disp = SSD1305.SSD1305()
disp.Init()
disp.clear()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# Define the folder name
folder_name = "Saved"

# Check if the folder exists
if not os.path.exists(folder_name):
    # If not, create the folder
    os.makedirs(folder_name)
    print(f'Folder "{folder_name}" created.')
else:
    print(f'Folder "{folder_name}" already exists.')

# Initialize pygame
pygame.init()

# Set up the drawing window with a larger size for easier drawing
scale_factor = 8
pygame.display.set_caption("Canvas")
button_height = 40
window_width, window_height = width * scale_factor, height * scale_factor + button_height
window = pygame.display.set_mode((window_width, window_height))

# Set up canvas and colors
canvas = pygame.Surface((window_width, window_height - button_height))
canvas.fill((0, 0, 0))  # Black canvas
draw_color = (255, 255, 255)  # White pen
erase_color = (0, 0, 0)  # Black to erase
brush_size = 15

# Flag to track changes in canvas
canvas_changed = False

# Font for drawing on SSD1305 display
font = ImageFont.truetype('04B_08__.TTF', 8)

# Function to show image on SSD1305 display
def show_image_on_display(image_path):
    picture = Image.open(image_path).resize((width, height)).convert('1')
    disp.clear()
    disp.getbuffer(picture)
    disp.ShowImage()
    picture.close()

# Function to draw text on SSD1305 display
def draw_text_on_display(text):
    draw.rectangle((0, 0, width, height), outline=0, fill=0)  # Clear previous text
    draw.text((0, 0), text, font=font, fill=255)
    disp.getbuffer(image)
    disp.ShowImage()

# Function to save canvas as PNG
def temp_canvas():
    small_canvas = pygame.transform.smoothscale(canvas, (width, height))
    pygame.image.save(small_canvas, "Saved/temp.png")
    show_image_on_display("Saved/temp.png")

# Button properties
button_font = pygame.font.Font(None, 30)
button_texts = ["Clear", "Save", "Increase Brush", "Decrease Brush"]
buttons = []
button_width = window_width // 4
for i, text in enumerate(button_texts):
    rect = pygame.Rect(i * button_width, window_height - button_height, button_width, button_height)
    buttons.append((rect, text, False))  # Add False to track if the button is pressed

# Main loop
running = True
last_save_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button draws
                mouseX, mouseY = event.pos
                if mouseY < window_height - button_height:
                    pygame.draw.circle(canvas, draw_color, (mouseX, mouseY), brush_size)
                    canvas_changed = True
            elif pygame.mouse.get_pressed()[2]:  # Right mouse button erases
                mouseX, mouseY = event.pos
                if mouseY < window_height - button_height:
                    pygame.draw.circle(canvas, erase_color, (mouseX, mouseY), brush_size)
                    canvas_changed = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            for i, (rect, text, _) in enumerate(buttons):
                if rect.collidepoint(mouseX, mouseY):
                    buttons[i] = (rect, text, True)  # Mark the button as pressed
                    if text == "Clear":
                        canvas.fill((0, 0, 0))  # Clear the canvas
                        canvas_changed = True
                    elif text == "Save":
                        current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                        small_canvas = pygame.transform.smoothscale(canvas, (width, height))
                        filename = f"Saved/{current_time}.png"
                        pygame.image.save(small_canvas, filename)
                    elif text == "Increase Brush":
                        brush_size += 1
                    elif text == "Decrease Brush":
                        brush_size -= 1
        elif event.type == pygame.MOUSEBUTTONUP:
            for i, (rect, text, pressed) in enumerate(buttons):
                if pressed:
                    buttons[i] = (rect, text, False)  # Mark the button as not pressed

    # Autosave every 1 second if canvas has changed
    current_time = time.time()
    if current_time - last_save_time >= 0.01 and canvas_changed:
        temp_canvas()
        last_save_time = current_time
        canvas_changed = False

    # Draw everything on the pygame window
    window.fill((0, 0, 0))
    window.blit(canvas, (0, 0))
    
    # Draw buttons
    for rect, text, pressed in buttons:
        color = (75, 75, 75) if pressed else (100, 100, 100)  # change button color when pressed 
        pygame.draw.rect(window, color, rect)
        text_surface = button_font.render(text, True, (255, 255, 255))
        window.blit(text_surface, text_surface.get_rect(center=rect.center))
        
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
