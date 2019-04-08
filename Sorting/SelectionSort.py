import time

arr = []
print ('Enter numbers to implement sorting as: N N N N N')
arr = list(map(int,input().split()))

length = len(arr)

start = time.time()
for i in range(length):
    min = arr[i]
    for j in range(i+1,length):
        if arr[j] < min :
            temp = min
            min = arr[j]
            arr[j] = temp
    arr[i] = min
end = time.time()

print (arr)

print("The running time is: ",end-start)
