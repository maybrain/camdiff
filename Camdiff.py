#!/usr/bin/python

import pygame.camera
import pygame.image
import datetime
import time
import os

def compare(ar1, ar2):
  camera_res = (640,480)
  diff_image = ar1.compare(ar2, distance=0, weights=(0.299,0.587,0.114) )
  ys = range(0,camera_res[1]/20)
  for x in range (0,camera_res[0]/20):
    for y in ys:
      if diff_image[x*20,y*20]>0:
        return True
  return False

ar1 = None
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
first = True
while True:
  cam.start()
  img = cam.get_image()
  cam.stop()
  ar2 = pygame.PixelArray (img)

  if first or not compare(ar1,ar2):
    first = False
    print 'DIFERENTE! '+str(datetime.datetime.now())
    ar1 = ar2
    target_file = 'imgs/'+str(datetime.datetime.now()).replace(' ','').replace('-','').replace(':','').replace('.','')+'.jpg'
    try:
        pygame.image.save(img, target_file)
    except pygame.error:
        os.mkdir('imgs')
        pygame.image.save(img, target_file)
  else: print 'IGUAL!! '+str(datetime.datetime.now())

  time.sleep(5)
pygame.camera.quit()
