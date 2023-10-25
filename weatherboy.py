import matplotlib.pyplot as plt
import numpy
import pandas as pd

df = pd.read_csv('Tempdata.csv')
X = df["Pressure"]
Y = df["Temperature"]

plt.scatter(X, Y)

model = numpy.poly1d(numpy.polyfit(X, Y, 3))
line = numpy.linspace(min(X), max(X), 100)
plt.plot(line, model(line))
plt.show()




