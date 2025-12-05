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
    
    public int findParent(int index) {
        if (index == 0) return -1;
        if (index < 0 || index >= heap.size()) return -1;
        int parentIdx = (index - 1) / 2;
        return heap.get(parentIdx);
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
        int index = sc.nextInt();
        MaxHeap heap = new MaxHeap();
        for (int num : arr) heap.insert(num);
        int result = heap.findParent(index);
        System.out.println(result);
    }
}

