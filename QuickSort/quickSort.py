A = [5, 10, 1, 3, 7, 18, 2]

def quicksort(A):

    pivot = 0
    i = 0
    j = len(A)-1

    while(A[i] <= A[pivot]):
        i+=1
    while(A[j] > A[pivot]):
        j-=1

#swap elements
    if (i < j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
    else:
        temp = A[j]
        A[j] = A[pivot]
        A[pivot] = temp

print(A)
quicksort(A)
print(A)