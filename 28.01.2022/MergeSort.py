#Function to implement Merge Sort
def merge(tempList, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = tempList[left+i]

    for j in range(0, n2):
        R[j] = tempList[middle+1+j]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            tempList[k] = L[i]
            i += 1
        else:
            tempList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        tempList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        tempList[k] = R[j]
        j += 1
        k += 1


def mergeSort(tempList, left, right):
    if left < right:
        middle = (left+(right-1))//2
        mergeSort(tempList, left, middle)
        mergeSort(tempList, middle+1, right)
        merge(tempList, left, middle, right)
    return tempList

unsortedList = [6, 2, 8, 4, 10]
print(mergeSort(unsortedList, 0, 4))
