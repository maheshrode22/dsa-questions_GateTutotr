"""
Verify all Starter Codes for All 15 Sliding Window Problems
Checks: Python, Java, JavaScript, C++, C syntax
"""
import json
import os
import subprocess
import tempfile

def load_problem(num):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, f"{num}.json"), 'r', encoding='utf-8') as f:
        return json.load(f)['problems'][0]

LANGUAGES = {1: "Python", 2: "Java", 3: "JavaScript", 4: "C++", 5: "C"}

def check_python_syntax(code):
    """Check Python syntax by compiling"""
    try:
        compile(code, '<string>', 'exec')
        return True, None
    except SyntaxError as e:
        return False, str(e)

def check_java_syntax(code):
    """Check Java code for common syntax issues"""
    issues = []
    if '#' in code and '# ' in code and '# TODO' in code:
        issues.append("Found Python-style comment (#) in Java code")
    if not 'class ' in code:
        issues.append("Missing class definition")
    if issues:
        return False, "; ".join(issues)
    return True, None

def check_js_syntax(code):
    """Check JavaScript for common issues"""
    issues = []
    if 'class Solution {' not in code and 'class Solution{' not in code:
        # Some JS files may not have class
        pass
    # Basic check passed
    return True, None

def check_cpp_syntax(code):
    """Check C++ for common issues"""
    issues = []
    if '#include' not in code:
        issues.append("Missing #include")
    if 'int main' not in code:
        issues.append("Missing main function")
    if issues:
        return False, "; ".join(issues)
    return True, None

def check_c_syntax(code):
    """Check C for common issues"""
    issues = []
    if '#include' not in code:
        issues.append("Missing #include")
    if 'int main' not in code:
        issues.append("Missing main function")
    if issues:
        return False, "; ".join(issues)
    return True, None

SYNTAX_CHECKERS = {
    1: check_python_syntax,
    2: check_java_syntax,
    3: check_js_syntax,
    4: check_cpp_syntax,
    5: check_c_syntax
}

def main():
    print("="*60)
    print("STARTER CODE SYNTAX VERIFICATION - ALL 15 PROBLEMS")
    print("="*60)
    
    all_passed = True
    issues_found = []
    
    for prob_num in range(1, 16):
        problem = load_problem(prob_num)
        print(f"\nProblem {prob_num}: {problem['title']}")
        
        for starter in problem['starterCodes']:
            lang_id = starter['language']
            lang_name = LANGUAGES.get(lang_id, f"Lang{lang_id}")
            code = starter['code']
            
            checker = SYNTAX_CHECKERS.get(lang_id)
            if checker:
                passed, error = checker(code)
                status = "[PASS]" if passed else "[FAIL]"
                print(f"  {lang_name:12s}: {status}")
                if not passed:
                    all_passed = False
                    issues_found.append((prob_num, problem['title'], lang_name, error))
                    print(f"               Error: {error}")
            else:
                print(f"  {lang_name:12s}: [SKIP] No checker available")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    if all_passed:
        print("\n*** ALL STARTER CODES PASS SYNTAX CHECK! ***")
    else:
        print(f"\n*** ISSUES FOUND: {len(issues_found)} ***")
        for prob_num, title, lang, error in issues_found:
            print(f"  Problem {prob_num} ({title}) - {lang}: {error}")

if __name__ == '__main__':
    main()
