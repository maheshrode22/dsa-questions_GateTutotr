import json
import os
import math

def linear_search(arr, n, k):
    for i in range(n):
        if arr[i] == k:
            return i
    return -1

def binary_search_iterative(arr, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(arr, low, high, k):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == k:
        return mid
    elif arr[mid] < k:
        return binary_search_recursive(arr, mid + 1, high, k)
    else:
        return binary_search_recursive(arr, low, mid - 1, k)

def jump_search(arr, n, k):
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < k:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < k:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == k:
        return prev
    return -1

def interpolation_search(arr, n, k):
    low = 0
    high = n - 1
    while low <= high and k >= arr[low] and k <= arr[high]:
        if low == high:
            if arr[low] == k: return low
            return -1
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (k - arr[low])))
        if arr[pos] == k:
            return pos
        if arr[pos] < k:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def exponential_search(arr, n, k):
    if n == 0: return -1
    if arr[0] == k:
        return 0
    i = 1
    while i < n and arr[i] <= k:
        i = i * 2
    return binary_search_recursive(arr, i // 2, min(i, n - 1), k)

def verify_problem(file_path, search_func, is_recursive=False):
    with open(file_path, 'r') as f:
        data = json.load(f)
        problem = data['problems'][0]
        print(f"Verifying {problem['title']}...")
        for i, tc in enumerate(problem['testCases']):
            input_lines = tc['input'].split('\n')
            line1 = input_lines[0].split()
            n = int(line1[0])
            k = int(line1[1])
            arr = list(map(int, input_lines[1].split()))
            
            expected = int(tc['expectedOutput'].strip())
            if is_recursive:
                actual = search_func(arr, 0, n - 1, k)
            else:
                actual = search_func(arr, n, k)
            
            if actual == expected:
                print(f"  Test Case {i+1}: PASSED")
            else:
                print(f"  Test Case {i+1}: FAILED")
                print(f"    Input: {tc['input']!r}")
                print(f"    Expected: {expected}")
                print(f"    Actual:   {actual}")
                return False
    return True

base_path = 'd:/gatetutor/all Q/2017/'
problems = [
    ('2017-search-1.json', linear_search),
    ('2017-search-2.json', binary_search_iterative),
    ('2017-search-3.json', binary_search_recursive, True),
    ('2017-search-4.json', jump_search),
    ('2017-search-5.json', interpolation_search),
    ('2017-search-6.json', exponential_search)
]

all_passed = True
for p in problems:
    file_name = p[0]
    func = p[1]
    is_rec = p[2] if len(p) > 2 else False
    if not verify_problem(os.path.join(base_path, file_name), func, is_rec):
        all_passed = False

if all_passed:
    print("\nAll searching problems verified successfully!")
else:
    print("\nSome problems failed verification.")
