from LinearSearch import LinearSearch
from BinarySearch import BinarySearch
import random
from time import time
import matplotlib.pyplot as plt

n = 100
i = 0
timeLinear = []
timeBinary = []
sizeArray = []

#Time calculations linear search
for i in range(n, n * 10, n):
	sizeArray.append(i)
	randomvalues = random.sample(range(i), i)
	startTime = time()
	LinearSearch(randomvalues, randomvalues[i-1])
	endTime = time()
	totalTime = endTime - startTime
	timeLinear.append(totalTime)
	print(totalTime, "for size", i)

n = 100000
i = 0

#Time Plotting for the binary search
for i in range(n, n * 10, n):
	randomvalues = random.sample(range(i),i)
	startTime = time()
	BinarySearch(randomvalues, randomvalues[i-1])
	endTime = time()
	totalTime = endTime - startTime
	timeBinary.append(totalTime)
	print(totalTime, "for size", i)

# draw graph for time vs size for both algorithms
fig, ax = plt.subplots(1, 1)
ax.plot(sizeArray,timeLinear, label = 'Linear Search')
ax.plot(sizeArray,timeBinary, label = 'Binary Search')
legend = ax.legend(loc = 'upper center', shadow = True, fontsize = 'large')
plt.show()
