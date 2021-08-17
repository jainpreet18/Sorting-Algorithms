def bubble(A):
    for i in range(1,len(A)):
        flag = 0
        for j in range(len(A)-i):
            if A[j+1]<A[j]:
                A[j],A[j+1]= A[j+1],A[j]
                flag =1
        if flag==0: break
    return

array = input().split()
array = [int(x) for x in array]
bubble(array)
print(array)
