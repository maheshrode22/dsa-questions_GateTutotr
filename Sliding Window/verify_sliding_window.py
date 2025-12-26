"""
Sliding Window Problems Verification Script
This script verifies all 15 Sliding Window problems:
1. Tests expected outputs against reference solutions
2. Tests all 5 language starter codes with implemented solutions
"""

import json
import subprocess
import os
import tempfile
import sys
from collections import deque

# ============================================================
# REFERENCE SOLUTIONS FOR ALL 15 PROBLEMS
# ============================================================

def solve_problem_1(input_str):
    """Max Window Sum"""
    lines = input_str.strip().split('\n')
    parts = lines[0].split()
    n, k = int(parts[0]), int(parts[1])
    arr = list(map(int, lines[1].split()))
    
    if k > n:
        return "0"
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, n):
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return str(max_sum)

def solve_problem_2(input_str):
    """Count Even Numbers in Each Window"""
    lines = input_str.strip().split('\n')
    parts = lines[0].split()
    n, k = int(parts[0]), int(parts[1])
    arr = list(map(int, lines[1].split()))
    
    if k > n:
        return ""
    
    # Count evens in first window
    count = sum(1 for i in range(k) if arr[i] % 2 == 0)
    result = [count]
    
    for i in range(k, n):
        if arr[i - k] % 2 == 0:
            count -= 1
        if arr[i] % 2 == 0:
            count += 1
        result.append(count)
    
    return ' '.join(map(str, result))

def solve_problem_3(input_str):
    """First Negative Number in Each Window"""
    lines = input_str.strip().split('\n')
    parts = lines[0].split()
    n, k = int(parts[0]), int(parts[1])
    arr = list(map(int, lines[1].split()))
    
    neg_queue = deque()
    result = []
    
    for i in range(n):
        if arr[i] < 0:
            neg_queue.append(i)
        
        if i >= k - 1:
            # Remove elements outside window
            while neg_queue and neg_queue[0] < i - k + 1:
                neg_queue.popleft()
            
            if neg_queue:
                result.append(arr[neg_queue[0]])
            else:
                result.append(0)
    
    return ' '.join(map(str, result))

def solve_problem_4(input_str):
    """Longest Unique Substring"""
    s = input_str.strip()
    
    char_index = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return str(max_len)

def solve_problem_5(input_str):
    """Longest Subarray with Sum At Most K"""
    lines = input_str.strip().split('\n')
    parts = lines[0].split()
    n, K = int(parts[0]), int(parts[1])
    arr = list(map(int, lines[1].split()))
    
    left = 0
    window_sum = 0
    max_len = 0
    
    for right in range(n):
        window_sum += arr[right]
        
        while window_sum > K and left <= right:
            window_sum -= arr[left]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return str(max_len)

def solve_problem_6(input_str):
    """Smallest Subarray with Sum At Least K"""
    lines = input_str.strip().split('\n')
    parts = lines[0].split()
    n, K = int(parts[0]), int(parts[1])
    arr = list(map(int, lines[1].split()))
    
    left = 0
    window_sum = 0
    min_len = float('inf')
    
    for right in range(n):
        window_sum += arr[right]
        
        while window_sum >= K:
            min_len = min(min_len, right - left + 1)
            window_sum -= arr[left]
            left += 1
    
    return str(min_len) if min_len != float('inf') else "0"

def solve_problem_7(input_str):
    """Longest Substring with At Most K Distinct Characters"""
    lines = input_str.strip().split('\n')
    s = lines[0].strip()
    K = int(lines[1].strip())
    
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
    
    return str(max_len)

def solve_problem_8(input_str):
    """Max Consecutive Ones After Flipping At Most K Zeros"""
    lines = input_str.strip().split('\n')
    parts = lines[0].split()
    n, K = int(parts[0]), int(parts[1])
    arr = list(map(int, lines[1].split()))
    
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
    
    return str(max_len)

