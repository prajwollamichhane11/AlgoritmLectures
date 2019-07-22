def binsearch(arr,n):
        first = 0
        last = len(arr)-1
        found = 0

        while first<last and found == 0:
                midpoint=(first+last)//2
                if arr[midpoint] == n:
                        found = midpoint
                        break
                else:
                        if n<arr[midpoint]:
                                first = first
                                last = midpoint-1
                        else:
                                first = midpoint+1
                                last = last
        return found

arr = [0,2,4,7,9,10,14,17]
print(linsearch(arr,0))
