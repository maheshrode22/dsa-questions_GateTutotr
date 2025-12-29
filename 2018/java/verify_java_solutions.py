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
        cwd='d:/gatetutor/all Q/2018/java'
    )
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip()

problems_map = {
    "2018-hash-1.json": "LinearProbing",
    "2018-hash-2.json": "QuadraticProbing",
    "2018-hash-3.json": "DoubleHashing",
    "2018-hash-4.json": "SeparateChaining",
    "2018-hash-5.json": "CountDistinct",
    "2018-hash-6.json": "FirstRepeating"
}

# Compile first
subprocess.run(['javac', 'Solutions.java'], cwd='d:/gatetutor/all Q/2018/java')

results = []
for file_name, class_name in problems_map.items():
    with open(f'd:/gatetutor/all Q/2018/{file_name}', 'r') as f:
        data = json.load(f)
        problem = data['problems'][0]
        print(f"Testing {problem['title']}...")
        
        all_passed = True
        for i, tc in enumerate(problem['testCases']):
            actual = run_java_test(class_name, tc['input'])
            expected = tc['expectedOutput'].strip()
            
            # Normalize spaces and newlines
            actual_norm = "\n".join([line.strip() for line in actual.splitlines() if line.strip()])
            expected_norm = "\n".join([line.strip() for line in expected.splitlines() if line.strip()])
            
            # For single line outputs, normalize spaces within lines
            if "\n" not in expected_norm:
                actual_norm = " ".join(actual_norm.split())
                expected_norm = " ".join(expected_norm.split())
            
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
