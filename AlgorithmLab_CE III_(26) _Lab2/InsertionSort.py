import time

def insertionSort(A):
    start = time.time()
    for j in range (1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key    
    end = time.time()
    return A

#if __name__ == '__main__':
#    A = list(map(int,input().split()))
#    insertionSort(A)
