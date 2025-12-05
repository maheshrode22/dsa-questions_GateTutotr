class Solution:
    def isMaxHeap(self, arr):
        n = len(arr)
        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[i] < arr[left]:
                return False
            if right < n and arr[i] < arr[right]:
                return False
        return True

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    sol = Solution()
    result = sol.isMaxHeap(arr)
    if result:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()




