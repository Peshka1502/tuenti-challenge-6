#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 6
# Taras Sotnikov
#
# Theres a comment in the png:
# comment a piet program qr.randomized.flipped.embedded.withnl.png
#
# flip vertically the image and call the Piet interpreter to get the output
# Piet interpeter: npiet-1.3d from http://www.bertnase.de/npiet/

from PIL import Image
from PIL import ImageOps
import os

col = Image.open("alice_shocked.png")
flip = ImageOps.mirror(col)

flip.save("alice_shocked_flip.png")

os.system("./npiet alice_shocked_flip.png")