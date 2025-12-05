"""
Complete Test Suite for Greedy Algorithms Problems
Tests all 15 problems with reference solutions matching starter code format
"""
import json
import os
import heapq

# ============ REFERENCE SOLUTIONS ============

# P1: Maximum Coins Collection
class Solution1:
    def maxCoins(self, piles, k):
        heap = [-p for p in piles]
        heapq.heapify(heap)
        total = 0
        for _ in range(k):
            if not heap:
                break
            coins = -heapq.heappop(heap)
            if coins > 0:
                total += coins
                if coins - 1 > 0:
                    heapq.heappush(heap, -(coins - 1))
        return total

# P2: Assign Cookies to Children
class Solution2:
    def assignCookies(self, greed, cookies):
        greed.sort()
        cookies.sort()
        i = j = count = 0
        while i < len(greed) and j < len(cookies):
            if cookies[j] >= greed[i]:
                count += 1
                i += 1
            j += 1
        return count

# P3: Maximum Product of Two Elements
class Solution3:
    def maxProduct(self, nums):
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)

# P4: Minimum Coins for Change
class Solution4:
    def minCoins(self, amount):
        coins = [10, 5, 2, 1]
        count = 0
        for c in coins:
            count += amount // c
            amount %= c
        return count

# P5: Buy Maximum Items with Budget
class Solution5:
    def maxItems(self, prices, budget):
        prices.sort()
        count = 0
        for p in prices:
            if budget >= p:
                budget -= p
                count += 1
        return count

# P6: Activity Selection Problem
class Solution6:
    def maxActivities(self, activities):
        activities.sort(key=lambda x: x[1])
        count = 0
        last_end = -1
        for start, end in activities:
            if start >= last_end:
                count += 1
                last_end = end
        return count

# P7: Fractional Knapsack
class Solution7:
    def fractionalKnapsack(self, items, capacity):
        items = [(v, w, v/w) for v, w in items]
        items.sort(key=lambda x: x[2], reverse=True)
        total = 0.0
        for v, w, ratio in items:
            if capacity >= w:
                total += v
                capacity -= w
            else:
                total += ratio * capacity
                break
        return total

# P8: Minimum Platforms Required
class Solution8:
    def minPlatforms(self, arrivals, departures):
        arrivals.sort()
        departures.sort()
        platforms = max_platforms = 0
        i = j = 0
        n = len(arrivals)
        while i < n and j < n:
            if arrivals[i] <= departures[j]:
                platforms += 1
                max_platforms = max(max_platforms, platforms)
                i += 1
            else:
                platforms -= 1
                j += 1
        return max_platforms

# P9: Job Sequencing with Deadlines
class Solution9:
    def jobSequencing(self, jobs):
        jobs.sort(key=lambda x: x[1], reverse=True)
        max_deadline = max(j[0] for j in jobs)
        slots = [False] * (max_deadline + 1)
        profit = 0
        for deadline, p in jobs:
            for slot in range(min(deadline, max_deadline), 0, -1):
                if not slots[slot]:
                    slots[slot] = True
                    profit += p
                    break
        return profit

# P10: Minimum Arrows to Burst Balloons
class Solution10:
    def minArrows(self, balloons):
        if not balloons:
            return 0
        balloons.sort(key=lambda x: x[1])
        arrows = 1
        pos = balloons[0][1]
        for start, end in balloons[1:]:
            if start > pos:
                arrows += 1
                pos = end
        return arrows

# P11: Huffman Encoding
class Solution11:
    def huffmanCost(self, frequencies):
        if len(frequencies) == 1:
            return frequencies[0]
        heap = frequencies[:]
        heapq.heapify(heap)
        cost = 0
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            cost += a + b
            heapq.heappush(heap, a + b)
        return cost

# P12: Minimum Cost to Connect All Ropes
class Solution12:
    def minCostToConnectRopes(self, lengths):
        if len(lengths) == 1:
            return 0
        heap = lengths[:]
        heapq.heapify(heap)
        cost = 0
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            cost += a + b
            heapq.heappush(heap, a + b)
        return cost

# P13: Optimal Merge Pattern
class Solution13:
    def optimalMergeCost(self, sizes):
        if len(sizes) == 1:
            return 0
        heap = sizes[:]
        heapq.heapify(heap)
        cost = 0
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            cost += a + b
            heapq.heappush(heap, a + b)
        return cost

# P14: Maximum Meetings in One Room
class Solution14:
    def maxMeetings(self, meetings):
        meetings.sort(key=lambda x: x[1])
        selected = []
        last_end = -1
        for start, end, idx in meetings:
            if start >= last_end:
                selected.append(idx)
                last_end = end
        return len(selected), selected

# P15: Minimum Spanning Tree (Prim's)
class Solution15:
    def primMST(self, n, edges):
        adj = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            adj[u].append((w, v))
            adj[v].append((w, u))
        visited = [False] * (n + 1)
        heap = [(0, 1)]
        cost = 0
        count = 0
        while heap and count < n:
            w, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            cost += w
            count += 1
            for wt, v in adj[u]:
                if not visited[v]:
                    heapq.heappush(heap, (wt, v))
        return cost


# ============ INPUT PARSER ============

