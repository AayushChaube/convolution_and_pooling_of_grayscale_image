#   Convolution and Pooling of Grayscale Image

##  Abstract
**Digital Image Processing has given many gifts to the world. Convolution and Pooling is one among them. This project implements the concept of Convolution and Pooling to compress the image by keeping the essential feature/information of the image. Here, the implementation is carried out without using any built-in function or any Machine Learning/Deep Learning frameworks. This implementation can be used in various Deep Learning/Machine Learning application as it increases the training speed because low image quality.**

##  Keywords
_Convolution, Pooling, Digital Image Processing, Grayscale Images, Image Processing, Feature Engineering_

##  Introduction
Right when Digital Signal Processing made an impact across the world in the domain of signal processing, with its application in almost every domain around the universe, there was an emerging technology that enhanced the application of Digital Signal Processing to another level, and of-course, made its own application as well. Electronics made it easy to build a camera. But Digital Image Processing gave those images a quality assurance. In today’s world, people click photo from their camera, they give it various cosmetic effect and post it on their social handles. The process of clicking image is dealt with electronics (i.e., Photo-transistors, etc.), and the posting of images on social media is dealt with computer domain (i.e., cloud computing, servers, backend, frontend, etc.), but the image effects is made possible due to Digital Image Processing[1][2]. Even when a company designs driver-less cars, Digital Image Processing is used to give eyes to the car. Hence, the use of a digital computer to run an algorithm on digital images is known as Digital Image Processing [6].

Digital Image Processing gives the developer a variety of options to manipulate any given image [1][3]. A few implementations of digital image processing are Image sharpening, rotations, blur effect, edges detection, morphological operations, color conversion, and many more [1][2]. All these operations are essential in almost all the fields of industries across the globe [4]. But there are situations when image quality is not the preference, but what is in the image, is what matters [6]. Under such a case, working on high graphic image will take more computation resources. This implies more processing time and/or more cost for system.

So, we need an algorithm, applying which to a digital image will degrade the image quality. But usually, degrading the image quality, leads to losing essential information of the image. So, say, if there is a grayscale image of a shoes. A researcher wants to create a classification model, saying that whether this image is having a shoe or not? Under such a case, if we degrade the quality and leading to which the image loses the information of the image (noise in image or manipulation of pixel values the image), then the model will not be able to classify. Hence, it is important to maintain the image’s essential information while degrading the image quality [7]. This will still have the original number of pixels, which still makes it quite a heavy file, but light than the original image. Hence if we apply another algorithm on the recent image such that the image not only degrades the image quality but also compresses or decreases the number of pixels. Again, the algorithm, should make sure that the compressed image should not lose the image information/feature [3][4][7].

A convolution is a filter that passes over an image, processing, it, and extracting features that show a commonality in the image [2][8]. Pooling is an algorithm used to reduce the overall amount of information in an image, while maintaining the features that are detected as present [5]. One way to do this is to make use of various built-in functions or frameworks available on the internet [8]. Whereas the other way is to built your own method to perform the exact algorithm [6][9]. So, the project is implementing Convolution and Pooling without using any built-in functions/methods or any frameworks.

##  Method
_A. Convolution:_

Generating a convolution is very simple. Simply scan every pixel in the image and then look at its neighboring pixels. You multiply out the values of these pixels by the equivalent weights in a filter [8][9].

So, for example consider this (Fig. 1)

In this case a 3×3 Convolution is specified.

The current pixel value is 192, but you can calculate the new one by looking at the neighbor values, and multiplying them out by the values specified in the filter, and making the new pixel value the final amount [5].

![Convolution Example](assets\doc\convolution_example_image.png)
$$\text{Fig. 1.} \quad \text{Convolution Example}$$

_B. Pooling_

Just like Convolution, Pooling helps us greatly in detecting features from an image, as well [5]. There are number of different types of pooling, but for simplification let us go with the one called MAX pooling.

The idea is here to iterate over the image, and look at the pixel and its immediate neighbors to the right, beneath, and right-beneath. Take the largest (hence the name MAX pooling) of them and load it into the new image. Thus, the new image will be ¼ the size of the old image (since, the dimensions on X and Y being halved by this process.) [5][8][9]. You will see that the features get maintained despite this compression!

![Pooling Example](assets\doc\pooling_example_image.png)
$$\text{Fig. 2.} \quad \text{Pooling example}$$

##  Implementation
_A. Algorithm:_

1.  Start
1.	Import necessary libraries/modules/packages
1.	Read image
1.	Convert the image in grayscale, if originally not in grayscale
1.	Store the dimensions of the image in a variable
1.	Create filter
1.	Initialize weight such that the result of the weight multiplied by the result of sum of all the elements of the filter is either zero or one.
1.	Initially map the center of the filter to the pixel that intercepts second column and second row of the image.
1.	Multiply the image pixel with the mapped filter pixel and calculate the sum of the individual pixel multiplication result
1.	Multiply the result with weight
1.	If result is less than 0, then update the value of image pixel, mapped by the center of the filter, to 0
1.	If result is greater than 255, then update the value of image pixel, mapped by the center of the filter, to 255
1.	Move to the next pixel in the row, and check if that pixel is before or on the second-last column of the image
1.	If yes, then repeat from step 9
1.	If no, then move to next row, and check if that row is before or on the second-last row of the image.
1.	If yes, then start from the pixel that intercepts second column of the present row, and then repeat from step 9
1.	If no, then stop the iteration
1.	Display output convolved image
1.	Decide the pooling value (n×n)
1.	Initialize new image’s number of rows and columns by dividing convolved image’s rows and columns by ‘n’
1.	Create an empty image (or matrix with zero values) of the dimension as mentioned in step 19
1.	Initially select the pixel that intercepts the first row and first column of the convolved image
1.	Create an empty list
1.	Append the pixel to the list
1.	Move to the next pixel of the same row
1.	Repeat step 24 and 25 for ‘n-1’ times
1.	Move to next row, and repeat step 24 and 25 for ‘n’ times
1.	Repeat step 27 for ‘n-2’ times
1.	Sort the list in reverse order (descending order)
1.	Update the pixel value of the new image (current row value of convolved image divided by 2, and current column value of convolved image divided by 2) with the first value of the list
1.	Clear the list
1.	Repeat step 24 to step 31 until all the pixels of the convolved image are pooled
1.	Display pooled image
1.  Stop

