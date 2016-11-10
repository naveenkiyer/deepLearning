# import the necessary packages
import numpy as np
import cv2
import random

def createAffineTransformation(img, i):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)
    d = random.randint(1, 100)

    pts1 = np.float32([[a,a],[b,a],[a,b]])
    pts2 = np.float32([[c,d],[b,a],[d,a]])
    
    rows, cols, ch = img.shape
    
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols, rows), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=[0, 0, 0, 0])
    
    filename = "adidas_affine_" + str(i) + ".png"
    cv2.imwrite(filename, dst)

def medianBlurring(img, i): # i can only be odd!!!!! Its kernel size should be a positive odd integer.
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)
    blurred = cv2.medianBlur(img, i)
    filename = "adidas_mblur_" + str(i) + ".png"
    cv2.imwrite(filename, blurred)

def laplacianGradient(img, i):
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    filename = "adidas_laplac_" + str(i) + ".png"
    cv2.imwrite(filename, laplacian)

def morphologicalTransform(img, i):
    kernel = np.ones((i,i), np.uint8)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    filename = "adidas_morph_" + str(i) + ".png"
    cv2.imwrite(filename, gradient)

if __name__ == "__main__":
    # load the games image
    print("Starting program")
    img = cv2.imread("logos/adidas_t1.png", cv2.IMREAD_UNCHANGED)
    b_c, g_c, r_c, a_c = cv2.split(img)
    new_img = cv2.merge((b_c, g_c, r_c, a_c))
    for i in range(0, 30):
        print("For loop 1 iteration " + str(i))
        createAffineTransformation(new_img, i)
    medianBlurring(img, 5)
    laplacianGradient(img, 0)
#    for i in range(2, 20):
#        print("For loop 2 iteration " + str(i))
#        if i % 2 == 1:
#            morphologicalTransform(img, str(i))
#            cv2.waitKey(0)
