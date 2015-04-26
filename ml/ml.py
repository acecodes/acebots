import matplotlib.pyplot as plt
import matplotlib

from sklearn import datasets, svm

# Preferably TkAgg
print("Current backend:", matplotlib.get_backend())
print("Matplotlib location:", matplotlib.matplotlib_fname())

# Sample built-in dataset
digits = datasets.load_digits()

print("Dataset size:", len(digits.data))

# Classifier
clf = svm.SVC(gamma=0.001, C=100)

x, y = digits.data[:-10], digits.target[:-10]
clf.fit(x, y)

print('Prediction:', clf.predict(digits.data[-2]))

plt.imshow(digits.images[-2],
           cmap=plt.cm.gray_r,
           interpolation='nearest')

plt.show()
