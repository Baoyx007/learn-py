__author__ = 'haven'

from PIL import Image,ImageFilter

def resize():
    im = Image.open('test.jpg')
    w,h = im.size

    print('original image size : %s*%s'%(w,h))

    im.thumbnail((w//2,h//2))
    print('resize /2 /2')
    im.save('thumbnail.jpg','jpeg')

def blur():
    im = Image.open('test.jpg')
    im2 = im.filter(ImageFilter.BLUR)
    im2.save('blur.jpg','jpeg')

blur()


