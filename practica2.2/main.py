__author__ = 'marc'

import cv2
import numpy

def main():
    """Main function"""
    img = cv2.imread('./img/Lenna.png')
    kernel = numpy.ones((7, 7), numpy.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Opening', opening)
    cv2.waitKey()
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Closing', closing)
    cv2.destroyWindow('Opening')
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
