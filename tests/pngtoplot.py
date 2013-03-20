'''
Created on Mar 7, 2013

@author: payne
'''
import pylab
import matplotlib.image as mpimg

img = mpimg.imread('image.png')
pylab.subplot(2, 2, 4, frameon=False, xticks=[], yticks=[], axisbg='k')
pylab.plt.imshow(img)
pylab.show()
pylab.savefig('test.png')

