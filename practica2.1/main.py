#! /usr/bin/env python
# -*- coding: utf8 -*-
"""Exercici2.2 opencv"""
__author__ = 'marc'

import cv2
import numpy as np
import os


def circles(img_source):
    """Apply hough circles function"""
    # Reduce the noise.
    img_source = cv2.medianBlur(img_source, 5)
    cimg = cv2.cvtColor(img_source, cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img_source, cv2.cv.CV_HOUGH_GRADIENT, 1, 10,
                               param1=140, param2=30, minRadius=1, maxRadius=30)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
    cv2.imwrite(ROOT+'/img/hough-circles.jpg', cimg)
    cv2.imshow('detected circles', cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def hlines(img_source):
    """Draw lines using Houghlines function"""
    img_dst = np.copy(img_source)
    img_source = cv2.medianBlur(img_source, 5)
    gray = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 180)

    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img_dst, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imwrite(ROOT+'/img/hough-lines.jpg', img_dst)
    cv2.imshow('Hough Lines', img_dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def print_menu(img_source):
    """Print a menu"""
    img_menu = np.copy(img_source)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = '1-> Draw contours'
    color = (255, 255, 255)
    cv2.putText(img_menu, text, (10, 40), font, 0.5, color, 1, cv2.CV_AA)
    text = '2-> Hough Circles'
    cv2.putText(img_menu, text, (10, 80), font, 0.5, color, 1, cv2.CV_AA)
    text = '3-> Hough Lines'
    cv2.putText(img_menu, text, (10, 120), font, 0.5, color, 1, cv2.CV_AA)
    text = 'q-> Quit'
    cv2.putText(img_menu, text, (10, 160), font, 0.5, color, 1, cv2.CV_AA)
    cv2.imshow('menu', img_menu)


def find_contours(img_source):
    """Find and draw contours on an image"""
    dst = np.copy(img_source)
    img_source2 = cv2.medianBlur(img_source, 5)
    imgray = cv2.cvtColor(img_source2, cv2.COLOR_BGR2GRAY)
    thresh = 95
    thresh = cv2.threshold(imgray, thresh, 255, 0)[1]
    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(dst, contours[0], -1, (0, 0, 0), 3)
    cv2.imwrite(ROOT+'/img/contours.jpg', dst)
    cv2.imshow('Gray window', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def main():
    """Main program"""
    img = cv2.imread(ROOT+'/img/Lenna.png')
    # img_menu = np.copy(img)
    # print_menu(img_menu)
    cont = True
    while cont:
        print_menu(img)
        key = cv2.waitKey()
        if key == 49:
            find_contours(img)
        elif key == 50:
            circles_img = cv2.imread(ROOT+'/img/board.jpg', 0)
            circles(circles_img)
        elif key == 51:
            img2 = cv2.imread(ROOT+'/img/building.jpg')
            hlines(img2)
        elif key == ord('q'):
            cont = False

DIREC = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.split(DIREC)[0]

if __name__ == "__main__":
    main()
