import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from matplotlib import pyplot as plt 
from sklearn.datasets import load_digits

digits = load_digits()

print(dir(digits))

df = pd.DataFrame(digits.data, digits.target)

x = digits.data
y = digits.target

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

model = SVC(C = 15.0, kernel = 'linear')

print (model.fit(x_train, y_train))

print (model.score(x_test, y_test))

print(model.predict([digits.data[60]]))

plt.matshow(digits.images[60])
plt.show()