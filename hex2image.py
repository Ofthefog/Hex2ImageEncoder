#!/usr/bin/python

from PIL import Image
import math, io

# Open target file's hexcode
# This assumes a hex file like the output of 'xxd -p' that was stripped of newlines

data = open('hexin.txt','r') 

# The image will be placed in the smallest square that will fit the data
# We can jump to the end of the file to obtain dimensions without having to iterate twice

data.seek(0,2)
toencode = (data.tell() - 1) / 2 
dim = int(math.ceil(math.sqrt(toencode)))
data.seek(0)

# Hex will be encoded into an greyscale value ( 2 digits a pixel )
# A transparent pixel stands for EOF
img = Image.new(mode = "RGBA", size = (dim,dim), color = (0,0,0,0))

pixels = img.load()

for y in range(dim):
    for x in range(dim):
	colourhex = "0x" + data.read(2)
	if len(colourhex) != 4: #0x + "FF" makes 4
		break # so EOF
	else:
	 colour = int(colourhex,16)
	 pixels[x,y] = (colour,colour,colour,255)

img.save("out.png")

data.close()
