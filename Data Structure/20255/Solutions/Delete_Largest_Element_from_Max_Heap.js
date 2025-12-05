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
    
    deleteMax() {
        if (this.heap.length === 0) return null;
        const maxVal = this.heap[0];
        this.heap[0] = this.heap[this.heap.length - 1];
        this.heap.pop();
        let idx = 0;
        while (idx < this.heap.length) {
            let largest = idx;
            const left = 2 * idx + 1;
            const right = 2 * idx + 2;
            
            if (left < this.heap.length && this.heap[left] > this.heap[largest]) {
                largest = left;
            }
            if (right < this.heap.length && this.heap[right] > this.heap[largest]) {
                largest = right;
            }
            
            if (largest === idx) break;
            [this.heap[idx], this.heap[largest]] = [this.heap[largest], this.heap[idx]];
            idx = largest;
        }
        return maxVal;
    }
    
    getHeap() {
        return this.heap;
    }
}

function solve(input) {
    const lines = input.trim().split("\n");
    const n = parseInt(lines[0]);
    const arr = lines[1].split(" ").map(Number);
    const heap = new MaxHeap();
    for (let num of arr) heap.insert(num);
    const deleted = heap.deleteMax();
    const remaining = heap.getHeap();
    console.log(deleted);
    if (remaining.length === 0) console.log("Heap is Empty");
    else console.log(remaining.join(" "));
}

const fs = require('fs');
solve(fs.readFileSync(0, 'utf-8'));

