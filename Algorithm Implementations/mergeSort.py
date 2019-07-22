def merge(left,right,arr):
	i = 0
	j = 0
	k = 0

	while (i<len(left) and j<len(right)):
		if(left[i] < right[j]):
			arr[k] = left[i]
			i = i + 1
		else:
			arr[k] = right[j]
			j = j + 1

		k = k + 1

	while (i<len(left)):
		arr[k] = left[i]
		i = i + 1
		k = k +1

	while (j < len(right)):
		arr[k] = right[j]
		j = j + 1
		k = k + 1

	return arr


def mersort(arr):
	n = len(arr)
	if (n<2):
		return

	mid = n//2
	left = arr[:mid]
	right = arr[mid:]

	mersort(left)
	mersort(right)

	merge(left,right,arr)

	return arr


print(mersort(arr))
