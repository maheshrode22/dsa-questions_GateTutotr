import json
import os
import sys
import subprocess
import tempfile

# Solutions map: filename -> replacement code for the Solution class method
solutions = {
    "1.json": """
    def isPalindrome(self, S):
        return "True" if S == S[::-1] else "False"
""",
    "2.json": """
    def isAnagram(self, S1, S2):
        return "True" if sorted(S1) == sorted(S2) else "False"
""",
    "3.json": """
    def KMP(self, T, P):
        if not P: return []
        lps = [0] * len(P)
        length = 0
        i = 1
        while i < len(P):
            if P[i] == P[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        res = []
        i = 0
        j = 0
        while i < len(T):
            if P[j] == T[i]:
                i += 1
                j += 1
            if j == len(P):
                res.append(i - j)
                j = lps[j - 1]
            elif i < len(T) and P[j] != T[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return res if res else [-1]
""",
    "4.json": """
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1
""",
    "5.json": """
    def lengthOfLongestSubstring(self, S):
        char_map = {}
        left = 0
        max_len = 0
        for right in range(len(S)):
            if S[right] in char_map:
                left = max(left, char_map[S[right]] + 1)
            char_map[S[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len
""",
    "6.json": """
    def rabinKarp(self, T, P):
        # Using standard find for verification simplicity as it's functionally equivalent for correctness
        res = []
        start = 0
        while True:
            idx = T.find(P, start)
            if idx == -1:
                break
            res.append(idx)
            start = idx + 1
        return res if res else [-1]
""",
    "7.json": """
    def longestPalindrome(self, S):
        if not S: return ""
        start = 0
        end = 0
        for i in range(len(S)):
            len1 = self.expandAroundCenter(S, i, i)
            len2 = self.expandAroundCenter(S, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return S[start:end+1]
    
    def expandAroundCenter(self, s, left, right):
        L, R = left, right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1
""",
    "8.json": """
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())
""",
    "9.json": """
    def zAlgorithm(self, T, P):
        # Using standard find for verification simplicity
        res = []
        start = 0
        while True:
            idx = T.find(P, start)
            if idx == -1:
                break
            res.append(idx)
            start = idx + 1
        return res if res else [-1]
""",
    "10.json": """
    def minWindow(self, S, T):
        from collections import Counter
        if not T or not S: return ""
        dict_t = Counter(T)
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        while r < len(S):
            character = S[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = S[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else S[ans[1] : ans[2] + 1]
"""
}

def verify_file(filepath):
    filename = os.path.basename(filepath)
    print(f"Verifying {filename}...")
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    problem = data['problems'][0]
    python_starter = next(sc for sc in problem['starterCodes'] if sc['language'] == 1)
    original_code = python_starter['code']
    
    # Inject solution
    # We look for the method definition and replace the body or the whole class
    # A simple way is to replace "class Solution:\n    def method(...):\n        pass" 
    # But regex is safer. Or just replacing the class definition.
    
    # For simplicity in this specific context, we know the structure.
    # We will replace the entire "class Solution:... pass" block with our solution class.
    # However, the starter code has `class Solution:\n    def name(self, args):\n        # TODO\n        pass`
    
    # Let's just append the solution method to the class or overwrite the class.
    # Actually, we can just replace the text `pass` with the body, but indentation is tricky.
    # Strategy: Replace "class Solution:" up to "if __name__" with our class.
    
    split_marker = "if __name__ == '__main__':"
    if split_marker not in original_code:
        print(f"Error: Could not find main block in {filename}")
        return False
        
    boilerplate = original_code.split(split_marker)[1]
    
    # Construct new code
    solution_body = solutions.get(filename)
    if not solution_body:
        print(f"No solution defined for {filename}")
        return False
        
    new_code = f"class Solution:{solution_body}\n\n{split_marker}{boilerplate}"
    
    all_passed = True
    for i, tc in enumerate(problem['testCases']):
        input_str = tc['input']
        expected = tc['expectedOutput'].strip()
        
        # Run code
        try:
            process = subprocess.Popen(
                [sys.executable, "-c", new_code],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(input=input_str)
            
            actual = stdout.strip()
            
            # Normalization for comparison (ignore trailing whitespace differences)
            # For list outputs, we might need more robust comparison, but let's try direct string first
            # The boilerplate usually prints space-separated values.
            
            if actual == expected:
                print(f"  Test Case {i+1}: PASS")
            else:
                # Special handling for Group Anagrams where order might differ if not fully controlled
                # But our boilerplate sorts it.
                print(f"  Test Case {i+1}: FAIL")
                print(f"    Input: {input_str}")
                print(f"    Expected: {expected}")
                print(f"    Actual:   {actual}")
                print(f"    Stderr:   {stderr}")
                all_passed = False
        except Exception as e:
            print(f"  Test Case {i+1}: ERROR {e}")
            all_passed = False
            
    return all_passed

def main():
    directory = r"d:\gatetutor\all Q\Data Structure\20255\String Algorithms"
    files = [f for f in os.listdir(directory) if f.endswith('.json') and f != 'verify_problems.py']
    
    # Sort numerically
    files.sort(key=lambda x: int(x.split('.')[0]))
    
    results = {}
    for f in files:
        results[f] = verify_file(os.path.join(directory, f))
        print("-" * 20)
        
    print("\nSummary:")
    for f, passed in results.items():
        status = "PASSED" if passed else "FAILED"
        print(f"{f}: {status}")

if __name__ == "__main__":
    main()
