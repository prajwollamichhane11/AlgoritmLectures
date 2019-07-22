def insort(arr):
	for i in range(1,len(arr)):
		j = i-1

		while j >= 0 and arr[j] > arr[i] :
			arr[j],arr[j+1] = arr[j+1],arr[j]
			j = j - 1
			i = i - 1
	return arr

arr = [2,1,87,342,8,42,21]
print(insort(arr))