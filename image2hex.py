#!/usr/bin/python

from PIL import Image
import io

# Open target's picture file
img = Image.open('out.png')
pixels = img.load()
dim = img.size[1] # We assume it is a square because we ( us! ) encoded it that way

# Open a text file to write the hex into
hout = open('hexout.txt','w')

# We will check just the Red value because we were ineffecient and did greyscale.
# I don't know of there is a way to go directly from pixel to hex but this works


for y in range(dim):
    for x in range(dim):
	if pixels[x,y][3] == 0:#EOF as decided in our encoding
	 break
	hexprelim = str(hex(pixels[x,y][0])) # this adds the 'x0' whch we don't need
	
	if len(hexprelim) == 4:
	 hexstripped = hexprelim[2]+hexprelim[3]
	elif len(hexprelim) == 3: # Whenever it is less than 10 the 0 is truncated, logically
	 hexstripped = "0" + hexprelim[2]
	else:
	 hexstripped = "00"
	
	hout.write(hexstripped)
	
