# -*- coding: utf-8 -*-

#   Importing Modules/Libraries/Packages
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt



#   Import/Read image
img = misc.ascent()

plt.grid(False)
plt.gray()
plt.axis('off')
plt.title('Original Image')
plt.imshow(img)
plt.show()



#   Pre-processing
img_transformed = np.copy(img)
size_x = img_transformed.shape[0]
size_y = img_transformed.shape[1]



#   Convolution


#   Creating Filter

#   For Horizontal Convolution

# filter = [[3, -6, 3], [0, 0, 0], [-3, 6, -3]]
filter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
# filter = [[-1, -2, 3], [0, 0, 0], [1, 2, -3]]
# filter = [[3, 0, 3], [-1, 0, 1], [-3, 0, -3]]
# filter = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
# filter = [[1, 0, 3], [-2, 0, 2], [-1, 0, -3]]

weight = 1


#   Convolution image with filter
for x in range(1, size_x-1):
  for y in range(1, size_y-1):
    convolution = 0.0
    convolution = convolution + (img[x-1, y-1]*filter[0][0])
    convolution = convolution + (img[x, y-1]*filter[0][1])
    convolution = convolution + (img[x+1, y-1]*filter[0][2])
    convolution = convolution + (img[x-1, y]*filter[1][0])
    convolution = convolution + (img[x, y]*filter[1][1])
    convolution = convolution + (img[x+1, y]*filter[1][2])
    convolution = convolution + (img[x-1, y+1]*filter[2][0])
    convolution = convolution + (img[x, y+1]*filter[2][1])
    convolution = convolution + (img[x+1, y+1]*filter[2][2])
    convolution = convolution*weight

    if convolution<0:
      convolution = 0
    if convolution>255:
      convolution = 255
    img_transformed[x, y] = convolution

plt.grid(False)
plt.gray()
# plt.axis('off')
plt.title('Convolved Image')
plt.imshow(img_transformed)
plt.show()



#   Pooling


#   Processing
new_x = int(size_x/2)
new_y = int(size_y/2)
newImage = np.zeros((new_x, new_y))
for x in range(0, size_x, 2):
  for y in range(0, size_y, 2):
    pixels = []
    pixels.append(img_transformed[x, y])
    pixels.append(img_transformed[x+1, y])
    pixels.append(img_transformed[x, y+1])
    pixels.append(img_transformed[x+1, y+1])
    pixels.sort(reverse=True)
    newImage[int(x/2),int(y/2)] = pixels[0]

plt.grid(False)
plt.gray()
# plt.axis('off')
plt.title('Pooled Image')
plt.imshow(newImage)
plt.show()



#   Output Image
images = []
images.append(img)
images.append(img_transformed)
images.append(newImage)

plt.figure(figsize=(20, 10))
columns = 3
for i, image in enumerate(images):
    plt.subplot(int(np.ceil(len(images) / columns + 1)), columns, i + 1)
    plt.grid(False)
    plt.gray()
    if i==0:
      plt.title('Orginal Image')
      plt.axis('off')
    if i==1:
      plt.title('Convolved Image')
    if i==2:
      plt.title('Pooled Image')
    plt.imshow(image)
plt.show()
