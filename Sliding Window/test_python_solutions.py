"""
Complete Language Starter Code Verification
Tests all 15 problems with Python implementations
"""
import json
import subprocess
import os
import tempfile
import sys
from collections import deque, Counter

def load_problem(num):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, f"{num}.json"), 'r', encoding='utf-8') as f:
        return json.load(f)['problems'][0]

# Complete Python implementations for all 15 problems
PYTHON_SOLUTIONS = {
1: '''class Solution:
    def maxWindowSum(self, arr, n, k):
        if k > n:
            return 0
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(k, n):
            window_sum = window_sum + arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum

if __name__ == '__main__':
    n_k = input().split()
    n = int(n_k[0])
    k = int(n_k[1])
    arr = list(map(int, input().split()))
    sol = Solution()
    print(sol.maxWindowSum(arr, n, k))''',

2: '''from collections import deque

class Solution:
    def countEvenInWindows(self, arr, n, k):
        if k > n:
            return []
        count = sum(1 for i in range(k) if arr[i] % 2 == 0)
        result = [count]
        for i in range(k, n):
            if arr[i - k] % 2 == 0:
                count -= 1
            if arr[i] % 2 == 0:
                count += 1
            result.append(count)
        return result

if __name__ == '__main__':
    n_k = input().split()
    n = int(n_k[0])
    k = int(n_k[1])
    arr = list(map(int, input().split()))
    sol = Solution()
    res = sol.countEvenInWindows(arr, n, k)
    print(' '.join(map(str, res))) if res else print('', end='')''',

3: '''from collections import deque

class Solution:
    def firstNegativeInWindows(self, arr, n, k):
        neg_queue = deque()
        result = []
        for i in range(n):
            if arr[i] < 0:
                neg_queue.append(i)
            if i >= k - 1:
                while neg_queue and neg_queue[0] < i - k + 1:
                    neg_queue.popleft()
                if neg_queue:
                    result.append(arr[neg_queue[0]])
                else:
                    result.append(0)
        return result

if __name__ == '__main__':
    n_k = input().split()
    n = int(n_k[0])
    k = int(n_k[1])
    arr = list(map(int, input().split()))
    sol = Solution()
    res = sol.firstNegativeInWindows(arr, n, k)
    print(' '.join(map(str, res)))''',

4: '''class Solution:
    def lengthOfLongestUniqueSubstring(self, s):
        char_index = {}
        max_len = 0
        left = 0
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == '__main__':
    s = input().strip()
    sol = Solution()
    print(sol.lengthOfLongestUniqueSubstring(s))''',

5: '''class Solution:
    def longestSubarrayAtMostK(self, arr, n, K):
        left = 0
        window_sum = 0
        max_len = 0
        for right in range(n):
            window_sum += arr[right]
            while window_sum > K and left <= right:
                window_sum -= arr[left]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == '__main__':
    n_K = input().split()
    n = int(n_K[0])
    K = int(n_K[1])
    arr = list(map(int, input().split()))
    sol = Solution()
    print(sol.longestSubarrayAtMostK(arr, n, K))''',

6: '''class Solution:
    def smallestSubarrayAtLeastK(self, arr, n, K):
        left = 0
        window_sum = 0
        min_len = float('inf')
        for right in range(n):
            window_sum += arr[right]
            while window_sum >= K:
                min_len = min(min_len, right - left + 1)
                window_sum -= arr[left]
                left += 1
        return min_len if min_len != float('inf') else 0

if __name__ == '__main__':
    n_K = input().split()
    n = int(n_K[0])
    K = int(n_K[1])
    arr = list(map(int, input().split()))
    sol = Solution()
    print(sol.smallestSubarrayAtLeastK(arr, n, K))''',

7: '''class Solution:
    def longestSubstringAtMostKDistinct(self, s, K):
        char_count = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            while len(char_count) > K:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == '__main__':
    s = input().strip()
    K = int(input().strip())
    sol = Solution()
    print(sol.longestSubstringAtMostKDistinct(s, K))''',

8: '''class Solution:
    def maxConsecutiveOnesAfterFlips(self, arr, n, K):
        left = 0
        zero_count = 0
        max_len = 0
        for right in range(n):
            if arr[right] == 0:
                zero_count += 1
            while zero_count > K:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == '__main__':
    n_K = input().split()
    n = int(n_K[0])
    K = int(n_K[1])
    arr = list(map(int, input().split()))
    sol = Solution()
    print(sol.maxConsecutiveOnesAfterFlips(arr, n, K))''',

9: '''from collections import Counter

class Solution:
    def minWindowLength(self, s, t):
        if len(t) > len(s):
            return -1
        t_count = Counter(t)
        required = len(t_count)
        formed = 0
        window_counts = {}
        left = 0
        min_len = float('inf')
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                    formed -= 1
                left += 1
        return min_len if min_len != float('inf') else -1

if __name__ == '__main__':
    s = input().strip()
    t = input().strip()
    sol = Solution()
    print(sol.minWindowLength(s, t))''',

10: '''class Solution:
    def countAnagramSubstrings(self, s, p):
        if len(p) > len(s):
            return 0
        p_count = [0] * 26
        s_count = [0] * 26
        for c in p:
            p_count[ord(c) - ord('a')] += 1
        count = 0
        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            if i >= len(p) - 1 and s_count == p_count:
                count += 1
        return count

if __name__ == '__main__':
    s = input().strip()
    p = input().strip()
    sol = Solution()
    print(sol.countAnagramSubstrings(s, p))''',

11: '''class Solution:
    def maxVowels(self, s, k):
        vowels = set('aeiouAEIOU')
        count = sum(1 for i in range(k) if s[i] in vowels)
        max_count = count
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            max_count = max(max_count, count)
        return max_count

if __name__ == '__main__':
    s = input().strip()
    try:
        k = int(input().strip())
        sol = Solution()
        print(sol.maxVowels(s, k))
    except:
        pass''',

12: '''class Solution:
    def numSubarrayProductLessThanK(self, arr, n, k):
        if k <= 1:
            return 0
        left = 0
        product = 1
        count = 0
        for right in range(n):
            product *= arr[right]
            while product >= k and left <= right:
                product //= arr[left]
                left += 1
            count += right - left + 1
        return count

if __name__ == '__main__':
    try:
        line1 = input().split()
        n = int(line1[0])
        k = int(line1[1])
        arr = list(map(int, input().split()))
        sol = Solution()
        print(sol.numSubarrayProductLessThanK(arr, n, k))
    except:
        pass''',

13: '''class Solution:
    def characterReplacement(self, s, k):
        count = [0] * 26
        left = 0
        max_count = 0
        max_len = 0
        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            max_count = max(max_count, count[idx])
            while right - left + 1 - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == '__main__':
    s = input().strip()
    try:
        k = int(input().strip())
        sol = Solution()
        print(sol.characterReplacement(s, k))
    except:
        pass''',

14: '''class Solution:
    def containsNearbyDuplicate(self, nums, n, k):
        seen = {}
        for i in range(n):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
        return False

if __name__ == '__main__':
    try:
        line1 = input().split()
        n = int(line1[0])
        k = int(line1[1])
        nums = list(map(int, input().split()))
        sol = Solution()
        if sol.containsNearbyDuplicate(nums, n, k):
            print("true")
        else:
            print("false")
    except:
        pass''',

15: '''class Solution:
    def equalSubstring(self, s, t, maxCost):
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        left = 0
        current_cost = 0
        max_len = 0
        for right in range(len(costs)):
            current_cost += costs[right]
            while current_cost > maxCost and left <= right:
                current_cost -= costs[left]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == '__main__':
    s = input().strip()
    t = input().strip()
    try:
        maxCost = int(input().strip())
        sol = Solution()
        print(sol.equalSubstring(s, t, maxCost))
    except:
        pass'''
}

