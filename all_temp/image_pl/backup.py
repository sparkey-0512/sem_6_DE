print("Image Plagiarism Program ----\n\n") 

import os
import numpy as np	
from PIL import Image
import cv2
from sewar.full_ref import mse, rmse, psnr, uqi, ssim, ergas, scc, rase, sam, msssim, vifp

#print("Select the first IMAGE: ")
#img_file_1 = input()
#
#print("Select the second one: ")
#img_file_2 = input()

# importing the image 
im1 = Image.open("images/monkey_diff.jpeg")
im2 = Image.open("images/monkey_filter.jpg")
  
# converting to jpg
rgb_im1 = im1.convert("RGB")
rgb_im2 = im2.convert("RGB") 

# exporting the image
rgb_im1.save("monkey1.jpg")
rgb_im2.save("monkey2.jpg")

image1 = cv2.imread("monkey1.jpg")
image2 = cv2.imread("monkey2.jpg")

# size not same resizing

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

#difference = cv2.subtract(image1,image2)
#
#res = not np.any(difference)
#print("Result of Plagiarism Detection : ")
#
#if res is True:
#    print("These two are Same Images ")
#else:
#    print("\nThese two are Different images\n")
#    cv2.imwrite("difference_image.jpg", difference)
#    print("Check the root file for the Resulting image formed")
#    print("which shows the difference between two source images input")
#    print("\n")
#    os.system("google-chrome-stable difference_image.jpg")

#print("Mean Squared Error(MSE): ") 
#print(mse(image1,image2),"\n")

print("Root Mean Squared Error(RMSE): ") 
print(rmse(image1,image2),"\n")

#print("Peak Signal-to-Noise Ration(PSNR): ") 
#print(psnr(image1,image2),"\n")

print("Structural Similarity Index(SSIM): ") 
x1, x2 = ssim(image1,image2)
x = (x1 + x2)/2
print(x,"\n")

print("Universal Quality Image Index (UQI): ") 
print(uqi(image1,image2),"\n")

#print("Multi-scale Structural Similarity Index(MS-SSIM): ") 
#print(msssim(image1,image2),"\n")
#
#print("Erreur Relative Globale Adimensionnelle de Synthese(ERGAS): ") 
#print(ergas(image1,image2),"\n")
#
#print("Spatial Correlation Coefficient (SCC): ") 
#print(scc(image1,image2),"\n")
#
#print("Relative Average Spectral Error(RASE): ") 
#print(rase(image1,image2),"\n")

print("Spectral Angle Mapper(SAM): ") 
print(sam(image1,image2),"\n")

#print("Visual Information Fidelity(VIF): ") 
#print(vifp(image1,image2),"\n")


print("Program ends here")
