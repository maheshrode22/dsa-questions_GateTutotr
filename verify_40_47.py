import json
import os

folder = os.path.join("Data Structure", "20255", "Bit Manipulation")
all_ok = True

for i in range(40, 48):
    file_path = os.path.join(folder, f"{i}.json")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        problem = data["problems"][0]
        tc_count = len(problem["testCases"])
        sc_count = len(problem["starterCodes"])
        title = problem["title"]
        
        issues = []
        if tc_count != 5:
            issues.append(f"Expected 5 test cases, got {tc_count}")
        if sc_count != 5:
            issues.append(f"Expected 5 starter codes, got {sc_count}")
        if "(Bit Manipulation)" not in title:
            issues.append("Title missing suffix")
        if problem.get("subdomainId") != 6033:
            issues.append(f"Wrong subdomainId: {problem.get('subdomainId')}")
        
        if issues:
            print(f"{i}.json: {'; '.join(issues)}")
            all_ok = False
        else:
            print(f"OK {i}.json: {title} ({tc_count} test cases, {sc_count} starter codes)")

if all_ok:
    print("\nAll files are correct!")
else:
    print("\nSome issues found.")

