def quicksort(A, start, end):
    if start<end:
        pivot = partition(A, start, end)
        quicksort(A, start, pivot-1)
        quicksort(A, pivot+1, end)
    return

def partition(A, start, end):

    pivot = A[end]
    pIndex = start

    for i in range(start,end):
        if (A[i] <= pivot):
            A[i],A[pIndex] = A[pIndex],A[i]
            pIndex +=1
    A[pIndex],A[end] = A[end],A[pIndex]
    return pIndex


arr = input().split()
arr = [int(x) for x in arr]
quicksort(arr,0,len(arr)-1)
print(arr)
