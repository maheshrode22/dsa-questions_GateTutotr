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
        cwd='d:/gatetutor/all Q/2016/java'
    )
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip()

problems_map = {
    "2016-sort-1.json": "BubbleSort",
    "2016-sort-2.json": "SelectionSort",
    "2016-sort-3.json": "InsertionSort",
    "2016-sort-4.json": "ShellSort",
    "2016-sort-5.json": "QuickSort",
    "2016-sort-6.json": "RadixSort"
}

# Compile first
subprocess.run(['javac', 'Solutions.java'], cwd='d:/gatetutor/all Q/2016/java')

results = []
for file_name, class_name in problems_map.items():
    with open(f'd:/gatetutor/all Q/2016/{file_name}', 'r') as f:
        data = json.load(f)
        problem = data['problems'][0]
        print(f"Testing {problem['title']}...")
        
        all_passed = True
        for i, tc in enumerate(problem['testCases']):
            actual = run_java_test(class_name, tc['input'])
            expected = tc['expectedOutput'].strip()
            
            # Normalize spaces
            actual_norm = " ".join(actual.split())
            expected_norm = " ".join(expected.split())
            
            if actual_norm == expected_norm:
                print(f"  Test Case {i+1}: PASSED")
            else:
                print(f"  Test Case {i+1}: FAILED")
                print(f"    Input: {tc['input']!r}")
                print(f"    Expected: {expected_norm!r}")
                print(f"    Actual:   {actual_norm!r}")
                all_passed = False
        
        results.append({"problem": problem['title'], "status": "PASSED" if all_passed else "FAILED"})

print("\nSummary:")
for res in results:
    print(f"{res['problem']}: {res['status']}")
