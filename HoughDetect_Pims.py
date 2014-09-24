# Uses the library pims, which is available at: https://github.com/soft-matter/pims 
import pims
from time import sleep
# This is the magic phrase to import a tiff stack.
v = pims.TiffStack('/media/joe/New Volume/ScopeData/StillImage/2014-Sep/RawFiles/Alexa555_0917_NHS_FITC_unadjusted.tif')
for frame in v[:]:
    plt.figure()
    # convert from 16 bit unsigned to 8 bit unsigned
    tmp = cv2.convertScaleAbs(frame, alpha=(255.0/65535.0))
    # show the image.  May want to just update a single image frame in the future.
    plt.imshow(tmp, cmap= 'gray', interpolation='bicubic')
    cv2.GaussianBlur(tmp, (5,5),0)
    # These parameters need to be adjusted
    circles = cv2.HoughCircles(tmp,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
    #print circles
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(tmp,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(tmp,(i[0],i[1]),2,(0,0,255),3)
    plt.xticks([]), plt.yticks([])
    plt.show()
    #cv2.waitKey(0)
    # NOTE: This produces an error around the conversion to the uint (line: circles = np.unit16(np.around(circles))).
    # Not sure why this error is here yet.
