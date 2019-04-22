from InsertionSort import insertionSort
import random
from time import time
import matplotlib.pyplot as plt

n = 1000
i = 0
timeInsertion = []
sizeArray = []

#Time calculations linear search
for i in range(n, n * 11, n):
	sizeArray.append(i)
	randomvalues = random.sample(range(i), i)
	startTime = time()
	insertionSort(randomvalues)
	endTime = time()
	totalTime = endTime - startTime
	timeInsertion.append(totalTime)
	print(totalTime, "for size", i)

# draw graph for time vs size for both algorithms
fig, ax = plt.subplots(1, 1)
ax.plot(sizeArray,timeInsertion, label = 'InsertionSort')
legend = ax.legend(loc = 'upper center', shadow = True, fontsize = 'large')
plt.show()
