import os
import numpy as np	
from PIL import Image
import cv2
from sewar.full_ref import ssim

def Image_Plagiarism(img1,img2):
    # importing the image 
    im1 = Image.open(img1)
    im2 = Image.open(img2)
    
    # converting to jpg
    rgb_im1 = im1.convert("RGB")
    rgb_im2 = im2.convert("RGB") 

    # exporting the image
    rgb_im1.save("media/file/image_1.jpg")
    rgb_im2.save("media/file/image_2.jpg")

    image1 = cv2.imread("media/file/image_1.jpg")
    image2 = cv2.imread("media/file/image_2.jpg")

    # size not same then resizing

    image1_dim = image1.shape
    image2_dim = image2.shape

    isDiff = 0

    if image1_dim != image2_dim :
        if image1_dim[0] > image2_dim[0] :
            new_height = image2_dim[0]
        elif image1_dim[0] < image2_dim[0] :
            new_height = image1_dim[0]
        else :
            new_height = image1_dim[0]

        if image1_dim[1] > image2_dim[1] :
            new_width = image2_dim[1]
        elif image1_dim[1] < image2_dim[1] :
            new_width = image1_dim[1]    
        else :
            new_width = image1_dim[1]
        
        new_dim = (new_width, new_height)
        isDiff = 1

    if isDiff == 1:
        image1 = cv2.resize(image1, new_dim, interpolation = cv2.INTER_AREA)
        image2 = cv2.resize(image2, new_dim, interpolation = cv2.INTER_AREA)

    # finding the difference between two images by subtracting the image array values

    difference = cv2.subtract(image1,image2)

    res = not np.any(difference)

    print("Result of Plagiarism Detection : ")

    # checking the resultant image matrix for the diff and if there is 
    # then it will produce an image from that matrix (difference image)
    if res is True:
        print("These two are Same Images ")
    else:
        print("\nThese two are Different images\n")
        cv2.imwrite("media/file/difference_image.jpg", difference)
        #os.system("google-chrome-stable difference_image.jpg")

    # finding How similary the image is with help of Structural similary Index algorithm

    print("Structural Similarity Index(SSIM): ") 
    x1, x2 = ssim(image1,image2)
    x1 = round(x1*100,2)
    print(x1*100,"\n")
    print("The Similarity between these two images: ", (x1)*100, "%")

    

    if x1 > 0.5 :
        return x1,"Plagiarism Detected!"
        #print("Plagiarism Detected!\n")
    else:
        return x1,"Acceptable"
        #print("Acceptable\n")
