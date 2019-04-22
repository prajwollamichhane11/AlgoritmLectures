# Best Case: O(1)
# Worst Case: O(N)
# Average Case: O(N)

#Author: Prajwol Lamichhane

def LinearSearch(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            found = 1
            break
        else:
            found = 0
    if found == 1:
        return 1
    else:
        return -1

#arr = list(map(int,input().split()))

#n = int(input("Enter the no. you want to search: "))

#print(LinearSearch(arr,5))
