class MaxHeap {
    constructor() {
        this.heap = [];
    }
    
    insert(val) {
        this.heap.push(val);
        this.heapifyUp(this.heap.length - 1);
    }
    
    heapifyUp(idx) {
        if (idx === 0) return;
        const parent = Math.floor((idx - 1) / 2);
        if (this.heap[idx] > this.heap[parent]) {
            [this.heap[idx], this.heap[parent]] = [this.heap[parent], this.heap[idx]];
            this.heapifyUp(parent);
        }
    }
    
    getHeap() {
        return this.heap;
    }
}

class Solution {
    createMaxHeap(arr) {
        const heap = new MaxHeap();
        for (let num of arr) {
            heap.insert(num);
        }
        return heap.getHeap();
    }
}

function solve(input) {
    const lines = input.trim().split("\n");
    const n = parseInt(lines[0]);
    const arr = lines[1].split(" ").map(Number);
    const sol = new Solution();
    const ans = sol.createMaxHeap(arr);
    if (ans.length === 0) console.log("Heap is Empty");
    else console.log(ans.join(" "));
}

const fs = require('fs');
solve(fs.readFileSync(0, 'utf-8'));