def run_python_code(code, input_data):
    """Run Python code with given input"""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code)
            temp_file = f.name
        
        result = subprocess.run(
            [sys.executable, temp_file],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        os.unlink(temp_file)
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as e:
        return f"ERROR: {e}"

def main():
    print("="*60)
    print("PYTHON STARTER CODE VERIFICATION - ALL 15 PROBLEMS")
    print("="*60)
    
    all_results = {}
    
    for prob_num in range(1, 16):
        problem = load_problem(prob_num)
        python_code = PYTHON_SOLUTIONS.get(prob_num)
        
        if not python_code:
            print(f"\nProblem {prob_num}: {problem['title']} - NO SOLUTION")
            all_results[prob_num] = False
            continue
        
        print(f"\nProblem {prob_num}: {problem['title']}")
        all_passed = True
        
        for i, test_case in enumerate(problem['testCases']):
            input_data = test_case['input']
            expected = test_case['expectedOutput'].strip()
            
            actual = run_python_code(python_code, input_data)
            passed = actual == expected
            
            status = "[PASS]" if passed else "[FAIL]"
            if not passed:
                all_passed = False
                print(f"  TC {i+1}: {status} Expected='{expected}' Actual='{actual}'")
            else:
                print(f"  TC {i+1}: {status}")
        
        all_results[prob_num] = all_passed
    
    # Summary
    print("\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60)
    
    passed = sum(1 for v in all_results.values() if v)
    failed = len(all_results) - passed
    
    for i in range(1, 16):
        problem = load_problem(i)
        status = "[PASS]" if all_results.get(i, False) else "[FAIL]"
        print(f"  Problem {i:2d}: {problem['title'][:40]:40s} {status}")
    
    print(f"\nTotal: {passed}/15 problems passed")
    
    if passed == 15:
        print("\n*** ALL PYTHON IMPLEMENTATIONS VERIFIED! ***")
    else:
        print(f"\n*** {failed} PROBLEMS NEED ATTENTION ***")

if __name__ == '__main__':
    main()