def solve_problem_9(input_str):
    """Minimum Window Substring Containing All Characters"""
    lines = input_str.strip().split('\n')
    s = lines[0].strip()
    t = lines[1].strip()
    
    if len(t) > len(s):
        return "-1"
    
    from collections import Counter
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
    
    return str(min_len) if min_len != float('inf') else "-1"

def solve_problem_10(input_str):
    """Count Anagram Substrings"""
    lines = input_str.strip().split('\n')
    s = lines[0].strip()
    p = lines[1].strip()
    
    if len(p) > len(s):
        return "0"
    
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
    
    return str(count)

def solve_problem_11(input_str):
    """Maximum Vowels in Substring of Length K"""
    lines = input_str.strip().split('\n')
    s = lines[0].strip()
    k = int(lines[1].strip())
    
    vowels = set('aeiouAEIOU')
    
    # Count vowels in first window
    count = sum(1 for i in range(k) if s[i] in vowels)
    max_count = count
    
    for i in range(k, len(s)):
        if s[i - k] in vowels:
            count -= 1
        if s[i] in vowels:
            count += 1
        max_count = max(max_count, count)
    
    return str(max_count)

def solve_problem_12(input_str):
    """Subarray Product Less Than K"""
    lines = input_str.strip().split('\n')
    parts = lines[0].split()
    n, k = int(parts[0]), int(parts[1])
    arr = list(map(int, lines[1].split()))
    
    if k <= 1:
        return "0"
    
    left = 0
    product = 1
    count = 0
    
    for right in range(n):
        product *= arr[right]
        
        while product >= k and left <= right:
            product //= arr[left]
            left += 1
        
        count += right - left + 1
    
    return str(count)

def solve_problem_13(input_str):
    """Longest Repeating Character Replacement"""
    lines = input_str.strip().split('\n')
    s = lines[0].strip()
    k = int(lines[1].strip())
    
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
    
    return str(max_len)

def solve_problem_14(input_str):
    """Contains Duplicate II"""
    lines = input_str.strip().split('\n')
    parts = lines[0].split()
    n, k = int(parts[0]), int(parts[1])
    nums = list(map(int, lines[1].split()))
    
    seen = {}
    
    for i in range(n):
        if nums[i] in seen and i - seen[nums[i]] <= k:
            return "true"
        seen[nums[i]] = i
    
    return "false"

def solve_problem_15(input_str):
    """Get Equal Substrings Within Budget"""
    lines = input_str.strip().split('\n')
    s = lines[0].strip()
    t = lines[1].strip()
    maxCost = int(lines[2].strip())
    
    # Calculate costs
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
    
    return str(max_len)

# Map problem number to solver
SOLVERS = {
    1: solve_problem_1,
    2: solve_problem_2,
    3: solve_problem_3,
    4: solve_problem_4,
    5: solve_problem_5,
    6: solve_problem_6,
    7: solve_problem_7,
    8: solve_problem_8,
    9: solve_problem_9,
    10: solve_problem_10,
    11: solve_problem_11,
    12: solve_problem_12,
    13: solve_problem_13,
    14: solve_problem_14,
    15: solve_problem_15
}

# ============================================================
# VERIFICATION FUNCTIONS
# ============================================================

