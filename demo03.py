# encoding = 'utf-8'
import os

imgpath = os.path.dirname(os.path.realpath(__file__))
img_sign = open(imgpath + '/params/sign.png', 'rb')
img_photo = open(imgpath + '/params/photo.png', 'rb')
files = [('files', ('photo.png', img_photo, 'image/png')), ('files', ('sign.png', img_sign, 'image/png'))]
print(files)