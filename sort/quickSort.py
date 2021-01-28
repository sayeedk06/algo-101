"QUICK SORT"
class Plugin:
    def __init__(self, *args, **kwargs):
        print("Sort type: ", args)
    
    def swap(self, a, b, A):
        self.temp = A[a]
        A[a] = A[b]
        A[b] = self.temp

    def partition(self,i, j, A):
        self.pivot = i

        while (i < j):
            while (A[i] <= A[self.pivot]):
                i+=1
            while (A[j] > A[self.pivot]):
                j-=1
    # swap elements
            if (i<j):
                self.swap(i, j, A)
        self.swap(self.pivot, j, A)
        return j

    def quick_sort(self,i, j,A):
        
        if (i < j):
            div = self.partition(i, j,A)
            self.quick_sort(i, div,A)
            self.quick_sort(div+1, j, A)

    def Sort(self, A):
        j = len(A)-1
        self.quick_sort(0, j,A)