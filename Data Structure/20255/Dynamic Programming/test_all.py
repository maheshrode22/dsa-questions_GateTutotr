"""
Complete Test Suite for Dynamic Programming Problems
Tests all 15 problems with reference solutions matching starter code format
"""
import json
import os

# ============ REFERENCE SOLUTIONS ============

# P1: Fibonacci Number
class Solution1:
    def fibonacci(self, n):
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# P2: Climbing Stairs
class Solution2:
    def climbStairs(self, n):
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# P3: House Robber
class Solution3:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

# P4: Maximum Subarray Sum (Kadane's)
class Solution4:
    def maxSubArray(self, nums):
        current_max = global_max = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            global_max = max(global_max, current_max)
        return global_max

# P5: Minimum Cost Climbing Stairs
class Solution5:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])

# P6: 0/1 Knapsack
class Solution6:
    def knapsack(self, items, capacity):
        n = len(items)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            v, w = items[i-1]
            for j in range(capacity + 1):
                dp[i][j] = dp[i-1][j]
                if j >= w:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)
        return dp[n][capacity]

# P7: Longest Common Subsequence
class Solution7:
    def lcs(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

# P8: Coin Change - Minimum Coins
class Solution8:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i and dp[i-c] != float('inf'):
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# P9: Longest Increasing Subsequence
class Solution9:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# P10: Unique Paths
class Solution10:
    def uniquePaths(self, m, n):
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

# P11: Edit Distance
class Solution11:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[m][n]

# P12: Longest Palindromic Subsequence
class Solution12:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

# P13: Matrix Chain Multiplication
class Solution13:
    def matrixChainOrder(self, p):
        n = len(p) - 1
        if n == 1:
            return 0
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                    dp[i][j] = min(dp[i][j], cost)
        return dp[0][n-1]

# P14: Partition Equal Subset Sum
class Solution14:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]

# P15: Shortest Common Supersequence
class Solution15:
    def shortestCommonSupersequence(self, s1, s2):
        m, n = len(s1), len(s2)
        # LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        lcs_len = dp[m][n]
        return m + n - lcs_len


# ============ INPUT PARSER (Matching Starter Code) ============

def parse_input(problem_num, input_str):
    """Parse input according to starter code format for each problem"""
    lines = input_str.strip().split('\n')
    
    if problem_num == 1:
        n = int(lines[0])
        return (n,)
    
    elif problem_num == 2:
        n = int(lines[0])
        return (n,)
    
    elif problem_num == 3:
        n = int(lines[0])
        nums = list(map(int, lines[1].split()))
        return (nums,)
    
    elif problem_num == 4:
        n = int(lines[0])
        nums = list(map(int, lines[1].split()))
        return (nums,)
    
    elif problem_num == 5:
        n = int(lines[0])
        cost = list(map(int, lines[1].split()))
        return (cost,)
    
    elif problem_num == 6:
        n, capacity = map(int, lines[0].split())
        items = []
        for i in range(1, n + 1):
            v, w = map(int, lines[i].split())
            items.append((v, w))
        return (items, capacity)
    
    elif problem_num == 7:
        s1 = lines[0]
        s2 = lines[1]
        return (s1, s2)
    
    elif problem_num == 8:
        n, amount = map(int, lines[0].split())
        coins = list(map(int, lines[1].split()))
        return (coins, amount)
    
    elif problem_num == 9:
        n = int(lines[0])
        nums = list(map(int, lines[1].split()))
        return (nums,)
    
    elif problem_num == 10:
        m, n = map(int, lines[0].split())
        return (m, n)
    
    elif problem_num == 11:
        word1 = lines[0] if len(lines) > 0 else ""
        word2 = lines[1] if len(lines) > 1 else ""
        return (word1, word2)
    
    elif problem_num == 12:
        s = lines[0]
        return (s,)
    
    elif problem_num == 13:
        n = int(lines[0])
        p = list(map(int, lines[1].split()))
        return (p,)
    
    elif problem_num == 14:
        n = int(lines[0])
        nums = list(map(int, lines[1].split()))
        return (nums,)
    
    elif problem_num == 15:
        s1 = lines[0]
        s2 = lines[1]
        return (s1, s2)


