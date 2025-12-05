class Solution:
    def findMaximum(self, arr):
        if not arr or len(arr) == 0:
            return None
        max_val = arr[0]
        for num in arr:
            if num > max_val:
                max_val = num
        return max_val

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    sol = Solution()
    result = sol.findMaximum(arr)
    
    if result is None:
        print("Array is Empty")
    else:
        print(result)

if __name__ == '__main__':
    solve()

