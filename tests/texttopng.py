'''
Created on Mar 7, 2013

@author: payne
'''
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

img = Image.new('L', (600, 600), 255)
draw = ImageDraw.Draw(img)
text_to_draw = 'stringtxt'
draw.text((2, 2), text_to_draw)
del draw

img.save('image.png')
