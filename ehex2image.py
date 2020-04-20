#!/usr/bin/python

from PIL import Image
import math, io

# Open target file's hexcode
# This assumes a hex file like the output of 'xxd -p' that was stripped of newlines

data = open('hexin.txt','r') 

# The image will be placed in the smallest square that will fit the data
# We can jump to the end of the file to obtain dimensions without having to iterate twice

data.seek(0,2)
toencode = (data.tell() - 1) / 6 # we will put 2 digits into the RGB values of a pixel
dim = int(math.ceil(math.sqrt(toencode)))
data.seek(0)

# A transparent pixel stands for EOF
img = Image.new(mode = "RGBA", size = (dim,dim), color = (0,0,0,0))

# Time to apply the hex to the RGB values
pixels = img.load()

for y in range(dim):
    for x in range(dim):
	hexchunk = data.read(6)
	sizecheck = len(hexchunk)
	if   sizecheck == 6:
		transparent = 255
		red = int("0x" + hexchunk[0]+hexchunk[1],16)
		blue = int("0x" + hexchunk[2]+hexchunk[3],16)
		green = int("0x" + hexchunk[4]+hexchunk[5],16)

		pixels[x,y] = (red,green,blue,transparent)

	elif sizecheck == 4:
		transparent = 170 # this will mean that 2 bits are encoded
		red = int("0x" + hexchunk[0]+hexchunk[1],16)
		blue = int("0x" + hexchunk[2]+hexchunk[3],16)

		pixels[x,y] = (red,green,0,transparent)
	
	elif sizecheck == 2:
		transparent = 85 # only 1 bit wlll be encoded
		red = int("0x" + hexchunk[0]+hexchunk[1],16)

		pixels[x,y] = (red,0,0,transparent)

	else:
		transparent = 0 # EOF, with no left over space

img.save("out.png")

data.close()
