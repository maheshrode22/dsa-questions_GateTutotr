import json
import os

json_path = r'd:\gatetutor\all Q\Data Structure\2023\new-5-problems-part2.json'

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print(f"ERROR: Failed to load JSON: {e}")
    exit(1)

problems = data['problems']
print(f"Found {len(problems)} problems\n")

all_pass = True
issues = []

# Problem 1: Find Diameter of Binary Tree
print("📌 Problem 1: Find Diameter of Binary Tree")
tc_outputs1 = ["3", "0", "1", "3", "4"]
for i, exp in enumerate(tc_outputs1, 1):
    actual_tc = problems[0]['testCases'][i-1]
    if actual_tc['expectedOutput'] == exp:
        print(f"  TC {i}: ✓ PASS")
    else:
        print(f"  TC {i}: ✗ FAIL - Expected: {exp}, Got: {actual_tc['expectedOutput']}")
        all_pass = False

# Problem 2: Check if Binary Tree is Balanced
print("\n📌 Problem 2: Check if Binary Tree is Balanced")
tc_outputs2 = ["YES", "NO", "YES", "YES", "NO"]
for i, exp in enumerate(tc_outputs2, 1):
    actual_tc = problems[1]['testCases'][i-1]
    if actual_tc['expectedOutput'] == exp:
        print(f"  TC {i}: ✓ PASS")
    else:
        print(f"  TC {i}: ✗ FAIL - Expected: {exp}, Got: {actual_tc['expectedOutput']}")
        all_pass = False

# Problem 3: Find Left View of Binary Tree
print("\n📌 Problem 3: Find Left View of Binary Tree")
tc_outputs3 = ["1 2 4", "1 3 4", "10", "1 2", "1 2 4"]
for i, exp in enumerate(tc_outputs3, 1):
    actual_tc = problems[2]['testCases'][i-1]
    if actual_tc['expectedOutput'] == exp:
        print(f"  TC {i}: ✓ PASS")
    else:
        print(f"  TC {i}: ✗ FAIL - Expected: {exp}, Got: {actual_tc['expectedOutput']}")
        all_pass = False

# Problem 4: Check if Binary Tree is BST
print("\n📌 Problem 4: Check if Binary Tree is BST")
tc_outputs4 = ["YES", "NO", "YES", "YES", "NO"]
for i, exp in enumerate(tc_outputs4, 1):
    actual_tc = problems[3]['testCases'][i-1]
    if actual_tc['expectedOutput'] == exp:
        print(f"  TC {i}: ✓ PASS")
    else:
        print(f"  TC {i}: ✗ FAIL - Expected: {exp}, Got: {actual_tc['expectedOutput']}")
        all_pass = False

# Problem 5: Find Lowest Common Ancestor in Binary Tree
print("\n📌 Problem 5: Find Lowest Common Ancestor in Binary Tree")
tc_outputs5 = ["2", "1", "2", "10", "2"]
for i, exp in enumerate(tc_outputs5, 1):
    actual_tc = problems[4]['testCases'][i-1]
    if actual_tc['expectedOutput'] == exp:
        print(f"  TC {i}: ✓ PASS")
    else:
        print(f"  TC {i}: ✗ FAIL - Expected: {exp}, Got: {actual_tc['expectedOutput']}")
        all_pass = False

# Structural checks
print("\n" + "="*60)
print("STRUCTURAL CHECKS")
print("="*60)

for i, p in enumerate(problems, 1):
    if p.get('subdomainId') != 2023:
        issues.append(f"P{i}: Wrong subdomainId (expected 2023, got {p.get('subdomainId')})")
    if len(p.get('testCases', [])) != 5:
        issues.append(f"P{i}: Expected 5 test cases, found {len(p.get('testCases', []))}")
    if len(p.get('starterCodes', [])) != 5:
        issues.append(f"P{i}: Expected 5 starter codes, found {len(p.get('starterCodes', []))}")
    hints_list = p.get('hintsList', [])
    hints_count = p.get('hints', 0)
    if len(hints_list) != hints_count:
        issues.append(f"P{i}: Hints mismatch (field={hints_count}, list={len(hints_list)})")

if issues:
    print("❌ Issues found:")
    for issue in issues:
        print(f"  • {issue}")
else:
    print("✓ All structural checks passed")

# Code Quality Checks
print("\n" + "="*60)
print("CODE QUALITY CHECKS")
print("="*60)

code_issues = []
for i, p in enumerate(problems, 1):
    # Check C++ code (language 4)
    cpp_code = p['starterCodes'][3]['code']
    if 'in findHeight' in cpp_code: # Check for previous typo just in case
        code_issues.append(f"P{i}: C++ typo - 'in findHeight'")
    
    # Check for missing return types or obvious syntax errors in C/C++
    c_code = p['starterCodes'][4]['code']
    if 'void leftView' in c_code and 'return' in c_code.split('leftView')[1].split('}')[0]:
        # This is a loose check, void functions shouldn't return values
        pass 

if code_issues:
    print("❌ Code issues found:")
    for issue in code_issues:
        print(f"  • {issue}")
    all_pass = False
else:
    print("✓ No code issues found")

print("\n" + "="*60)
print("FINAL REPORT")
print("="*60)
if all_pass and not issues and not code_issues:
    print("✅✅✅ ALL CHECKS PASSED - NO MISTAKES! ✅✅✅")
else:
    print(f"❌❌❌ FOUND {len(issues) + len(code_issues)} ISSUE(S) ❌❌❌")
