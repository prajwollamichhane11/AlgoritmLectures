def selsort(arr):
	for i in range(0,len(arr)-1):
		min = i
		for j in range(i+1,len(arr)):
			if arr[j] < arr[min]:
				min = j
		if min != i:
			arr[i],arr[min] = arr[min],arr[i]
	return arr
print(selsort(arr))