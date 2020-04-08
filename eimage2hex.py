#!/usr/bin/python

from PIL import Image
import io

# Open target's picture file
img = Image.open('out.png')
pixels = img.load()
dim = img.size[1] # We assume it is a square because we ( us! ) encoded it that way

# Open a text file to write the hex into
hout = open('hexout.txt','w')





 


# Decoding is just encoding done backwards
# This is much cleaner than using hex()
for y in range(dim):
    for x in range(dim):
	transparency = pixels[x,y][3]
	# Our transparency ranges should have plenty of room between these checks
	if transparency > 50:
		red = format(pixels[x,y][0],'x')#R
		hout.write(red.zfill(2))# zfill gets rid of the truncating single digit problem
	if transparency > 100:
		green = format(pixels[x,y][1],'x')#G
		hout.write(green.zfill(2))
	if transparency > 200:
		blue = format(pixels[x,y][2],'x')#B
		hout.write(blue.zfill(2))
	if transparency != 255:
		break
	
hout.close()


