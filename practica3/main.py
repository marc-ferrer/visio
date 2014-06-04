#!/usr/bin/env python
# -*- coding: utf8 -*-
"""face detecting using opencv"""
import cv2
# import video


def main():
    """Main function"""
    cap = cv2.VideoCapture(0)
    detectorLocation = '../haarcascades/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(detectorLocation)
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Display the resulting frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray = cv2.equalizeHist(gray)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
