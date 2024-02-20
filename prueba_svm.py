import cv2
import numpy as np
import pylab as plt
from glob import glob
import argparse
import os
import progressbar
import pickle as pkl
from numpy.lib import stride_tricks
from skimage import feature
from sklearn import metrics
from sklearn.model_selection import train_test_split
import time
import mahotas as mt

import numpy as np
import skimage
from skimage import io
import glob
import cv2
import matplotlib.pyplot as plt

def load_data_set(load_aug = False):
  import skimage
  imgs = io.imread('DJI_20231004102555_0001_MS_G.TIF')
  imgs = skimage.color.gray2rgb(imgs)
  print(imgs.shape)
  labels = io.imread('DJI_20231004102555_0001_MS_G.TIF')
  #labels = skimage.color.gray2rgb(labels)
  test = io.imread('DJI_20231004102555_0001_MS_NIR.TIF')
  test = skimage.color.gray2rgb(test)
  imgs_train = []
  label_train = []
  imgs_test = []

  print("_"*30)
  print("[INFO] Loading orginal training data...")
  for i in range(len(imgs)):
    imgs_train.append(np.array(imgs[i]))
    label_train.append(np.array(labels[i]))
  print("check the consistency of training data...")
  print("num of imgs_train: {}".format(len(imgs_train)))
  print('num of groundTruth_train: {}'.format(len(label_train)))
  
  print("_"*30)
  print("[INFO] Loading orginal testing data...")
  for i in range(len(test)):
    imgs_test.append(np.array(test[i]))
  print('num of test images: {}'.format(len(imgs_test)))
  return imgs_train, label_train, imgs_test



imgs_train, label_train, imgs_test = load_data_set()

print(imgs_train[0].shape)
print(label_train[0].shape)

# Mostrar las imágenes y las etiquetas
print('Mostrando los datos originales:')
f, ax = plt.subplots(1, 2)
ax[0].imshow(imgs_train[0])
ax[0].set_title('1ra imagen de entrenamiento')
ax[1].imshow(label_train[0])
ax[1].set_title('1ra etiqueta de entrenamiento')

plt.show()