# Hex2ImageEncoder
Encode a hex dump into the IDAT section of a png file


This is not quite steganography and it doesn't create a malicious payload. The intended purpose is to encode abritary files as an image so that they may be passed in messaging apps or any other service that limits by file type, so the fact the image contains a file is rather obvious. Furthermore, if sent as plaintext, patterns can be seen with the naked eye that suggest things such as language or magic numbers. 

The method used takes a hex dump such as from 'xxd', chops this into 2 charecter sections which determines the value of a greyscale pixel. This creates an effeciency in cases of totally random data of around 31-33%. This can be improved by having high levels of sameness in the hexdump, or more practically, encoding different values in the RGBA slots. Currently, the transparency is used as a binary bit to determine the EOF.

TODO

Add the ability to pass filename arguments by commandline, rather than hardcoding names

Increase effeciency by using all RGB values
