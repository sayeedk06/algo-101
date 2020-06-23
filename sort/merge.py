# A = []

"MERGE SORT"


def merge(left,right,sorted):
    nL = len(left)
    nR = len(right)

    left_index = 0
    right_index = 0
    sort_index = 0

    while(left_index < nL and right_index < nR):
        if (left[left_index] < right[right_index]):
            sorted[sort_index] = left[left_index]
            sort_index += 1
            left_index += 1
        else:
            sorted[sort_index] = right[right_index]
            sort_index += 1
            right_index += 1
    while(left_index < nL):
        sorted[sort_index] = left[left_index]
        sort_index += 1
        left_index += 1
    while(right_index < nR):
        sorted[sort_index] = right[right_index]
        sort_index += 1
        right_index += 1






def merge_sort(A):
    # print(A)
    n = len(A)
    if(n<2):
        return A
    else:
        mid = int(n/2)
        left = []
        right = []
        for i in range(0,mid):

            left.append(A[i])
        for i in range(mid,n):
            right.append(A[i])

        merge_sort(left)
        merge_sort(right)
        merge(left, right,A)





# print("Unsorted = " + str(A))
# merge_sort(A)
# print("Sorted = " + str(A))
