import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from tkinter import Tk, Label, Button, Frame, filedialog, Entry
from PIL import ImageTk, Image
import numpy as np


#dir = "C:\\Users\\Jey Pérez\\OneDrive\\Documentos\\GitHub\\TESIS\\Imagenes"
dir = "D:\\IMAGENES\\Imagenes"
Categories = ['JPG', 'TIF']
data = []

for category in Categories:
    path = os.path.join(dir, category)
    label = Categories.index(category)
    
    for img in os.listdir(path):
        imgpath = os.path.join(path, img)
        imagen_img = cv2.imread(imgpath, 0)
        try:
            imagen_img = cv2.resize(imagen_img, (50, 50))
            image = np.array(imagen_img).flatten()
            data.append([image, label])
        except Exception as e:
            pass

print(len(data))

pick_in = open('data1.pickle', 'wb')
pickle.dump(data, pick_in)
pick_in.close()