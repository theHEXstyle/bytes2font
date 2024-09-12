# This is a simple program to check the font binaries.
# The concept is the make sure that the characters are properly encoded
# before they are rendered by the display

#The ONLY assumption that the code does is:
#    each line of the .cpp file corresponds to a character line

# input:  a .cpp font file
# output: an image rendition of the font (not an actual font)
HEX_PER_LINE = 3

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import re

filename = './input/FontReg36.cpp'  #<----------- change file name!

font_image = []

def divide_chunks(l, n):

    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


with open(filename) as file:
    lines = file.read().rstrip()
    matches = re.findall(r'0x([0-9abcdefABCDEF]+)', lines)  # regex to find hex values


counter = 0
char_lines = divide_chunks(matches, HEX_PER_LINE)
for char_line in char_lines:
    font_line = ''.join([bin(int(x, 16))[2:].zfill(8) for x in char_line])
    font_line = [(int(x)-1)*-255 for x in font_line]
    if font_image == []:
        font_image = [font_line]
    else:
        font_image.append(font_line)

image = Image.fromarray(np.array(font_image, dtype=np.uint8))

# Save the image
image.save(filename.replace('/input/', '/output/').replace('.cpp', '.png'))





