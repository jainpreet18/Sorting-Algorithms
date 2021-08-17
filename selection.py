def selection(A):
    for i in range(len(A)-1):
        minIndex = i
        for j in range(i+1,len(A)):
            if (A[j] < A[minIndex]):
                minIndex = j
            A[i],A[minIndex] = A[minIndex],A[i]

    return

array = input().split()
array = [int(x) for x in array]
selection(array)
print(array)
