# A = [10, 16, 8, 12, 15, 6, 3, 9,5]
A = [16, 4, 2, 1, 17, 3]

def swap(a, b):
        temp = A[a]
        A[a] = A[b]
        A[b] = temp

def partition(i, j):

    pivot = i
    # i = 0
    # j = len(A)-1

    while(i < j):        
        while(A[i] <= A[pivot]):
            i+=1
        while(A[j] > A[pivot]):
            j-=1
#swap elements
        if (i<j):
            swap(i, j)

    swap(pivot, j)
    return j 

def quick_sort(i, j=len(A)-1):
    
    if (i < j):
        div = partition(i, j)
        quick_sort(i, div)
        quick_sort(div+1, j)
    else:
        return

print(A)
quick_sort(0)
print(A)