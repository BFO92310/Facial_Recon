#!usr/bin/env python
#-*- coding: utf-8 -*-
from picamera import PiCamera
from time import sleep
import cv2


camera=PiCamera()
#lancement camera
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/BFO/img.jpg')
camera.stop_preview()

#définition des arguments
imagePath='/home/pi/Desktop/BFO/img.jpg'
cascPath='/home/pi/Desktop/BFO/haarcascade.xml'

#création de la cascade puis lecture de la photo
faceCascade = cv2.CascadeClassifier(cascPath)

image=cv2.imread(imagePath)
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Détection visage
faces=faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

#Réponse
import pygame
pygame.init()
if len(faces)==1:
    pygame.mixer.music.load("/home/pi/Desktop/BFO/sounds/you-look-so-handsome.wav")
    pygame.mixer.music.play()
    sleep(3)
elif len(faces)>1:
    pygame.mixer.music.load("/home/pi/Desktop/BFO/sounds/hi.wav")
    pygame.mixer.music.play()
    sleep(3)
else:
    pygame.mixer.music.load("/home/pi/Desktop/BFO/sounds/no.wav")
    pygame.mixer.music.play()
    sleep(3)