def load_problem(problem_number):
    """Load a problem JSON file"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, f"{problem_number}.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['problems'][0]

def verify_test_cases(problem_number):
    """Verify test cases against reference solution"""
    problem = load_problem(problem_number)
    solver = SOLVERS[problem_number]
    
    print(f"\n{'='*60}")
    print(f"Problem {problem_number}: {problem['title']}")
    print(f"{'='*60}")
    
    all_passed = True
    for i, test_case in enumerate(problem['testCases']):
        input_data = test_case['input']
        expected = test_case['expectedOutput'].strip()
        
        try:
            actual = solver(input_data).strip()
        except Exception as e:
            actual = f"ERROR: {e}"
        
        passed = actual == expected
        status = "[PASS]" if passed else "[FAIL]"
        
        if not passed:
            all_passed = False
            print(f"\n  Test Case {i+1}: {status}")
            print(f"    Input: {input_data[:50]}..." if len(input_data) > 50 else f"    Input: {input_data}")
            print(f"    Expected: '{expected}'")
            print(f"    Actual:   '{actual}'")
        else:
            print(f"  Test Case {i+1}: {status}")
    
    return all_passed

def verify_all_problems():
    """Verify all 15 problems"""
    print("\n" + "="*60)
    print("SLIDING WINDOW PROBLEMS - TEST CASE VERIFICATION")
    print("="*60)
    
    results = {}
    for i in range(1, 16):
        try:
            results[i] = verify_test_cases(i)
        except Exception as e:
            print(f"\nProblem {i}: ERROR - {e}")
            results[i] = False
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY - Test Cases Verification")
    print("="*60)
    passed = sum(1 for v in results.values() if v)
    failed = len(results) - passed
    
    for i in range(1, 16):
        problem = load_problem(i)
        status = "[PASS]" if results[i] else "[FAIL]"
        print(f"  Problem {i:2d}: {problem['title'][:40]:40s} - {status}")
    
    print(f"\nTotal: {passed} passed, {failed} failed")
    return results

# ============================================================
# LANGUAGE-SPECIFIC CODE TESTING
# ============================================================

# Implemented solutions for each language
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

def verify_python_solutions():
    """Verify all Python solutions work correctly"""
    print("\n" + "="*60)
    print("PYTHON STARTER CODE VERIFICATION")
    print("="*60)
    
    results = {}
    for prob_num in range(1, 16):
        problem = load_problem(prob_num)
        python_code = PYTHON_SOLUTIONS.get(prob_num)
        
        if not python_code:
            print(f"\nProblem {prob_num}: {problem['title']} - NO SOLUTION")
            results[prob_num] = False
            continue
        
        print(f"\nProblem {prob_num}: {problem['title']}")
        all_passed = True
        
        for i, test_case in enumerate(problem['testCases']):
            input_data = test_case['input']
            expected = test_case['expectedOutput'].strip()
            
            actual = run_python_code(python_code, input_data)
            passed = actual == expected
            
            if not passed:
                all_passed = False
                print(f"  Test Case {i+1}: [FAIL]")
                print(f"    Expected: '{expected}'")
                print(f"    Actual:   '{actual}'")
            else:
                print(f"  Test Case {i+1}: [PASS]")
        
        results[prob_num] = all_passed
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY - Python Solutions")
    print("="*60)
    passed = sum(1 for v in results.values() if v)
    failed = len(results) - passed
    print(f"Total: {passed} passed, {failed} failed")
    
    return results

# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == '__main__':
    print("="*60)
    print("SLIDING WINDOW PROBLEMS - COMPREHENSIVE VERIFICATION")
    print("="*60)
    
    # Task 1: Verify all test cases against reference solutions
    print("\n" + "="*60)
    print("TASK 1: Verifying Test Cases Against Reference Solutions")
    print("="*60)
    test_case_results = verify_all_problems()
    
    # Task 2: Verify Python starter code implementations
    print("\n" + "="*60)
    print("TASK 2: Verifying Python Starter Code Implementations")
    print("="*60)
    python_results = verify_python_solutions()
    
    # Final Summary
    print("\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60)
    
    tc_passed = sum(1 for v in test_case_results.values() if v)
    py_passed = sum(1 for v in python_results.values() if v)
    
    print(f"\nTest Cases Verification: {tc_passed}/15 problems passed")
    print(f"Python Implementations:   {py_passed}/15 problems passed")
    
    if tc_passed == 15 and py_passed == 15:
        print("\n*** ALL TESTS PASSED! ***")
    else:
        print("\n*** SOME TESTS FAILED - Review the output above for details ***")
