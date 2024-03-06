from modelo import Algorithms
Procesador= Algorithms()
#SaveName: NOmbre imagen a guardar
#ImagePath: Ruta de la imagen a procesar
#SaveName => "NOmbredeguardo.png"
#### PARAMETROS DE ENTRADA
Kmeans=Algorithms()
SaveDir= 'C:/Users/Asus/Documents/CRIEE-MAIZ_2023/BD_y_ALGORITMOS/ALGORITMOS/Procesamiento_Imagenes'
ImagePath= 'C:/Users/Asus/Documents/CRIEE-MAIZ_2023/BD_y_ALGORITMOS/ALGORITMOS/Procesamiento_Imagenes'
#SaveDir= 'C:/Users/Asus/Documents/CRIEE-MAIZ_2023/BD_y_ALGORITMOS/ALGORITMOS/Procesamiento_Imagenes'
#DirPath= 'C:/Users/Asus/Documents/CRIEE-MAIZ_2023/BD_y_ALGORITMOS/ALGORITMOS/Procesamiento_Imagenes'
SaveName= 'prueba.png'
Procesador.SaveSegImage(SaveName, ImagePath, SaveDir, "Kmeans")
kmeans.SaveSegImage(SaveName, ImagePath, SaveDir, "Kmeans")
Algorithms.SaveSegDir(SaveDir, DirPath,"Kmeans" )
