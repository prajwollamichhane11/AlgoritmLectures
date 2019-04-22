from InsertionSort import insertionSort
import random
from time import time
import matplotlib.pyplot as plt

worstTimeInsertion = []
bestTimeInsertion = []
sizeArray = []


n = 1000
#Time calculations for Best Case of Insertion Sort
for i in range(n, n * 11, n):
	sizeArray.append(i)
	randomvalues = random.sample(range(i), i)
	startTime = time()
	randomvalues.sort()
	insertionSort(randomvalues)
	endTime = time()
	totalTime = endTime - startTime
	bestTimeInsertion.append(totalTime)
	print(totalTime, "for size", i)

# draw graph for time vs size for both algorithms
fig, ax = plt.subplots(1, 1)
ax.plot(sizeArray,bestTimeInsertion, label = 'Best Case InsertionSort')
plt.xlabel("Size of Array")
plt.ylabel("Time")
plt.title("Simple Plotting")
plt.legend()
plt.show()

'''
n = 1000
#Time calculations for Worst Case of Insertion Sort
for i in range(n, n * 11, n):
	sizeArray.append(i)
	randomvalues = random.sample(range(i), i)
	startTime = time()
	randomvalues.sort()
	randomvalues = randomvalues[::-1]
	insertionSort(randomvalues)
	endTime = time()
	totalTime = endTime - startTime
	worstTimeInsertion.append(totalTime)
	print(totalTime, "for size", i)


fig, ax = plt.subplots(1, 1)
ax.plot(sizeArray,worstTimeInsertion, label = 'Worst Case InsertionSort')
plt.xlabel("Size of Array")
plt.ylabel("Time")
plt.title("Simple Plotting")
plt.legend()
plt.show()
'''
