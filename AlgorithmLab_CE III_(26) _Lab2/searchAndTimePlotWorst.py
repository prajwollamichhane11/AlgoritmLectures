
import matplotlib.pyplot as plt
import random
import time

from MergeSort import mergesort
from InsertionSort import insertionSort


def plotfunction():
    sample_size = 1
    x, y1, y2 = [], [], []

    n = 1000
    for n in range(n, n*11 , n):
        A = random.sample(range(n), n)

        start_time = time.time()
        sorted_A = insertionSort(A)
        end_time = time.time()
        x.append(n)
        y1.append(end_time - start_time)


        start_time = time.time()
        sorted_A = mergesort(A)
        end_time = time.time()
        y2.append(end_time - start_time)

    plt.plot(x, y1,label="Insertion")
    plt.plot(x, y2,label="Merge")
    plt.title("Worst Case Insertion vs Merge")
    plt.xlabel("Size(N)", color = "blue")
    plt.ylabel("Execution Time", color = "blue")
    plt.show()

if __name__ == "__main__":
    plotfunction()