##  Results and Discussions
_A. Results_
![Original image](assets\doc\original_image.png)
$$\text{Fig. 3.} \quad \text{Original image}$$

![Convolved image](assets\doc\convolved_image.png)
$$\text{Fig. 4.} \quad \text{Convolved image}$$

![Pooled image](assets\doc\pooled_image.png)
$$\text{Fig. 5.} \quad \text{Pooled image}$$

![Comparison of Original image, Convolved image and Pooled image](assets\doc\comparison.png)
$$\text{Fig. 6.} \quad \text{Comparison of Original image, Convolved image and Pooled image}$$

_B. Discussions:_

We can see the effects of the filters that we have used in our code. But with different filter values, we can have different filter effects [1][2][6]. So, consider the following filter values, and their impact on the image.

Using [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]] gives us a very strong set of vertical lines. This is seen in the figure below (Fig. 7.).

![Vertical line effects](assets\doc\vertical_line_effects.png)
$$\text{Fig. 7.} \quad \text{Vertical line effects}$$

Using [[-1, -2, -1], [0, 0, 0], [1, 2, 1]] gives us horizontal lines. This is shown in the figure below (Fig. 8.).

![Horizontal Line Effects](assets\doc\horizontal_line_effects.png)
$$\text{Fig. 8.} \quad \text{Horizontal line effects}$$

This set of code is custom made. With the latest upgrade in the technology, there are various packages and modules available in languages like Python, MATLAB, etc., where rather than typing these lengthy algorithms, just a couple of lines of codes will give you the same result [5][6]. But one would find it difficult to learn the algorithm of such modules

##  Conclusion
_A. Conclusion_

This project touched some of the basics and the key concepts of Digital Image Processing. The very concept of digital filters was used to demonstrate how filters application on image, changes/effects the image. The effects shown here was degrading the image quality while maintaining its feature. This is called as Convolution. Along with convolution, pooling was also demonstrated, where the image was compressed to 25% of the original image size, without losing the important information of the image. The implementation of convolution and pooling on grayscale image without using any built-in function, incorporated the theoretical concept and helped to clarify the concept of the same.

_B. Future Scope_

This project was a stepping stone to the Digital world of Image. This project can be used in various innovative technologies like Deep Learning, Image Processing, etc. This concept of helps greatly in automation industry. Because convolution and pooling boost the speed of extracting features from images, by reducing the image quality and number of pixels, hence they can be used to train millions of images at one go with lesser amount of computation power as compared to the one that would be needed if convolution and pooling would not have been implemented. This model could also help in saving hours of time in development of driverless/pilotless automobiles. With latest upscale in the world of Virtual Reality and Augmented Reality, this process could help in developing some amazing augmented effects A biggest application of this concept would be in the health-care domain for diagnosis, prognosis, and treatment of disease. Classification systems like Handwritten Digit Classifier, American Sign Language Classification, Fingerprint Classification, etc., are a pool of applications for convolution and pooling.

##  References

1.	Wikipedia, the free encyclopedia, “Digital image processing - WIkipedia”, [https://en.wikipedia.org/wiki/Digital_image_processing](https://en.wikipedia.org/wiki/Digital_image_processing), April, 2021.
1.	“Digital Image Processing – Tutorialspoint”, [https://www.tutorialspoint.com/dip/index.htm](https://www.tutorialspoint.com/dip/index.htm), 2021.
1.	Anil K. Jain, “Fundamentals and Digital Image Processing”, Prentice Hall of India Private Ltd., Third Edition.
1.	“Digital Image Processing (DIP) Tutorial - Javatpoint”, [https://www.javatpoint.com/digital-image-processing-tutorial](https://www.javatpoint.com/digital-image-processing-tutorial), 2020.
1.	“Machine Learning Glossary | Google Developers”, [https://developers.google.com/machine-learning/glossary/#convolution](https://developers.google.com/machine-learning/glossary/#convolution), January, 2021.
1.	William K Pratt, “Digital Image Processing”, Third Edition, John Wiley & Sons, Inc., 2001.
1.	“Representation: Feature Engineering | Machine Learning Crash Course”, [https://developers.google.com/machine-learning/crash-course/representation/feature-engineering](https://developers.google.com/machine-learning/crash-course/representation/feature-engineering), February, 2020.
1.	Miguel Fernandez Zafra, “Understanding Convolutions and Pooling in Neural Networks: a simple explanation – Towards Data Science”, [https://towardsdatascience.com/understanding-convolutions-and-pooling-in-neural-networks-a-simple-explanation-885a2d78f211](https://towardsdatascience.com/understanding-convolutions-and-pooling-in-neural-networks-a-simple-explanation-885a2d78f211), May, 2020.
1.	S. Albawi, T. A. Mohammed and S. Al-Zawi, "Understanding of a convolutional neural network," 2017 International Conference on Engineering and Technology (ICET), 2017, pp. 1-6, doi: 10.1109/ICEngTechnol.2017.8308186.