def run_solution(problem_num, args):
    """Run the solution for a given problem number"""
    if problem_num == 1:
        sol = Solution1()
        return str(sol.fibonacci(*args))
    elif problem_num == 2:
        sol = Solution2()
        return str(sol.climbStairs(*args))
    elif problem_num == 3:
        sol = Solution3()
        return str(sol.rob(*args))
    elif problem_num == 4:
        sol = Solution4()
        return str(sol.maxSubArray(*args))
    elif problem_num == 5:
        sol = Solution5()
        return str(sol.minCostClimbingStairs(*args))
    elif problem_num == 6:
        sol = Solution6()
        return str(sol.knapsack(*args))
    elif problem_num == 7:
        sol = Solution7()
        return str(sol.lcs(*args))
    elif problem_num == 8:
        sol = Solution8()
        return str(sol.coinChange(*args))
    elif problem_num == 9:
        sol = Solution9()
        return str(sol.lengthOfLIS(*args))
    elif problem_num == 10:
        sol = Solution10()
        return str(sol.uniquePaths(*args))
    elif problem_num == 11:
        sol = Solution11()
        return str(sol.minDistance(*args))
    elif problem_num == 12:
        sol = Solution12()
        return str(sol.longestPalindromeSubseq(*args))
    elif problem_num == 13:
        sol = Solution13()
        return str(sol.matrixChainOrder(*args))
    elif problem_num == 14:
        sol = Solution14()
        result = sol.canPartition(*args)
        return "YES" if result else "NO"
    elif problem_num == 15:
        sol = Solution15()
        return str(sol.shortestCommonSupersequence(*args))


# ============ MAIN TEST RUNNER ============

def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 60)
    print("DYNAMIC PROGRAMMING - COMPLETE TEST SUITE")
    print("=" * 60)
    print()
    
    total_tests = 0
    passed_tests = 0
    failed_problems = []
    
    for i in range(1, 16):
        filepath = os.path.join(folder, f'{i}.json')
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            problem = data['problems'][0]
            title = problem['title']
            test_cases = problem['testCases']
            
            problem_passed = True
            results = []
            
            for tc_idx, tc in enumerate(test_cases):
                total_tests += 1
                input_str = tc['input']
                expected = tc['expectedOutput']
                
                try:
                    args = parse_input(i, input_str)
                    actual = run_solution(i, args)
                    
                    if actual == expected:
                        passed_tests += 1
                        results.append(f"TC{tc_idx+1}:✓")
                    else:
                        problem_passed = False
                        results.append(f"TC{tc_idx+1}:✗({actual}!={expected})")
                except Exception as e:
                    problem_passed = False
                    results.append(f"TC{tc_idx+1}:ERR({str(e)[:20]})")
            
            status = "PASS" if problem_passed else "FAIL"
            if not problem_passed:
                failed_problems.append(i)
            
            diff_map = {1: 'Easy', 2: 'Medium', 3: 'Hard'}
            diff = diff_map.get(problem['difficulty'], '?')
            
            print(f"P{i:2d} [{diff:6s}] {title[:35]:35s} {status}")
            print(f"    {' '.join(results)}")
            
        except Exception as e:
            print(f"P{i:2d} ERROR: {str(e)}")
            failed_problems.append(i)
    
    print()
    print("=" * 60)
    print(f"RESULTS: {passed_tests}/{total_tests} tests passed")
    
    if failed_problems:
        print(f"FAILED PROBLEMS: {failed_problems}")
    else:
        print("ALL PROBLEMS PASSED! ✓")
    print("=" * 60)


if __name__ == '__main__':
    main()
