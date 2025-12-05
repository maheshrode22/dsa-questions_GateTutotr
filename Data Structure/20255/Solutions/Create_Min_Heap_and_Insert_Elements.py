class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._heapify_up(parent)
    
    def getHeap(self):
        return self.heap

class Solution:
    def createMinHeap(self, arr):
        heap = MinHeap()
        for num in arr:
            heap.insert(num)
        return heap.getHeap()

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    sol = Solution()
    result = sol.createMinHeap(arr)
    
    if not result:
        print("Heap is Empty")
    else:
        print(" ".join(map(str, result)))

if __name__ == '__main__':
    solve()

