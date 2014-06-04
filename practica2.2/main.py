#! /usr/bin/env python
# -*- coding: utf8 -*-
"""Exercici2.2 opencv"""
__author__ = 'marc'
import cv2
import numpy


def opening(img):
    """apply opening to an image"""
    kernel = numpy.ones((7, 7), numpy.uint8)
    opening_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Opening', opening_img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def closing(img):
    """apply closing to an image"""
    kernel = numpy.ones((7, 7), numpy.uint8)
    closing_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('closing', closing_img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def canny():
    """Apply canny edge detection"""
    # Remove the noise in the image
    detected_edges = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(detected_edges, 60, 110, apertureSize=3)
    cv2.imshow('canny', edges)
    cv2.waitKey()
    cv2.destroyAllWindows()


def print_menu(img):
    """Print a menu"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = '1-> Opening'
    cv2.putText(img, text, (10, 40), font, 0.5, (255, 255, 255), 1, cv2.CV_AA)
    text = '2-> Closing'
    cv2.putText(img, text, (10, 80), font, 0.5, (255, 255, 255), 1, cv2.CV_AA)
    text = '3-> Canny edge detection'
    cv2.putText(img, text, (10, 120), font, 0.5, (255, 255, 255), 1, cv2.CV_AA)
    text = 'q-> Quit'
    cv2.putText(img, text, (10, 160), font, 0.5, (255, 255, 255), 1, cv2.CV_AA)
    cv2.imshow('menu', img)


def cannyTrack(img):
    """function"""

    def nothing(value, *arg):
        cv2.imshow('edge', edge)
    cv2.namedWindow('edge')
    cv2.createTrackbar('thrs1', 'edge', 60, 120, nothing)
    cv2.createTrackbar('thrs2', 'edge', 110, 250, nothing)
    exit_canny = False
    while not exit_canny:
        detected_edges = cv2.GaussianBlur(img, (5, 5), 0)
        gray = cv2.cvtColor(detected_edges, cv2.COLOR_BGR2GRAY)
        thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
        thrs2 = cv2.getTrackbarPos('thrs2', 'edge')
        edge = cv2.Canny(detected_edges, thrs1, thrs2, apertureSize=3)
        vis = img.copy()
        # vis /= 2
        vis[edge != 0] = (0, 255, 0)
        cv2.imshow('edge', edge)
        key = cv2.waitKey(1)
        if key == 53:
            cv2.imwrite('../img/canny-Lena.png', edge)
            exit_canny = True


def main():
    """Main function"""
    img = cv2.imread('../img/Lenna.png')
    img_menu = numpy.copy(img)
    print_menu(img_menu)
    # key = cv2.waitKey()
    # cv2.namedWindow('canny demo')
    # cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, canny)
    key = cv2.waitKey()
    if key == 49:
        opening(img)
    elif key == 50:
        closing(img)
    elif key == 51:
        canny()
    elif key == 52:
        cannyTrack(img)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    # img = cv2.imread('../img/Lenna.png')
    # lowThreshold = 0
    # max_lowThreshold = 100
    # ratio = 3
    main()
