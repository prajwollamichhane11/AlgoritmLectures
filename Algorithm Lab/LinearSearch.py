arr = list(map(int,input().split()))

n = int(input("Enter the no. you want to search: "))

for i in range(len(arr)):
    if arr[i] == n:
        i = 1
        break
    else:
        i = 0
if i == 1:
    print("Yes")
else:
    print("No")
    
