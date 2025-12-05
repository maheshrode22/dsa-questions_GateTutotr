import java.util.*;

class MaxHeap {
    private ArrayList<Integer> heap;
    
    public MaxHeap() {
        heap = new ArrayList<>();
    }
    
    public void insert(int val) {
        heap.add(val);
        heapifyUp(heap.size() - 1);
    }
    
    private void heapifyUp(int idx) {
        if (idx == 0) return;
        int parent = (idx - 1) / 2;
        if (heap.get(idx) > heap.get(parent)) {
            Collections.swap(heap, idx, parent);
            heapifyUp(parent);
        }
    }
    
    public Integer deleteMax() {
        if (heap.isEmpty()) return null;
        int maxVal = heap.get(0);
        heap.set(0, heap.get(heap.size() - 1));
        heap.remove(heap.size() - 1);
        int idx = 0;
        while (idx < heap.size()) {
            int largest = idx;
            int left = 2 * idx + 1;
            int right = 2 * idx + 2;
            
            if (left < heap.size() && heap.get(left) > heap.get(largest)) {
                largest = left;
            }
            if (right < heap.size() && heap.get(right) > heap.get(largest)) {
                largest = right;
            }
            
            if (largest == idx) break;
            Collections.swap(heap, idx, largest);
            idx = largest;
        }
        return maxVal;
    }
    
    public ArrayList<Integer> getHeap() {
        return heap;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        MaxHeap heap = new MaxHeap();
        for (int num : arr) heap.insert(num);
        Integer deleted = heap.deleteMax();
        ArrayList<Integer> remaining = heap.getHeap();
        System.out.println(deleted);
        if (remaining.isEmpty()) System.out.println("Heap is Empty");
        else {
            for (int i = 0; i < remaining.size(); i++) {
                System.out.print(remaining.get(i));
                if (i < remaining.size() - 1) System.out.print(" ");
            }
        }
    }
}

