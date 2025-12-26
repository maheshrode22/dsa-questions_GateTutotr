"""Quick verification of all sliding window problems"""
import json
import os
from collections import deque, Counter

def load_problem(num):
    with open(f"{num}.json", 'r', encoding='utf-8') as f:
        return json.load(f)['problems'][0]

# Reference solutions
def s1(inp):
    lines = inp.strip().split('\n')
    n, k = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    if k > n: return "0"
    ws = sum(arr[:k])
    ms = ws
    for i in range(k, n):
        ws = ws + arr[i] - arr[i-k]
        ms = max(ms, ws)
    return str(ms)

def s2(inp):
    lines = inp.strip().split('\n')
    n, k = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    if k > n: return ""
    cnt = sum(1 for i in range(k) if arr[i] % 2 == 0)
    res = [cnt]
    for i in range(k, n):
        if arr[i-k] % 2 == 0: cnt -= 1
        if arr[i] % 2 == 0: cnt += 1
        res.append(cnt)
    return ' '.join(map(str, res))

def s3(inp):
    lines = inp.strip().split('\n')
    n, k = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    nq = deque()
    res = []
    for i in range(n):
        if arr[i] < 0: nq.append(i)
        if i >= k-1:
            while nq and nq[0] < i-k+1: nq.popleft()
            res.append(arr[nq[0]] if nq else 0)
    return ' '.join(map(str, res))

def s4(inp):
    s = inp.strip()
    ci = {}
    ml, l = 0, 0
    for r in range(len(s)):
        if s[r] in ci and ci[s[r]] >= l: l = ci[s[r]] + 1
        ci[s[r]] = r
        ml = max(ml, r-l+1)
    return str(ml)

def s5(inp):
    lines = inp.strip().split('\n')
    n, K = int(lines[0].split()[0]), int(lines[0].split()[1])
    arr = list(map(int, lines[1].split()))
    l, ws, ml = 0, 0, 0
    for r in range(n):
        ws += arr[r]
        while ws > K and l <= r:
            ws -= arr[l]; l += 1
        ml = max(ml, r-l+1)
    return str(ml)

def s6(inp):
    lines = inp.strip().split('\n')
    n, K = int(lines[0].split()[0]), int(lines[0].split()[1])
    arr = list(map(int, lines[1].split()))
    l, ws, ml = 0, 0, float('inf')
    for r in range(n):
        ws += arr[r]
        while ws >= K:
            ml = min(ml, r-l+1)
            ws -= arr[l]; l += 1
    return str(ml) if ml != float('inf') else "0"

def s7(inp):
    lines = inp.strip().split('\n')
    s, K = lines[0].strip(), int(lines[1].strip())
    cc = {}; l, ml = 0, 0
    for r in range(len(s)):
        cc[s[r]] = cc.get(s[r], 0) + 1
        while len(cc) > K:
            cc[s[l]] -= 1
            if cc[s[l]] == 0: del cc[s[l]]
            l += 1
        ml = max(ml, r-l+1)
    return str(ml)

def s8(inp):
    lines = inp.strip().split('\n')
    n, K = int(lines[0].split()[0]), int(lines[0].split()[1])
    arr = list(map(int, lines[1].split()))
    l, zc, ml = 0, 0, 0
    for r in range(n):
        if arr[r] == 0: zc += 1
        while zc > K:
            if arr[l] == 0: zc -= 1
            l += 1
        ml = max(ml, r-l+1)
    return str(ml)

def s9(inp):
    lines = inp.strip().split('\n')
    s, t = lines[0].strip(), lines[1].strip()
    if len(t) > len(s): return "-1"
    tc = Counter(t)
    req, formed = len(tc), 0
    wc = {}; l, ml = 0, float('inf')
    for r in range(len(s)):
        c = s[r]
        wc[c] = wc.get(c, 0) + 1
        if c in tc and wc[c] == tc[c]: formed += 1
        while formed == req:
            if r-l+1 < ml: ml = r-l+1
            lc = s[l]
            wc[lc] -= 1
            if lc in tc and wc[lc] < tc[lc]: formed -= 1
            l += 1
    return str(ml) if ml != float('inf') else "-1"

