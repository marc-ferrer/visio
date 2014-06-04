__author__ = 'marc'

import cv2


def main():
    """Main program"""
    img = cv2.imread('../img/Lenna.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = 100
    ret, thresh = cv2.threshold(imgray, thresh, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 0, 0), 3)
    cv2.imshow('Gray window', img)
    cv2.waitKey()

if __name__ == "__main__":
    main()