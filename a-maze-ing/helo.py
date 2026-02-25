import os
import sys

def draw_background(hex_color):
    r = (hex_color >> 16) & 255
    g = (hex_color >> 8) & 255
    b = hex_color & 255

    # Get terminal size
    rows, cols = os.get_terminal_size()

    # Set TrueColor background
    sys.stdout.write(f"\033[48;2;{r};{g};{b}m")
    
    # Move cursor top-left
    sys.stdout.write("\033[H")

    # Fill entire screen manually
    for _ in range(rows):
        sys.stdout.write(" " * cols + "\n")

    # Return cursor top-left
    sys.stdout.write("\033[H")
    sys.stdout.flush()

draw_background(0x0B132B)