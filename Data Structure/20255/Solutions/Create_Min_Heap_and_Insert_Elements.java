import java.util.*;

class MinHeap {
    private ArrayList<Integer> heap;
    
    public MinHeap() {
        heap = new ArrayList<>();
    }
    
    public void insert(int val) {
        heap.add(val);
        heapifyUp(heap.size() - 1);
    }
    
    private void heapifyUp(int idx) {
        if (idx == 0) return;
        int parent = (idx - 1) / 2;
        if (heap.get(idx) < heap.get(parent)) {
            Collections.swap(heap, idx, parent);
            heapifyUp(parent);
        }
    }
    
    public ArrayList<Integer> getHeap() {
        return heap;
    }
}

class Solution {
    ArrayList<Integer> createMinHeap(int[] arr) {
        MinHeap heap = new MinHeap();
        for (int num : arr) {
            heap.insert(num);
        }
        return heap.getHeap();
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        Solution sol = new Solution();
        ArrayList<Integer> ans = sol.createMinHeap(arr);
        if (ans.isEmpty()) System.out.println("Heap is Empty");
        else {
            for (int i = 0; i < ans.size(); i++) {
                System.out.print(ans.get(i));
                if (i < ans.size() - 1) System.out.print(" ");
            }
        }
    }
}

