import numpy as np
import matplotlib.pyplot as plt

import cv2 #for OpenCV functions

img = cv2.imread('/home/mjin/Desktop/workplace/ia/numpy/00-puppy.jpg') #read image file
type(img) #check type of img
print(type(img))
#always check the location of the image file is correct


print(img.shape) #check shape of img


plt.imshow(img) #show image
plt.show()


# !!!!! 
#matplotlib uses RGB color space, while OpenCV uses BGR.
# So, if you want to display an image read by OpenCV using matplotlib, you need to convert it from BGR to RGB.
# This can be done using cv2.cvtColor()


fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert from
plt.imshow(fix_img) # Show the image
plt.show()          # Open the window
img_gray = cv2.imread("/home/mjin/Desktop/workplace/ia/numpy/00-puppy.jpg", cv2.IMREAD_GRAYSCALE) #read image file in grayscale

plt.imshow(img_gray , cmap='gray') #show image in grayscale
plt.show() #show image in grayscale

plt.imshow(img_gray , cmap='magma') #show image in magma colormap
plt.show() #show image in magma colormap


fix_img.shape

new_img = cv2.resize(fix_img, (1000, 400)) #resize image to 300x300 pixels
plt.imshow(new_img) #show resized image
plt.show() #show resized image



w_ratio = 0.5
h_ratio = 0.5

new_img =cv2.resize(fix_img,(0,0),img,w_ratio,h_ratio) #resize image to 50% of original size
plt.imshow(new_img) #show resized image
plt.show() #show resized image

new_img = cv2.flip(new_img,0)
plt.imshow(new_img) #show flipped image
plt.show() #show flipped image

new_img = cv2.flip(new_img,1)
plt.imshow(new_img) #show flipped image
plt.show() #show flipped image


new_img = cv2.flip(new_img,-1)
plt.imshow(new_img) #show flipped image
plt.show() #show flipped image


cv2.imwrite('my_new_picture.jpg',new_img)




fig = plt.figure(figsize=(10, 8))       # 10x8 inç boyutunda bir figür (çizim alanı) oluştur
ax = fig.add_subplot(111)               # 1 satır, 1 sütun, 1. subplot: tek bir grafik alanı oluştur
ax.imshow(fix_img)                      # fix_img görüntüsünü bu subplot üzerinde göster
plt.show() 