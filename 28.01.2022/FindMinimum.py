def divideAndConquer_Min(arr, ind, len):
	minimum = 0;
	if (ind >= len - 2):
		if (arr[ind] < arr[ind + 1]):
			return arr[ind];
		else:
			return arr[ind + 1];

	minimum = divideAndConquer_Min(arr, ind + 1, len);

	if (arr[ind] < minimum):
		return arr[ind];
	else:
		return minimum;

print(divideAndConquer_Min([1,2,4,5,6,32,64,23,0,4,45],0,11))