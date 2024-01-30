# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:33:11 2023

@author: gloes
"""


import os
import random
import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from tkinter import Tk, Label, Button, Frame, filedialog, Entry
from PIL import ImageTk, Image


root = Tk()
root.title("GUI software de identificación de imagenes en base k-means")
#root.iconbitmap('ico_Br.ico')
root.geometry("800x600")
root['background'] = '#19232d'

img_1 = Image.open("imagen1.jpg")

np.random.seed(42)

#dir = 'C://Users//gloes//Desktop//Codigo//BrIm'
dir = 'C:/Users/Jey Pérez/OneDrive/Escritorio/NDVI/BrIm'
img_temp = cv2.imread('imagen3.jpg', 0)

Catg = ['isquemia', 'NMO', 'Normal', 'PRES']
data = []
data1 = []
labela = []
data_label = []

# a = 0
# b = 0
# c = 0
d = 0
SZ = 32
# Data reading

for category in Catg:
    path = os.path.join(dir, category)
    label = Catg.index(category)
    
    for img in os.listdir(path):
        imgpath = os.path.join(path, img)
        Br_img = cv2.imread(imgpath, 0)
        try:
            Br_img = cv2.resize(Br_img, (SZ, SZ))
            image1 = np.array(Br_img).flatten()
            Br_img = Br_img.astype('float32')
            if "I" in img[:6]:
                # a += 1
                labela.append("isquemia")
            elif "N" in img[:6]:
                # b += 1
                labela.append("NMO")
            elif "P" in img[:6]:
                # c += 1
                labela.append("PRES")
            else:
                if d==4: continue
                d += 1
                labela.append("Normal")
            data1.append(Br_img)
            # data.append([image1, label])
            
        except Exception as e:
            pass

data1 = np.array(data1)

for i in labela:
    if i == "isquemia":
        data_label.append(0)
    elif i == "NMO":
        data_label.append(1)
    elif i == "Normal":
        data_label.append(2)
    else:
        data_label.append(3)
data_label = np.array(data_label)

data2 = data1

data1 = data1/255.0

# k-means accept data with less than 3 dimensions
reshaped_data = data1.reshape(len(data1), -1)
reshaped_data.shape


kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit_predict(reshaped_data)
kmeans.cluster_centers_.shape
# 2,1024
kmeans.cluster_centers_ = kmeans.cluster_centers_*255
plt.figure(figsize = (10, 9))
bottom = 0.35

reference_labels = {}


def get_reference_dict(clusters, data_label):
    reference_label = {}
    # For loop to run through each label of cluster label
    for i in range(len(np.unique(clusters))):
        index = np.where(clusters == i, 1, 0)
        num = np.bincount(data_label[index == 1]).argmax()
        reference_label[i] = num
    return reference_label


# Mapping predictions to original labels
def get_labels(clusters, refernce_labels):
    temp_labels = np.random.rand(len(clusters))
    for i in range(len(clusters)):
        temp_labels[i] = reference_labels[clusters[i]]
    return temp_labels


reference_labels = get_reference_dict(clusters, data_label)
predicted_labels = get_labels(clusters, reference_labels)

print(accuracy_score(predicted_labels, data_label))


ran_numb = random.randint(0, 15)

img_identify = predicted_labels[ran_numb]

img_in = data_label[ran_numb]


Catg = ['isquemia', 'NMO', 'Normal', 'PRES']

print(Catg[int(img_identify)])
print(Catg[int(img_in)])

Nk_brain = data2[ran_numb]
plt.imshow(Nk_brain, cmap='gray')

upFrame = Frame(root, width=200, height=600)
upFrame.grid(row=0, column=0, padx=70, pady=2)

upFrame1 = Frame(root, width=200, height=600, bg='#19232d')
upFrame1.grid(row=0, column=1, padx=70, pady=2)

rightFrame = Frame(root, width=200, height=600)
rightFrame.grid(row=1, column=1, padx=70, pady=2)

leftFrame = Frame(root, width=200, height=600)
leftFrame.grid(row=1, column=0, padx=50, pady=10)

rsz_img1 = img_1.resize((220, 110), Image.ANTIALIAS)
N_img1 = ImageTk.PhotoImage(rsz_img1)
# N_img = ImageTk.PhotoImage(Nbrain)
imgtk = ImageTk.PhotoImage(image=Image.fromarray(Nk_brain))

e = Entry(rightFrame, width=20)
e_1 = Entry(rightFrame, width=20)

e.grid(row=0, column=1)

e_1.grid(row=1, column=1)


def getName():
    name = e.get()
    label_a = Label(rightFrame, text=name)
    label_a.grid(row=3, column=1, padx=20)


def getAge():
    name = e_1.get()
    label_e = Label(rightFrame, text=name)
    label_e.grid(row=4, column=1, padx=20)


accuracy_percent = accuracy_score(predicted_labels, data_label)*100


label_logo = Label(upFrame, image=N_img1).grid(row=0, column=0)
label_img = Label(leftFrame, image=imgtk).grid(row=0, column=0)
label_a = Label(rightFrame, text="Nombre: ").grid(row=3, column=0, padx=20)
label_e = Label(rightFrame, text="Edad: ").grid(row=4, column=0, padx=20)
label_1 = Label(
    rightFrame, text="Anomalia: "
    + str(Catg[int(img_in)]))
label_1.grid(row=5, column=0, padx=20)
label_2 = Label(rightFrame,
                text="Identificada: "
                + str(Catg[int(img_identify)]))
label_2.grid(row=6, column=0, padx=20)
label_3 = Label(rightFrame, text="Porcentaje de confiabilidad:"
                + str(accuracy_percent) + "%").grid(
                    row=7, column=0, padx=20)
label_4 = Label(upFrame1,
                text="UNIVERSIDAD PONTIFICIA BOLIVARIANA",
                bg='#19232d', fg='#fff').grid(row=0, column=0, padx=20)
label_5 = Label(upFrame1,
                text="Programa de ingenieria electronica",
                bg='#19232d', fg='#fff').grid(row=1, column=0, padx=20)
label_7 = Label(upFrame1,
                text="Desarrollado por: Juan D.",
                bg='#19232d', fg='#fff').grid(row=3, column=0, padx=20)



def openf():
    global label_img
    global img_l
    global img_r
    global label_1
    global label_2
    root.filename = filedialog.askopenfilename(
        initialdir="C:/Users/Jey Pérez/OneDrive/Escritorio/NDVI/BrIm",
        title="Selecciona una imagen", filetypes=(("png files", "*.png"),
                                                  ("all files", "*.*")))
    img_l = Image.open(root.filename)
    img_temp = cv2.imread(root.filename, 0)
    img_temp = cv2.resize(img_temp, (SZ, SZ))
    # img_tempo1 = np.array(img_temp).flatten()
    img_temp = img_temp.astype('float32')
    img_temp1 = img_temp/255
    reshaped_img = img_temp1.reshape(-1, 1024)
    reshaped_img.shape
    cluster_img = kmeans.predict(reshaped_img)
    pred_img = get_labels(cluster_img, reference_labels)
    rzs_img = img_l.resize((250, 250), Image.ANTIALIAS)
    img_r = ImageTk.PhotoImage(rzs_img)
    label_img = Label(leftFrame, image=img_r).grid(row=0, column=0)
    label_1.grid_forget()
    label_2.grid_forget()
    label_2 = Label(rightFrame,
                    text="Identificada: "
                    + str(Catg[int(pred_img)])).grid(row=6, column=0, padx=20)


button_name = Button(rightFrame, text="Ingresar nombre",
                      command=getName).grid(row=0, column=0)

button_age = Button(rightFrame, text="Ingresar edad",
                    command=getAge).grid(row=1, column=0)

button_open = Button(leftFrame, text="Open", bg="#6F7997", fg="white",
                      command=openf).grid(row=1, column=0)

root.mainloop()
