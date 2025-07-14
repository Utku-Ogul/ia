import numpy as np  # NumPy library for scientific computing and array operations
import matplotlib.pyplot as plt  # Matplotlib library for plotting and visualization
from PIL import Image  # Import Image module to open and process image files

# Load an image using PIL
pic = Image.open('00-puppy.jpg')  # Opens the image file '00-puppy.jpg'

#plt.imshow(pic)  # Display the image
#plt.axis('off')  # eksenleri gizler (isteğe bağlı)
#plt.show()       # resmi ekranda açar

type(pic)  # Check the type of the image object

pic_arr = np.asarray(pic)  # Convert the image to a NumPy array
pic_arr.shape # Check the shape of the NumPy array representing the image
    #(1300, 1950, 3)


#plt.imshow(pic_arr)

pic_red = pic_arr.copy()  # Create a copy of the original image array
#RGB renk kanallarını ayırma 
plt.imshow(pic_red[:,:,0])  # Display the copied image
plt.show()  # Show the image window

plt.imshow(pic_red[:,:,0],cmap='gray')  # Display the red channel in grayscale
plt.show()  # Show the image window


pic_red[:, :, 1] = 0    # Zero out contribution from green
pic_red[:, :, 2] = 0    # Zero out contribution from blue
plt.imshow(pic_red) # Display the modified image with only the red channel
plt.show()  # Show the image window
