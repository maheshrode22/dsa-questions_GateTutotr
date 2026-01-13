#!/usr/bin/env python3
"""Check for issues in problems 40-47"""
import json
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

folder_path = os.path.join("Data Structure", "20255", "Bit Manipulation")
issues_found = []

for i in range(40, 48):
    file_path = os.path.join(folder_path, f"{i}.json")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if "problems" not in data or len(data["problems"]) == 0:
            issues_found.append(f"{i}.json: Missing problems array")
            continue
            
        problem = data["problems"][0]
        
        # Check required fields
        required_fields = ["title", "description", "examples", "constraints", "testCases", "starterCodes", "subdomainId"]
        for field in required_fields:
            if field not in problem:
                issues_found.append(f"{i}.json: Missing field '{field}'")
        
        # Check subdomainId
        if problem.get("subdomainId") != 6033:
            issues_found.append(f"{i}.json: Wrong subdomainId (got {problem.get('subdomainId')}, expected 6033)")
        
        # Check title format
        if "(Bit Manipulation)" not in problem.get("title", ""):
            issues_found.append(f"{i}.json: Title missing '(Bit Manipulation)' suffix")
        
        # Check test cases
        if "testCases" in problem:
            if len(problem["testCases"]) != 5:
                issues_found.append(f"{i}.json: Expected 5 test cases, got {len(problem['testCases'])}")
            
            for j, tc in enumerate(problem["testCases"]):
                if "input" not in tc or "expectedOutput" not in tc:
                    issues_found.append(f"{i}.json: Test case {j+1} missing input or expectedOutput")
        
        # Check starter codes
        if "starterCodes" in problem:
            if len(problem["starterCodes"]) != 5:
                issues_found.append(f"{i}.json: Expected 5 starter codes, got {len(problem['starterCodes'])}")
            
            languages = [1, 2, 3, 4, 5]  # Python, Java, JavaScript, C++, C
            found_languages = [sc.get("language") for sc in problem["starterCodes"]]
            for lang in languages:
                if lang not in found_languages:
                    issues_found.append(f"{i}.json: Missing starter code for language {lang}")
            
            for sc in problem["starterCodes"]:
                if "code" not in sc or "TODO" not in sc.get("code", ""):
                    issues_found.append(f"{i}.json: Starter code missing TODO comment")
        
        print(f"OK {i}.json: {problem.get('title', 'Unknown')}")
        
    except json.JSONDecodeError as e:
        issues_found.append(f"{i}.json: JSON decode error - {e}")
    except Exception as e:
        issues_found.append(f"{i}.json: Error - {e}")

print("\n" + "="*50)
if issues_found:
    print("ISSUES FOUND:")
    for issue in issues_found:
        print(f"  - {issue}")
else:
    print("No issues found! All files are correct.")
print("="*50)

