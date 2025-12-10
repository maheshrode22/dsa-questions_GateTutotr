import json
import os
import sys

# Define the directory and files to check
DIR = r"d:\gatetutor\all Q\Arrays"
FILES = [
    "Delete_Element_At_Position.json",
    "Majority_Element.json",
    "Rotate_Array_By_N.json",
    "Smallest_Missing_Element.json",
    "Sort_Array_Asc_Desc.json"
]

def solve_delete_element(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    if n == 0: return ""
    arr = list(map(int, lines[1].strip().split()))
    pos = int(lines[2])
    
    if 0 <= pos < len(arr):
        arr.pop(pos)
    
    return " ".join(map(str, arr))

def solve_majority_element(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    if n == 0: return "There are no Majority Elements in the given array"
    arr = list(map(int, lines[1].strip().split()))
    
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    
    for x in arr:
        if counts[x] > n / 2:
            return str(x)
            
    return "There are no Majority Elements in the given array"

def solve_rotate_array(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    if n == 0: return ""
    arr = list(map(int, lines[1].strip().split()))
    n_rot = int(lines[2])
    
    n_rot = n_rot % n # Handle rotation larger than size
    rotated = arr[n_rot:] + arr[:n_rot]
    return " ".join(map(str, rotated))

def solve_smallest_missing(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    if n == 0: return "0"
    arr = list(map(int, lines[1].strip().split()))
    
    missing = 0
    for x in arr:
        if x == missing:
            missing += 1
        elif x > missing:
            break
    return str(missing)

def solve_sort_array(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    if n == 0: return ""
    arr = list(map(int, lines[1].strip().split()))
    
    asc = sorted(arr)
    desc = sorted(arr, reverse=True)
    
    return " ".join(map(str, asc)) + "\n" + " ".join(map(str, desc))

SOLVERS = {
    "Delete_Element_At_Position.json": solve_delete_element,
    "Majority_Element.json": solve_majority_element,
    "Rotate_Array_By_N.json": solve_rotate_array,
    "Smallest_Missing_Element.json": solve_smallest_missing,
    "Sort_Array_Asc_Desc.json": solve_sort_array
}

def verify_file(filename):
    path = os.path.join(DIR, filename)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"FAILED to load {filename}: {e}")
        return

    problems = data.get('problems', [])
    if not problems:
        print(f"NO PROBLEMS found in {filename}")
        return

    problem = problems[0]
    print(f"Verifying {filename}: {problem['title']}")
    
    solver = SOLVERS.get(filename)
    if not solver:
        print(f"NO SOLVER defined for {filename}")
        return

    test_cases = problem.get('testCases', [])
    all_passed = True
    
    for i, tc in enumerate(test_cases):
        inp = tc['input']
        exp = tc['expectedOutput'].strip()
        
        try:
            act = solver(inp).strip()
        except Exception as e:
            print(f"  TestCase {i+1}: ERROR - {e}")
            all_passed = False
            continue
            
        if act == exp:
            print(f"  TestCase {i+1}: PASS")
        else:
            print(f"  TestCase {i+1}: FAIL")
            print(f"    Input:\n{inp}")
            print(f"    Expected:\n{exp}")
            print(f"    Actual:\n{act}")
            all_passed = False

    if all_passed:
        print(f"SUCCESS: All test cases passed for {filename}\n")
    else:
        print(f"FAILURE: Some test cases failed for {filename}\n")

if __name__ == "__main__":
    for f in FILES:
        verify_file(f)
