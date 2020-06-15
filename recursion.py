A = [1,6,7,8,4,20,44,30]

""" Recursion"""
"Here an array is divided in the middle recursively"

def recursion(A):
    print("\t" + str(A))
    n = len(A)
    if(n<2):
        print("\treturn = " + str(A))
        return A
    else:
        mid = int(n/2)
        print("\t\tMid = " + str(mid))
        left = []
        right = []
        for i in range(0,mid):
            left.append(A[i])
        for i in range(mid,n):
            right.append(A[i])
        print("\tLeft = " + str(left))
        print("\t\t\tright = " + str(right))
        recursion(left)
        recursion(right)






recursion(A)
