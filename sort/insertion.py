A = []

"INSERTION SORT"

print("Enter a list of number to be sorted. Enter 0 to quit input and start sorting")
x = 1
while(x != "0"):
    x = input("Enter a number = ")
    A.append(int(x))
    print(A)

print("\n")

for i in range(1,len(A)):
    marker = i
    checker = i-1
    print("Checker = " + str(checker) + " Marker = " + str(marker) + "\n")
    while (checker>=0):
        if(A[checker] > A[marker]):
            temp = A[checker]
            A[checker] = A[marker]
            A[marker] = temp

        checker -= 1
        marker -= 1
    print("Iteration " + str(i) + " = " + str(A))

print("Sorted result = " + str(A))