def parse_input(problem_num, input_str):
    lines = input_str.strip().split('\n')
    
    if problem_num == 1:
        n, k = map(int, lines[0].split())
        piles = list(map(int, lines[1].split()))
        return (piles, k)
    
    elif problem_num == 2:
        greed = list(map(int, lines[1].split()))
        cookies = list(map(int, lines[3].split()))
        return (greed, cookies)
    
    elif problem_num == 3:
        nums = list(map(int, lines[1].split()))
        return (nums,)
    
    elif problem_num == 4:
        amount = int(lines[0])
        return (amount,)
    
    elif problem_num == 5:
        n, budget = map(int, lines[0].split())
        prices = list(map(int, lines[1].split()))
        return (prices, budget)
    
    elif problem_num == 6:
        n = int(lines[0])
        activities = []
        for i in range(1, n + 1):
            s, e = map(int, lines[i].split())
            activities.append((s, e))
        return (activities,)
    
    elif problem_num == 7:
        n, capacity = map(int, lines[0].split())
        items = []
        for i in range(1, n + 1):
            v, w = map(int, lines[i].split())
            items.append((v, w))
        return (items, capacity)
    
    elif problem_num == 8:
        n = int(lines[0])
        arrivals = list(map(int, lines[1].split()))
        departures = list(map(int, lines[2].split()))
        return (arrivals, departures)
    
    elif problem_num == 9:
        n = int(lines[0])
        jobs = []
        for i in range(1, n + 1):
            d, p = map(int, lines[i].split())
            jobs.append((d, p))
        return (jobs,)
    
    elif problem_num == 10:
        n = int(lines[0])
        balloons = []
        for i in range(1, n + 1):
            s, e = map(int, lines[i].split())
            balloons.append((s, e))
        return (balloons,)
    
    elif problem_num == 11:
        frequencies = list(map(int, lines[1].split()))
        return (frequencies,)
    
    elif problem_num == 12:
        lengths = list(map(int, lines[1].split()))
        return (lengths,)
    
    elif problem_num == 13:
        sizes = list(map(int, lines[1].split()))
        return (sizes,)
    
    elif problem_num == 14:
        n = int(lines[0])
        meetings = []
        for i in range(1, n + 1):
            s, e = map(int, lines[i].split())
            meetings.append((s, e, i))
        return (meetings,)
    
    elif problem_num == 15:
        n, m = map(int, lines[0].split())
        edges = []
        for i in range(1, m + 1):
            u, v, w = map(int, lines[i].split())
            edges.append((u, v, w))
        return (n, edges)


def run_solution(problem_num, args):
    if problem_num == 1:
        sol = Solution1()
        return str(sol.maxCoins(*args))
    elif problem_num == 2:
        sol = Solution2()
        return str(sol.assignCookies(*args))
    elif problem_num == 3:
        sol = Solution3()
        return str(sol.maxProduct(*args))
    elif problem_num == 4:
        sol = Solution4()
        return str(sol.minCoins(*args))
    elif problem_num == 5:
        sol = Solution5()
        return str(sol.maxItems(*args))
    elif problem_num == 6:
        sol = Solution6()
        return str(sol.maxActivities(*args))
    elif problem_num == 7:
        sol = Solution7()
        return f"{sol.fractionalKnapsack(*args):.2f}"
    elif problem_num == 8:
        sol = Solution8()
        return str(sol.minPlatforms(*args))
    elif problem_num == 9:
        sol = Solution9()
        return str(sol.jobSequencing(*args))
    elif problem_num == 10:
        sol = Solution10()
        return str(sol.minArrows(*args))
    elif problem_num == 11:
        sol = Solution11()
        return str(sol.huffmanCost(*args))
    elif problem_num == 12:
        sol = Solution12()
        return str(sol.minCostToConnectRopes(*args))
    elif problem_num == 13:
        sol = Solution13()
        return str(sol.optimalMergeCost(*args))
    elif problem_num == 14:
        sol = Solution14()
        count, indices = sol.maxMeetings(*args)
        return str(count) + "\n" + " ".join(map(str, indices))
    elif problem_num == 15:
        sol = Solution15()
        return str(sol.primMST(*args))


# ============ MAIN TEST RUNNER ============

def main():
    folder = r'd:\gatetutor\all Q\Data Structure\20255\Greedy Algorithms'
    
    print("=" * 60)
    print("GREEDY ALGORITHMS - COMPLETE TEST SUITE")
    print("=" * 60)
    print()
    
    total_tests = 0
    passed_tests = 0
    failed_problems = []
    
    for i in range(1, 16):
        filepath = os.path.join(folder, f'{i}.json')
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            problem = data['problems'][0]
            title = problem['title']
            test_cases = problem['testCases']
            
            problem_passed = True
            results = []
            
            for tc_idx, tc in enumerate(test_cases):
                total_tests += 1
                input_str = tc['input']
                expected = tc['expectedOutput']
                
                try:
                    args = parse_input(i, input_str)
                    actual = run_solution(i, args)
                    
                    if actual == expected:
                        passed_tests += 1
                        results.append(f"TC{tc_idx+1}:✓")
                    else:
                        problem_passed = False
                        results.append(f"TC{tc_idx+1}:✗({actual}!={expected})")
                except Exception as e:
                    problem_passed = False
                    results.append(f"TC{tc_idx+1}:ERR({str(e)[:20]})")
            
            status = "PASS" if problem_passed else "FAIL"
            if not problem_passed:
                failed_problems.append(i)
            
            diff_map = {1: 'Easy', 2: 'Medium', 3: 'Hard'}
            diff = diff_map.get(problem['difficulty'], '?')
            
            print(f"P{i:2d} [{diff:6s}] {title[:35]:35s} {status}")
            print(f"    {' '.join(results)}")
            
        except Exception as e:
            print(f"P{i:2d} ERROR: {str(e)}")
            failed_problems.append(i)
    
    print()
    print("=" * 60)
    print(f"RESULTS: {passed_tests}/{total_tests} tests passed")
    
    if failed_problems:
        print(f"FAILED PROBLEMS: {failed_problems}")
    else:
        print("ALL PROBLEMS PASSED! ✓")
    print("=" * 60)


if __name__ == '__main__':
    main()
