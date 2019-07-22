def linsearch(arr,n):
        l = len(arr)
        for i in range(0,l):
                if arr[i] == n:
                        return i
        return 0


arr = [0,5,3,7,2,8,9]
print(linsearch(arr,2))