def s10(inp):
    lines = inp.strip().split('\n')
    s, p = lines[0].strip(), lines[1].strip()
    if len(p) > len(s): return "0"
    pc = [0]*26; sc = [0]*26
    for c in p: pc[ord(c)-ord('a')] += 1
    cnt = 0
    for i in range(len(s)):
        sc[ord(s[i])-ord('a')] += 1
        if i >= len(p): sc[ord(s[i-len(p)])-ord('a')] -= 1
        if i >= len(p)-1 and sc == pc: cnt += 1
    return str(cnt)

def s11(inp):
    lines = inp.strip().split('\n')
    s, k = lines[0].strip(), int(lines[1].strip())
    vow = set('aeiouAEIOU')
    cnt = sum(1 for i in range(k) if s[i] in vow)
    mc = cnt
    for i in range(k, len(s)):
        if s[i-k] in vow: cnt -= 1
        if s[i] in vow: cnt += 1
        mc = max(mc, cnt)
    return str(mc)

def s12(inp):
    lines = inp.strip().split('\n')
    n, k = int(lines[0].split()[0]), int(lines[0].split()[1])
    arr = list(map(int, lines[1].split()))
    if k <= 1: return "0"
    l, prod, cnt = 0, 1, 0
    for r in range(n):
        prod *= arr[r]
        while prod >= k and l <= r:
            prod //= arr[l]; l += 1
        cnt += r-l+1
    return str(cnt)

def s13(inp):
    lines = inp.strip().split('\n')
    s, k = lines[0].strip(), int(lines[1].strip())
    cnt = [0]*26; l, mc, ml = 0, 0, 0
    for r in range(len(s)):
        idx = ord(s[r])-ord('A')
        cnt[idx] += 1
        mc = max(mc, cnt[idx])
        while r-l+1-mc > k:
            cnt[ord(s[l])-ord('A')] -= 1
            l += 1
        ml = max(ml, r-l+1)
    return str(ml)

def s14(inp):
    lines = inp.strip().split('\n')
    n, k = int(lines[0].split()[0]), int(lines[0].split()[1])
    nums = list(map(int, lines[1].split()))
    seen = {}
    for i in range(n):
        if nums[i] in seen and i-seen[nums[i]] <= k:
            return "true"
        seen[nums[i]] = i
    return "false"

def s15(inp):
    lines = inp.strip().split('\n')
    s, t, mc = lines[0].strip(), lines[1].strip(), int(lines[2].strip())
    costs = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
    l, cc, ml = 0, 0, 0
    for r in range(len(costs)):
        cc += costs[r]
        while cc > mc and l <= r:
            cc -= costs[l]; l += 1
        ml = max(ml, r-l+1)
    return str(ml)

solvers = {1:s1,2:s2,3:s3,4:s4,5:s5,6:s6,7:s7,8:s8,9:s9,10:s10,11:s11,12:s12,13:s13,14:s14,15:s15}

print("="*60)
print("SLIDING WINDOW - TEST CASE VERIFICATION")
print("="*60)
failed_problems = []
for pnum in range(1, 16):
    prob = load_problem(pnum)
    solver = solvers[pnum]
    all_pass = True
    fails = []
    for i, tc in enumerate(prob['testCases']):
        exp = tc['expectedOutput'].strip()
        try:
            act = solver(tc['input']).strip()
        except Exception as e:
            act = f"ERR:{e}"
        if act != exp:
            all_pass = False
            fails.append((i+1, exp, act, tc['input']))
    status = "PASS" if all_pass else "FAIL"
    print(f"Problem {pnum:2d}: {prob['title'][:45]:45s} [{status}]")
    if not all_pass:
        failed_problems.append((pnum, prob['title'], fails))

print("\n" + "="*60)
if failed_problems:
    print(f"FAILED PROBLEMS: {len(failed_problems)}")
    for pnum, title, fails in failed_problems:
        print(f"\nProblem {pnum}: {title}")
        for tc_num, exp, act, inp in fails:
            print(f"  TC{tc_num}: Expected='{exp}' Actual='{act}'")
            print(f"       Input: {inp[:60]}...")
else:
    print("ALL 15 PROBLEMS PASSED!")
