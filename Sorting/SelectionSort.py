arr = []
print ('Enter numbers to implement sorting as: N N N N N')
arr = list(map(int,input().split()))

length = len(arr)

for i in range(length):
    min = arr[i]
    for j in range(i+1,length):
        if arr[j] < min :
            temp = min
            min = arr[j]
            arr[j] = temp
    arr[i] = min

print (arr)
