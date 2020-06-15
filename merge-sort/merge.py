
A = [1,6,7,8,4,20,44,30]

""" MERGE SORT """

def merge_sort(A):
    print(A)
    n = len(A)
    if(n<2):
        return A
    else:
        mid = int(n/2)
        print("Mid = " + str(mid))
        left = []
        right = []
        for i in range(0,mid):
            # print("i = " + str(i))
            left.append(A[i])
        for i in range(mid,n):
            right.append(A[i])
        print("Left = " + str(left))
        print("right = " + str(right))
        merge_sort(left)
        merge_sort(right)






merge_sort(A)
