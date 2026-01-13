import json
import os

json_path = r'd:\gatetutor\all Q\Data Structure\2023\new-5-problems.json'

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

# Problem 1: Find Height of Binary Tree
print("📌 Problem 1: Find Height of Binary Tree")
tc_inputs = ["7\n1 2 3 4 5 -1 -1", "1\n10", "3\n1 2 -1", "5\n1 2 3 -1 4", "15\n1 2 3 4 5 6 7 8 -1 -1 -1 -1 -1 -1 -1"]
tc_outputs = ["2", "0", "1", "2", "3"]
for i, (inp, exp) in enumerate(zip(tc_inputs, tc_outputs), 1):
    actual_tc = problems[0]['testCases'][i-1]
    if actual_tc['input'] == inp and actual_tc['expectedOutput'] == exp:
        print(f"  TC {i}: ✓ PASS")
    else:
        print(f"  TC {i}: ✗ FAIL")
        all_pass = False

# Problem 2: Level Order Traversal
print("\n📌 Problem 2: Level Order Traversal of Binary Tree")
tc_outputs2 = ["1 2 3 4 5", "10", "1 2 3", "1 3 4", "1 2 3 4 6 7"]
for i, exp in enumerate(tc_outputs2, 1):
    actual_tc = problems[1]['testCases'][i-1]
    if actual_tc['expectedOutput'] == exp:
        print(f"  TC {i}: ✓ PASS")
    else:
        print(f"  TC {i}: ✗ FAIL - Expected: {exp}, Got: {actual_tc['expectedOutput']}")
        all_pass = False

# Problem 3: Check if Two Trees are Identical
print("\n📌 Problem 3: Check if Two Trees are Identical")
tc_outputs3 = ["YES", "NO", "YES", "NO", "YES"]
for i, exp in enumerate(tc_outputs3, 1):
    actual_tc = problems[2]['testCases'][i-1]
    if actual_tc['expectedOutput'] == exp:
        print(f"  TC {i}: ✓ PASS")
    else:
        print(f"  TC {i}: ✗ FAIL")
        all_pass = False

# Problem 4: Mirror a Binary Tree
print("\n📌 Problem 4: Mirror a Binary Tree")
tc_outputs4 = ["3 1 5 2 4", "10", "3 1 2", "1 2 3", "4 3 1"]
for i, exp in enumerate(tc_outputs4, 1):
    actual_tc = problems[3]['testCases'][i-1]
    if actual_tc['expectedOutput'] == exp:
        print(f"  TC {i}: ✓ PASS")
    else:
        print(f"  TC {i}: ✗ FAIL - Expected: {exp}, Got: {actual_tc['expectedOutput']}")
        all_pass = False

# Problem 5: Find Maximum Element
print("\n📌 Problem 5: Find Maximum Element in Binary Tree")
tc_outputs5 = ["5", "10", "100", "100", "-1"]
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

# Check for typo in C++ code (should be fixed now)
print("\n" + "="*60)
print("CODE QUALITY CHECKS")
print("="*60)

code_issues = []
for i, p in enumerate(problems, 1):
    cpp_code = p['starterCodes'][3]['code']
    if 'in findHeight' in cpp_code:
        code_issues.append(f"P{i}: C++ typo - 'in findHeight' should be 'int findHeight'")

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
