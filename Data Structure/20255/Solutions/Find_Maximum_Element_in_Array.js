class Solution{
  findMaximum(arr){
    if(!arr || arr.length === 0) return null;
    let max = arr[0];
    for(let i = 1; i < arr.length; i++){
      if(arr[i] > max) max = arr[i];
    }
    return max;
  }
}
function solve(input){
  const lines = input.trim().split("\n");
  const n = parseInt(lines[0]);
  const arr = lines[1].split(" ").map(Number);
  const sol = new Solution();
  const ans = sol.findMaximum(arr);
  if(ans === null || ans === undefined) console.log("Array is Empty");
  else console.log(ans);
}
const fs = require('fs');
solve(fs.readFileSync(0, 'utf-8'));

