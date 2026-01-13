import json

def audit_json(file_path):
    print(f"--- Auditing {file_path} ---")
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    problems = data.get('problems', [])
    if len(problems) != 5:
        print(f"Error: Expected 5 problems, found {len(problems)}")
    
    for i, p in enumerate(problems):
        title = p.get('title', 'No Title')
        print(f"Problem {i+1}: {title}")
        
        # Check subdomainId
        if p.get('subdomainId') != 2019:
            print(f"  - Warning: subdomainId is {p.get('subdomainId')}, expected 2019")
            
        # Check test cases count
        test_cases = p.get('testCases', [])
        if len(test_cases) < 5:
            print(f"  - Error: Only {len(test_cases)} test cases found")
            
        # Check starter codes
        starter_codes = p.get('starterCodes', [])
        languages = [sc.get('language') for sc in starter_codes]
        expected_langs = [1, 2, 3, 4, 5]
        for lang in expected_langs:
            if lang not in languages:
                print(f"  - Error: Missing starter code for language {lang}")
                
        # Check for placeholder text
        desc = p.get('description', '')
        if "TODO" in desc or "..." in desc:
            print(f"  - Warning: Potential placeholder in description")
            
        # Check test case consistency
        for j, tc in enumerate(test_cases):
            if not tc.get('input') or not tc.get('expectedOutput'):
                print(f"  - Error: Test case {j+1} is missing input or expectedOutput")

audit_json(r'd:\gatetutor\all Q\Data Structure\2019\new-5-problems.json')
audit_json(r'd:\gatetutor\all Q\Data Structure\2019\new-5-problems-part2.json')
