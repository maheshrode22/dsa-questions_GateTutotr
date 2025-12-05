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
    
    def deleteMax(self):
        if not self.heap:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        idx = 0
        while idx < len(self.heap):
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            
            if largest == idx:
                break
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest
        return max_val
    
    def getHeap(self):
        return self.heap

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    heap = MaxHeap()
    for num in arr:
        heap.insert(num)
    deleted = heap.deleteMax()
    remaining = heap.getHeap()
    print(deleted)
    if not remaining:
        print("Heap is Empty")
    else:
        print(" ".join(map(str, remaining)))

if __name__ == '__main__':
    solve()

