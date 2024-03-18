# import numpy as np

# data = np.genfromtxt("iris/iris.data", delimiter=",")

# print("Data type: ", type(data))
# print("Data shape: ", data.shape)
# print(data[:10])

# data1 = np.genfromtxt("iris/iris.data", delimiter=",", dtype=None)
# print(data1.shape)
# print(type(data1))
# print(type(data1[0]))
# print(type(data1[0][4]))
# print(data1[:10])

# dt = np.dtype("f8, f8, f8, f8, U30")
# data2 = np.genfromtxt("iris/iris.data", delimiter=",", dtype=dt)
# print(data2.shape)
# print(type(data2))
# print(type(data2[0]))
# print(type(data2[0][0]))
# print(data2[:10])


import numpy as np
import matplotlib as npl
import matplotlib.pyplot as plt

dt = np.dtype("f8, f8, f8, f8, U30")
data2 = np.genfromtxt("iris/iris.data", delimiter=",", dtype=dt)

# Данные из отдельных столбцов
sepal_length = [] # Sepal Lenght
sepal_width = [] # Sepal Width
petal_length = [] # Petal Lenght
petal_width = [] # Petal Width

# Выполняем обход всей коллекции data2
for dot in data2:
    sepal_length.append(dot[0])
    sepal_width.append(dot[1])
    petal_length.append(dot[2])
    petal_width.append(dot[3])

# Строим графики по проекции данных
# Учитываем, что каждые 50 типов ирисов идут последовательно
plt.figure(1)
setosa, = plt.plot(sepal_length[:50], sepal_width[:50], 'ro', label='Setosa')
versicolor, = plt.plot(sepal_length[50:100], sepal_width[50:100], 'g^', label='Versicolor')
virginica, = plt.plot(sepal_length[100:150], sepal_width[100:150], 'bs', label='Virginica')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

plt.show()

