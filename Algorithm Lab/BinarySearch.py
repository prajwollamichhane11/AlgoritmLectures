arr = list(map(int,input().split()))
n = int(input("Enter the no. you want to search: "))

first = 0
last = len(arr)-1
found = 0

while first<=last:
    midpoint = (first + last)//2
    if arr[midpoint] == n:
        found = 1
        break
    else:
        if n < arr[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1

if found == 1:
    print("Yes")
else:
    print("No")
