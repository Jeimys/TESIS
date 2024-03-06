import skimage as ski
from skimage import data
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
from skimage import data, segmentation, color
from skimage import graph
from matplotlib import pyplot as plt
import os


class Algorithms:
    """"""

    def __init__(self, **kwargs):
        kwargsSet = {"KmeansThresh"}
        if "KmeansThresh" in kwargs:
            KmeansThresh = kwargs.pop("KmeansThresh")
            self.AssertKmeansThresh(KmeansThresh)
            self.KmeansThresh = KmeansThresh

        assert (
            kwargs == dict()
        ), f"Invalids/invalid kwargs.\nValids kwargs are {kwargsSet}."

    ################################################################
    # Segmentation techniques
    # This methods are not explicitly used in the use of a object Algorithms,
    # The method that must be called are of type Get,Show or Put.

    def __K_means__(self, ImagePath):
        Image = ski.io.imread(ImagePath)
        labels1 = segmentation.slic(Image)
        g = graph.rag_mean_color(Image, labels1)
        if hasattr(self, "KmeansThresh"):
            labels2 = graph.cut_threshold(labels1, g, self.KmeansThresh)
            Result = color.label2rgb(labels2, Image, kind="avg", bg_label=0)
        else:
            Result = color.label2rgb(labels1, Image, kind="avg", bg_label=0)

        return Result

    ################################################################
    # Get methods ( Methods that return data )

    def GetSegImage(self, ImagePath, Technique):
        self.AssertDataType(ImagePath, "Path", str)
        self.AssertTechnique(Technique)
        if Technique == "Kmeans":
            return self.__K_means__(ImagePath)

    def GetSegDir(self, DirPath, Technique):
        self.AssertDataType(DirPath, "Path", str)
        self.AssertTechnique(Technique)
        FilesNames = os.listdir(DirPath)
        Data = []
        for FileName in FilesNames:
            ImagePath = os.path.join(DirPath, FileName)
            Data.append(self.GetSegImage(ImagePath, Technique))
        return Data

    ################################################################
    # Show methods ( Methods that show segment images )

    def ShowSegImage(self, ImagePath, Technique):
        self.AssertDataType(ImagePath, "Path", str)
        self.AssertTechnique(Technique)
        Image = self.GetSegImage(ImagePath, Technique)
        plt.imshow(Image)
        plt.tight_layout()
        plt.axis("off")
        plt.show()

    def ShowSegDir(self, DirPath, Technique):
        self.AssertDataType(DirPath, "Path", str)
        self.AssertTechnique(Technique)
        FilesNames = os.listdir(DirPath)
        for FileName in FilesNames:
            ImagePath = os.path.join(DirPath, FileName)
            self.ShowSegImage(ImagePath, Technique)

    ################################################################
    # Put methods ( Methods that put data as atributes )

    def PutSegImage(self, ImagePath, Technique):
        self.AssertDataType(ImagePath, "Path", str)
        self.AssertTechnique(Technique)
        self.SegImage = self.GetSegImage(ImagePath, Technique)

    def PutSegDir(self, DirPath, Technique):
        self.AssertDataType(DirPath, "Path", str)
        self.AssertTechnique(Technique)
        self.DirData = self.GetSegDir(DirPath, Technique)

    def PutKmeansThresh(self, KmeansThresh):
        self.AssertKmeansThresh(KmeansThresh)
        self.KmeansThresh = KmeansThresh

    ################################################################
    # Save methods ( Methods that save data )

    def SaveSegImage(self, SaveName, ImagePath, SaveDir, Technique):
        self.AssertDataType([SaveName, ImagePath, SaveDir], "Path", str)
        self.AssertTechnique(Technique)
        Image = self.GetSegImage(ImagePath, Technique)
        SavePath = os.path.join(SaveDir, SaveName)
        plt.imsave(SavePath, Image)

    def SaveSegDir(self, SaveDir, DirPath, Technique):
        self.AssertDataType([SaveDir, DirPath], "Path", str)
        self.AssertTechnique(Technique)
        try:
            os.mkdir(SaveDir)
        except:
            pass
        FileNames = os.listdir(DirPath)
        for FileName in FileNames:
            ImagePath = os.path.join(DirPath, FileName)
            self.SaveSegImage(FileName, ImagePath, SaveDir, Technique)

    ################################################################
    # Asserts methods ( Methods that save data ). This asserts methods are commun to many functions
    # Are not implemented asserts methods that works only for a specific function
    # Before any method the necessary assert methods are called, this kill and show erros in the inputs

    def AssertDataType(self, Data, Name, DataType):
        if type(Data) != list:
            assert (
                type(Data) == DataType
            ), f"{Name} must be a {DataType}, got: {type(Data)}"
        else:
            for values in Data:
                self.AssertDataType(values, Name, DataType)

    def AssertTechnique(self, Technique):
        TechniquesSet = {"Kmeans"}
        assert (
            Technique in TechniquesSet
        ), f"{Technique} is not a valid segmentation technique.\nThe valids methods are {TechniquesSet}"

    def AssertKmeansThresh(self, KmeansThresh):
        self.AssertDataType(KmeansThresh, "KmeansThresh", int)
        assert (
            KmeansThresh >= 0
        ), f"Intensity must be greater than 0, got: {KmeansThresh}"
