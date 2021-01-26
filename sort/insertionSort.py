# A = []

"INSERTION SORT"


class Plugin:
    def __init__(self, *args, **kwargs):
        print("sortType: ", args)

    def Sort(self, A):
        for i in range(1,len(A)):
            marker = i
            checker = i-1
            # print("Checker = " + str(checker) + " Marker = " + str(marker) + "\n")
            while (checker>=0):
                if(A[checker] > A[marker]):
                    temp = A[checker]
                    A[checker] = A[marker]
                    A[marker] = temp

                checker -= 1
                marker -= 1
        # print("Iteration " + str(i) + " = " + str(A))

    # print("Sorted result = " + str(A))
    
