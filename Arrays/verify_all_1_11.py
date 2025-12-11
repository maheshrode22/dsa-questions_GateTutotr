import json
import sys
from io import StringIO

# Solutions for all problems 1-11
def solution1_replaceNegative(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    print(' '.join(map(str, arr)))

def solution2_replaceDivisibleBy3(arr):
    for i in range(len(arr)):
        if arr[i] % 3 == 0:
            arr[i] = -1
    print(' '.join(map(str, arr)))

def solution3_replaceFirstLast(arr):
    if len(arr) > 0:
        arr[0] = 0
        arr[-1] = 0
    print(' '.join(map(str, arr)))

def solution4_replaceMultiplesOf5(arr):
    for i in range(len(arr)):
        if arr[i] % 5 == 0:
            arr[i] = 5
    print(' '.join(map(str, arr)))

def solution5_isPalindrome(arr):
    is_pal = arr == arr[::-1]
    print("true" if is_pal else "false")

def solution6_firstRepeating(arr):
    first_occurrence = {}
    repeating_elements = set()
    for i, num in enumerate(arr):
        if num in first_occurrence:
            repeating_elements.add(num)
        else:
            first_occurrence[num] = i
    if not repeating_elements:
        print("No repeating element")
    else:
        first_repeating = min(repeating_elements, key=lambda x: first_occurrence[x])
        print(f"First repeating element is {first_repeating}")

def solution7_calculateAverage(arr):
    total = sum(arr)
    average = total / len(arr)
    print(f"{average:.2f}")

def solution8_printGreaterThanX(arr, x):
    for num in arr:
        if num > x:
            print(num)

def solution9_createSquares(arr):
    squares = [num * num for num in arr]
    print(' '.join(map(str, squares)))

def solution10_printPairsWithSum(arr, target):
    n = len(arr)
    used = [False] * n
    for i in range(n):
        if used[i]:
            continue
        for j in range(i + 1, n):
            if used[j]:
                continue
            if arr[i] + arr[j] == target:
                print(f"({arr[i]}, {arr[j]})")
                used[i] = True
                used[j] = True
                break

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def solution11_replaceWithFactorial(arr):
    result = [factorial(num) for num in arr]
    print(' '.join(map(str, result)))

def parse_input(input_str, problem_num):
    lines = input_str.strip().split('\n')
    if problem_num in [7, 9, 11]:
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        return (arr,)
    elif problem_num in [8, 10]:
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        x = int(lines[2])
        return (arr, x)
    else:  # problems 1-6
        n = int(lines[0])
        if n > 0:
            arr = list(map(int, lines[1].split()))
        else:
            arr = []
        return (arr,)

def test_problem(json_file, problem_num, solution_func):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR reading {json_file}: {e}")
        return False
    
    problem = data['problems'][0]
    title = problem['title']
    test_cases = problem['testCases']
    starter_codes = problem.get('starterCodes', [])
    
    print(f"\n{'='*70}")
    print(f"Problem {problem_num}: {title}")
    print(f"{'='*70}")
    
    # Check starter codes
    print("\n[Starter Code Check]")
    languages = {1: 'Python', 2: 'Java', 3: 'JavaScript', 4: 'C++', 5: 'C'}
    starter_issues = []
    for sc in starter_codes:
        lang_id = sc.get('language')
        code = sc.get('code', '')
        lang_name = languages.get(lang_id, f'Lang{lang_id}')
        
        has_todo = 'TODO' in code.upper() or '# TODO' in code or '// TODO' in code
        has_input = False
        has_main = False
        
        if lang_id == 1:  # Python
            has_input = 'input()' in code or '__main__' in code
            has_main = '__main__' in code
        elif lang_id == 2:  # Java
            has_input = 'Scanner' in code or 'nextInt()' in code
            has_main = 'public static void main' in code
        elif lang_id == 3:  # JavaScript
            has_input = 'readFileSync' in code or 'input' in code
            has_main = 'solve(' in code
        elif lang_id == 4:  # C++
            has_input = 'cin' in code
            has_main = 'int main()' in code
        elif lang_id == 5:  # C
            has_input = 'scanf' in code
            has_main = 'int main()' in code
        
        if not has_todo:
            starter_issues.append(f"  - {lang_name}: Missing TODO comment")
        if not has_input:
            starter_issues.append(f"  - {lang_name}: Missing input reading")
        if not has_main:
            starter_issues.append(f"  - {lang_name}: Missing main function")
    
    if starter_issues:
        print("  ISSUES FOUND:")
        for issue in starter_issues:
            print(issue)
    else:
        print("  [OK] All starter codes have TODO comments and input reading")
    
    # Test all test cases
    print(f"\n[Test Cases Check] ({len(test_cases)} test cases)")
    all_passed = True
    
    for i, test_case in enumerate(test_cases, 1):
        input_str = test_case['input']
        expected_output = test_case['expectedOutput']
        
        try:
            args = parse_input(input_str, problem_num)
        except Exception as e:
            print(f"  Test {i}: PARSE ERROR - {e}")
            all_passed = False
            continue
        
        # Capture output
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            solution_func(*args)
            actual_output = captured_output.getvalue().strip()
        except Exception as e:
            actual_output = f"ERROR: {str(e)}"
        finally:
            sys.stdout = old_stdout
        
        # Compare outputs
        if actual_output == expected_output:
            print(f"  Test {i}: [PASSED]")
        else:
            print(f"  Test {i}: [FAILED]")
            print(f"    Input: {repr(input_str[:50])}")
            print(f"    Expected: {repr(expected_output)}")
            print(f"    Got:      {repr(actual_output)}")
            all_passed = False
    
    if all_passed and not starter_issues:
        print(f"\n[OK] Problem {problem_num}: ALL CHECKS PASSED")
    elif all_passed:
        print(f"\n[OK] Problem {problem_num}: All test cases passed (starter code issues noted)")
    else:
        print(f"\n[FAIL] Problem {problem_num}: SOME ISSUES FOUND")
    
    return all_passed and not starter_issues

if __name__ == '__main__':
    solutions = {
        1: solution1_replaceNegative,
        2: solution2_replaceDivisibleBy3,
        3: solution3_replaceFirstLast,
        4: solution4_replaceMultiplesOf5,
        5: solution5_isPalindrome,
        6: solution6_firstRepeating,
        7: solution7_calculateAverage,
        8: solution8_printGreaterThanX,
        9: solution9_createSquares,
        10: solution10_printPairsWithSum,
        11: solution11_replaceWithFactorial
    }
    
    all_problems_passed = True
    
    for i in range(1, 12):
        json_file = f"{i}.json"
        passed = test_problem(json_file, i, solutions[i])
        if not passed:
            all_problems_passed = False
    
    print(f"\n{'='*70}")
    print("FINAL SUMMARY")
    print(f"{'='*70}")
    if all_problems_passed:
        print("[SUCCESS] ALL PROBLEMS (1-11) ARE CORRECT!")
        print("  - All starter codes have TODO comments and input reading")
        print("  - All test cases pass correctly")
    else:
        print("[ISSUES] SOME PROBLEMS HAVE ISSUES")
        print("  Please review the output above for details")
    print(f"{'='*70}")

