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
#root.iconbitmap('ico_Br.ico')     # Icono a ventana principal 
root.geometry("800x600")
root['background'] = '#19232d'

np.random.seed(42)


root.mainloop()
