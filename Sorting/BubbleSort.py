print ('Enter numbers to implement sorting as: N N N N N')
arr = list(map(int,input().split()))

length = len(arr)

for i in range(length):
    for j in range(0,length-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print("The Sorted numbers are:")
print(arr)
