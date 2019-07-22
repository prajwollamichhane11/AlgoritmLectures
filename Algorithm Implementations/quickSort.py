def partition(arr,low,high):
    i = low
    pivot = arr[low]

    for j in range(low+1 , high):

        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i],arr[low] = arr[low],arr[i]
    return ( i )

def quickSort(arr,low,high):

    if low < high:
        pi = partition(arr,low,high)

        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


if __name__ == '__main__':
    arr = list(input())
    n = len(arr)

    quickSort(arr,0,n-1)
    for i in range(n):
        if arr[i] != ' ':
            print(arr[i],end=' ')
