def SelectionSort(A):
    if len(A) > 1:
        m = 0
        for i in range (1,len(A)):
            if A[i] < A[m]:
                m = i
        A[0],A[m] = A[m],A[0]
        A = [A[0]]+SelectionSort(A[1:])
    return A

arr = list(map(int,input().split()))

print(SelectionSort(arr))
