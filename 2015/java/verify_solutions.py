import json
import subprocess
import os

def run_java_test(class_name, input_str):
    process = subprocess.Popen(
        ['java', '-cp', '.', class_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd='d:/gatetutor/all Q/2014/java'
    )
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip()

problems_map = {
    "2014-rec-1.json": "RecursiveFactorial",
    "2014-rec-2.json": "RecursiveSumOfDigits",
    "2014-rec-3.json": "RecursiveFibonacci",
    "2014-rec-4.json": "RecursivePower",
    "2014-rec-5.json": "TowerOfHanoi",
    "2014-rec-6.json": "RecursiveStringReversal",
    "2014-rec-7.json": "RecursiveCheckSorted",
    "2014-rec-8.json": "StringPermutations",
    "2014-rec-9.json": "NQueensCount",
    "2014-rec-10.json": "SubsetSum"
}

# Compile first
subprocess.run(['javac', 'Solutions.java'], cwd='d:/gatetutor/all Q/2014/java')

results = []
for file_name, class_name in problems_map.items():
    with open(f'd:/gatetutor/all Q/2014/{file_name}', 'r') as f:
        data = json.load(f)
        problem = data['problems'][0]
        print(f"Testing {problem['title']}...")
        
        all_passed = True
        for i, tc in enumerate(problem['testCases']):
            actual = run_java_test(class_name, tc['input'])
            expected = tc['expectedOutput'].strip()
            
            # Normalize line endings for multiline outputs
            actual_norm = "\n".join([line.strip() for line in actual.splitlines()])
            expected_norm = "\n".join([line.strip() for line in expected.splitlines()])
            
            if actual_norm == expected_norm:
                print(f"  Test Case {i+1}: PASSED")
            else:
                print(f"  Test Case {i+1}: FAILED")
                print(f"    Input: {tc['input']!r}")
                import difflib
                diff = difflib.unified_diff(
                    expected_norm.splitlines(),
                    actual_norm.splitlines(),
                    fromfile='Expected',
                    tofile='Actual',
                    lineterm=''
                )
                print("\n".join(diff))
                all_passed = False
        
        results.append({"problem": problem['title'], "status": "PASSED" if all_passed else "FAILED"})

print("\nSummary:")
for res in results:
    print(f"{res['problem']}: {res['status']}")
