import time

arr = []
print ('Enter numbers to implement sorting as: N N N N N')
arr = list(map(int,input().split()))

start = time.time()
for i in range(len(arr)-1):
    min = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min] :
            min = j
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp
end = time.time()

print (arr)

print("The running time is: ",end-start)
