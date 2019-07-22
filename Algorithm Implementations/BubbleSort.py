import time

print ('Enter numbers to implement sorting as: N N N N N')
arr = list(map(int,input().split()))

length = len(arr)

start = time.time()
for i in range(length):
    for j in range(0,length-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
end = time.time()

print("The Sorted numbers are:")
print(arr)

print("The running time is: ",end-start)
