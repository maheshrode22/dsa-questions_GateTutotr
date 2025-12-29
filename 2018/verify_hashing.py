import json
import os

def linear_probing(m, n, keys):
    table = [-1] * m
    for key in keys:
        idx = key % m
        i = 0
        while i < m:
            curr = (idx + i) % m
            if table[curr] == -1:
                table[curr] = key
                break
            i += 1
    return table

def quadratic_probing(m, n, keys):
    table = [-1] * m
    for key in keys:
        idx = key % m
        i = 0
        while i < m:
            curr = (idx + i*i) % m
            if table[curr] == -1:
                table[curr] = key
                break
            i += 1
    return table

def double_hashing(m, p, n, keys):
    table = [-1] * m
    for key in keys:
        h1 = key % m
        h2 = p - (key % p)
        i = 0
        while i < m:
            curr = (h1 + i * h2) % m
            if table[curr] == -1:
                table[curr] = key
                break
            i += 1
    return table

def separate_chaining(m, n, keys):
    table = [[] for _ in range(m)]
    for key in keys:
        idx = key % m
        table[idx].append(key)
    return table

def count_distinct(arr, n):
    return len(set(arr))

def first_repeating(arr, n):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    for x in arr:
        if counts[x] > 1:
            return x
    return -1

def verify_problem(file_path, func, is_chaining=False, is_double=False):
    with open(file_path, 'r') as f:
        data = json.load(f)
        problem = data['problems'][0]
        print(f"Verifying {problem['title']}...")
        for i, tc in enumerate(problem['testCases']):
            lines = tc['input'].strip().split('\n')
            line1 = lines[0].split()
            
            if is_double:
                m_val, p_val, n_val = map(int, line1)
            elif problem['title'] in ["Count Distinct Elements", "First Repeating Element"]:
                n_val = int(line1[0])
                m_val = 0
            else:
                m_val, n_val = map(int, line1)
            
            if n_val > 0:
                keys = list(map(int, lines[1].split()))
            else:
                keys = []
            
            if is_chaining:
                actual_table = func(m_val, n_val, keys)
                actual_lines = []
                for idx in range(m_val):
                    actual_lines.append(f"Index {idx}: {' '.join(map(str, actual_table[idx]))}")
                actual = "\n".join(actual_lines).strip()
            elif is_double:
                actual = " ".join(map(str, func(m_val, p_val, n_val, keys)))
            elif problem['title'] in ["Count Distinct Elements", "First Repeating Element"]:
                actual = str(func(keys, n_val))
            else:
                actual = " ".join(map(str, func(m_val, n_val, keys)))
            
            expected = tc['expectedOutput'].strip()
            if actual.replace('\r', '') == expected.replace('\r', ''):
                print(f"  Test Case {i+1}: PASSED")
            else:
                print(f"  Test Case {i+1}: FAILED")
                print(f"    Input: {tc['input']!r}")
                print(f"    Expected: {expected!r}")
                print(f"    Actual:   {actual!r}")
                return False
    return True

base_path = 'd:/gatetutor/all Q/2018/'
problems = [
    ('2018-hash-1.json', linear_probing),
    ('2018-hash-2.json', quadratic_probing),
    ('2018-hash-3.json', double_hashing, False, True),
    ('2018-hash-4.json', separate_chaining, True),
    ('2018-hash-5.json', count_distinct),
    ('2018-hash-6.json', first_repeating)
]

all_passed = True
for p in problems:
    file_name = p[0]
    func = p[1]
    is_chain = p[2] if len(p) > 2 else False
    is_double = p[3] if len(p) > 3 else False
    if not verify_problem(os.path.join(base_path, file_name), func, is_chain, is_double):
        all_passed = False

if all_passed:
    print("\nAll hashing problems verified successfully!")
else:
    print("\nSome problems failed verification.")
