def insertion(A):
    for i in range(1,len(A)):
        hole = i
        value = A[i]
        while(hole>0 and A[hole-1]>value):
            A[hole] = A[hole-1]
            hole -=1
        A[hole] = value
    return A



numbers = input()
array = numbers.split()
array = [int(x) for x in array]
print(array)
sorted = insertion(array)
print(sorted)
