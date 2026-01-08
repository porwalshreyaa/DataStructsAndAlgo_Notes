class MinHeap:
    def __init__(self):
        self.arr = []
    def insert(self, value):
        self.arr.append(value) #suppose arr is empty rn
        n = len(self.arr)
        self._compare_parent_and_swap(n-1)
    def delete(self):
        n =len(self.arr)
        self.arr[0],self.arr[n-1]=self.arr[n-1],self.arr[0]
        self.arr.pop()
        self._compare_child_and_swap(0)
    def _compare_parent_and_swap(self, index):
        if index>0:
            p = (index-1)//2
            if self.arr[p] > self.arr[index]:
                self.arr[p], self.arr[index] = self.arr[index], self.arr[p]
            return self._compare_parent_and_swap(p)
        else:
            return
    def _compare_child_and_swap(self, index):
        n = len(self.arr)
        smallest = index
        l = 2*index +1
        r = 2*index +2
        if l<n and self.arr[l]<self.arr[smallest]:
            smallest=l
        if r<n and self.arr[r]<self.arr[smallest]:
            smallest=r
        if smallest != index:
            self.arr[index], self.arr[smallest]=self.arr[smallest], self.arr[index]
            self._compare_child_and_swap(smallest)
    def show(self):
        for i in self.arr:
            print(i)

# array = MinHeap()
# array.insert(4)
# array.insert(5)
# array.insert(1)
# array.insert(2)
# array.insert(3)
# array.insert(7)
# array.insert(12)
# array.show() # [1,2,4,5,3,7,12]
# print("after delete")
# array.delete()
# array.delete()
# array.show() 

# Heapify - parent to children but start from last
# for minimum

def BottomCompare(arr, ind):
    n = len(arr)
    smallest = ind
    l = ind*2 + 1
    r = ind*2 + 2
    if l < n and arr[l]<arr[smallest]:
        smallest=l
    if r < n and arr[r]<arr[smallest]:
        smallest=r
    if smallest!=ind:
        arr[smallest], arr[ind]=arr[ind], arr[smallest]
        BottomCompare(arr, smallest)

def heapify(arr):
    n = len(arr)
    if n<2:
        return arr
    currentIndex = n-1
    while currentIndex>=0:
        BottomCompare(arr,currentIndex)
        currentIndex-=1
    return arr

array2 = [5,2,0,1,9,100,4]

print(heapify(array2)) # [0,1,4,2,9,100,5]