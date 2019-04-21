# Best Case: O(1)
# Worst Case: O(log(N))
# Average Case: O(log(N))

#Author: Prajwol Lamichhane
def BinarySearch(arr,n):
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

#arr = list(map(int,input().split()))

#arr = sorted(arr)
#n = int(input("Enter the no. you want to search: "))
#BinarySearch(arr,n)

if __name__ == '__main__':
    arr = [0,1,2,3,4,5]
