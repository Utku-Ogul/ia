import cv2
import numpy as np
import matplotlib.pyplot as plt 

blank_image = np.zeros((512, 512, 3), dtype=np.uint16)
#512x512 boyutunda, 3 kanallı (RGB), tüm değerleri sıfır olan (siyah) boş bir görüntü oluşturur

plt.imshow(blank_image)
plt.show()


cv2.rectangle(blank_image,pt1=(384,0),pt2=(510,150),color=(0,255,0),thickness=10)
print(blank_image)


plt.imshow(blank_image)
plt.show()


cv2.rectangle(blank_image,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=10)
plt.imshow(blank_image)
plt.show()


cv2.circle(blank_image,center=(100,100),radius=50,color=(255,0,0),thickness=10)    
plt.imshow(blank_image)
plt.show()


cv2.circle(blank_image,center=(400,400),radius=50,color=(255,0,0),thickness=-1)    
plt.imshow(blank_image)
plt.show()


cv2.line(blank_image,pt1=(0,0),pt2=(512,512),color=(255,255,0),thickness=10)
plt.imshow(blank_image)
plt.show()


font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_image,text='Hello', org=(10,500),fontFace=font,fontScale=4,color=(255,255,255),thickness=3,lineType=cv2.LINE_AA)
plt.imshow(blank_image)
plt.show()

cv2