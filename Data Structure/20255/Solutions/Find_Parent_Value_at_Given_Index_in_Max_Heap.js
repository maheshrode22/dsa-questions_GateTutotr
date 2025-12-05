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
    
    findParent(index) {
        if (index === 0) return -1;
        if (index < 0 || index >= this.heap.length) return -1;
        const parentIdx = Math.floor((index - 1) / 2);
        return this.heap[parentIdx];
    }
    
    getHeap() {
        return this.heap;
    }
}

function solve(input) {
    const lines = input.trim().split("\n");
    const n = parseInt(lines[0]);
    const arr = lines[1].split(" ").map(Number);
    const index = parseInt(lines[2]);
    const heap = new MaxHeap();
    for (let num of arr) heap.insert(num);
    const result = heap.findParent(index);
    console.log(result);
}

const fs = require('fs');
solve(fs.readFileSync(0, 'utf-8'));

