class Solution:
    def binary_search(self, v:int, L:list):
        v = int(v)
        left, right = 0, len(L)-1
        while left <= right:
            mid = (left+right)//2
            if L[mid] == v:
                return mid
            elif L[mid]<v:
                left = mid+1
            else:
                right = mid-1
        return (-1)