import json
import os

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr: return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

def verify_problem(file_path, sort_func):
    with open(file_path, 'r') as f:
        data = json.load(f)
        problem = data['problems'][0]
        print(f"Verifying {problem['title']}...")
        for i, tc in enumerate(problem['testCases']):
            input_lines = tc['input'].split('\n')
            if len(input_lines) < 2:
                # Handle single element or empty
                if not input_lines[0].strip():
                    arr = []
                else:
                    # Maybe just N? No, usually N then array.
                    # If only 1 line, it might be N=1 and the array is on the same line or missing.
                    # But our test cases are N \n array.
                    arr = []
            else:
                arr = list(map(int, input_lines[1].split()))
            
            expected = list(map(int, tc['expectedOutput'].split()))
            actual = sort_func(arr.copy())
            
            if actual == expected:
                print(f"  Test Case {i+1}: PASSED")
            else:
                print(f"  Test Case {i+1}: FAILED")
                print(f"    Input: {arr}")
                print(f"    Expected: {expected}")
                print(f"    Actual:   {actual}")
                return False
    return True

base_path = 'd:/gatetutor/all Q/2016/'
problems = [
    ('2016-sort-1.json', bubble_sort),
    ('2016-sort-2.json', selection_sort),
    ('2016-sort-3.json', insertion_sort),
    ('2016-sort-4.json', shell_sort),
    ('2016-sort-5.json', quick_sort),
    ('2016-sort-6.json', radix_sort)
]

all_passed = True
for file_name, func in problems:
    if not verify_problem(os.path.join(base_path, file_name), func):
        all_passed = False

if all_passed:
    print("\nAll sorting problems verified successfully!")
else:
    print("\nSome problems failed verification.")
