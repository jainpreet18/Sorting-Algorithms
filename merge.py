def mergesort(A):

    n = len(A)

    if(n<2):
        return A

    mid = int(n/2)
    left = A[:mid]
    right = A[mid:]

    left = mergesort(left) 
    right = mergesort(right)
    A = merge(left,right,A)

    return A

def merge(L,R,A):
    i,j,k = 0,0,0

    while(i<len(L) and j<len(R)):
        if(L[i]<R[j]):
            A[k] = L[i]
            i +=1
        else:
            A[k] = R[j]
            j +=1
        k += 1

    while(i<len(L)):
        A[k] = L[i]
        i +=1
        k +=1

    while(j<len(R)):
        A[k] = R[j]
        j +=1
        k +=1

    return A



array = input().split()
array = [int(x) for x in array]
array = mergesort(array)
print(array)
