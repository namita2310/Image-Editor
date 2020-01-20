import cv2 
import argparse 
import pytesseract
import string
  
# now let's initialize the list of reference point 
ref_point = [] 
crop = False

def funcRotate(degree=0):
    degree = cv2.getTrackbarPos('degree','Frame')
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    cv2.imshow('Rotate', rotated_image)
    #clone1=rotated_image.copy()
    
    return rotated_image
    
def shape_selection(event, x, y, flags, param): 
    # grab references to the global variables 
    global ref_point, crop 
  	
    
    # if the left mouse button was clicked, record the starting 
    # (x, y) coordinates and indicate that cropping is being performed 
    if event == cv2.EVENT_LBUTTONDOWN: 
        ref_point = [(x, y)] 
  
    # check to see if the left mouse button was released 
    elif event == cv2.EVENT_LBUTTONUP: 
        # record the ending (x, y) coordinates and indicate that 
        # the cropping operation is finished 
        ref_point.append((x, y)) 
  
        # draw a rectangle around the region of interest 
        cv2.rectangle(rotated_image, ref_point[0], ref_point[1], (0, 255, 0), 2) 
        
        cv2.imshow("image",rotated_image) 
  
  
# construct the argument parser and parse the arguments 
ap = argparse.ArgumentParser() 
ap.add_argument("-i", "--image", required = True, help ="Path to the image") 
args = vars(ap.parse_args()) 
  
# load the image, clone it, and setup the mouse callback function 
image = cv2.imread(args["image"]) 
clone = image.copy() 
cv2.namedWindow("Frame") 


degree=0
height, width = image.shape[:2]
cv2.createTrackbar('degree','Frame',degree,360,funcRotate)
rotated_image=funcRotate(0)

cv2.imshow('Frame',image)  
  
# keep looping until the 'q' key is pressed 
cv2.setMouseCallback("Rotate", shape_selection) 
while True: 
    # display the image and wait for a keypress 
    cv2.imshow("image",image) 
    key = cv2.waitKey(1) & 0xFF
  
    # press 'r' to reset the window 
    if key == ord("r"): 
        rotated_image = rotated_image.copy() 
  
    # if the 'c' key is pressed, break from the loop 
    elif key == ord("c"): 
        break
  
if len(ref_point) == 2: 
    crop_img = rotated_image[ref_point[0][1]:ref_point[1][1], ref_point[0][0]: #clone
                                                           ref_point[1][0]] 
    cv2.imshow("crop_img", crop_img)
     
    cv2.waitKey(0)
    
 
  
# close all open windows 
cv2.destroyAllWindows()  


