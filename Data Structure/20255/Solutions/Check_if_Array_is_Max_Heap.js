class Solution {
    isMaxHeap(arr) {
        const n = arr.length;
        for (let i = 0; i < n; i++) {
            const left = 2 * i + 1;
            const right = 2 * i + 2;
            
            if (left < n && arr[i] < arr[left]) {
                return false;
            }
            if (right < n && arr[i] < arr[right]) {
                return false;
            }
        }
        return true;
    }
}

function solve(input) {
    const lines = input.trim().split("\n");
    const n = parseInt(lines[0]);
    const arr = lines[1].split(" ").map(Number);
    const sol = new Solution();
    const result = sol.isMaxHeap(arr);
    if (result) console.log("YES");
    else console.log("NO");
}

const fs = require('fs');
solve(fs.readFileSync(0, 'utf-8'));




