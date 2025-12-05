class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._heapify_up(parent)
    
    def findParent(self, index):
        if index == 0:
            return -1
        if index < 0 or index >= len(self.heap):
            return -1
        parent_idx = (index - 1) // 2
        return self.heap[parent_idx]
    
    def getHeap(self):
        return self.heap

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    index = int(input())
    heap = MaxHeap()
    for num in arr:
        heap.insert(num)
    result = heap.findParent(index)
    print(result)

if __name__ == '__main__':
    solve()

