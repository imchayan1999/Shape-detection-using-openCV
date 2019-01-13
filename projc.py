import cv2
import numpy as np

# Getting image location and converting it to grayscale
image = cv2.imread('Enter the image location',cv2.IMREAD_GRAYSCALE)
cv2.imshow('original',image)

# Calculating lower and upper treshold by setting random error as 33%(0.33)
random = 0.33
m = np.median(image)
lowtresh = int(max(0, (1.0 - random) * m))
hightresh = int(min(255, (1.0 + random) * m))


# Finding edges using Canny edge detection method
edges = cv2.Canny(image, lowtresh, hightresh)

# Finding Contours
(_, cnts, _) = cv2.findContours(edges,
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# Using Contour Approximation method to find vertices of geometrical shapes
def detectShape(cnt):
    shape = 'unknown'
    peri = cv2.arcLength(c, True)
    vertices = cv2.approxPolyDP(c, 0.04 * peri, True)
    
    if len(vertices) == 3:
        shape = 'triangle'
        
# Differentiating between square and rectangle using aspect ratios.        
    elif len(vertices) == 4:
        x, y, width, height = cv2.boundingRect(vertices)
        aspectRatio = float(width) / height
        
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            shape = "square"
        else:
            shape = "rectangle"
    
    elif len(vertices) == 5:
        shape = "pentagon"
        
    elif len(vertices) == 6:
        shape = "hexagon"
    
    
    else:
        shape = "circle"
        
    return shape


for c in cnts:
   # Computing moment for area, centroid calculations etc.
    M = cv2.moments(c)
    
    # Finding Centroids
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])
    
    shape = detectShape(c)
    
    # Outlining the Contours
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    
    
    # Writing the name of the shape on the respective shapes.
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 2)
    
    cv2.imshow("Image", image)


cv2.waitKey(0)
cv2.destroyAllWindows()

