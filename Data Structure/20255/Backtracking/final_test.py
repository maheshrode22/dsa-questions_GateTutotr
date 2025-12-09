"""
Final Verification Suite for Backtracking Problems
"""
import json
import os
import sys

# ============ REFERENCE SOLUTIONS ============

class Solution1:
    def generateBinaryStrings(self, n):
        if n == 0: return []
        res = []
        def backtrack(s):
            if len(s) == n:
                res.append(s)
                return
            backtrack(s + '0')
            backtrack(s + '1')
        backtrack("")
        return res

class Solution2:
    def permuteString(self, s):
        res = []
        s = sorted(list(s))
        used = [False] * len(s)
        def backtrack(path):
            if len(path) == len(s):
                res.append("".join(path))
                return
            for i in range(len(s)):
                if used[i]: continue
                if i > 0 and s[i] == s[i-1] and not used[i-1]: continue
                used[i] = True
                path.append(s[i])
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return res

class Solution3:
    def generateParenthesis(self, n):
        res = []
        def backtrack(s, open_cnt, close_cnt):
            if len(s) == 2 * n:
                res.append(s)
                return
            if open_cnt < n:
                backtrack(s + '(', open_cnt + 1, close_cnt)
            if close_cnt < open_cnt:
                backtrack(s + ')', open_cnt, close_cnt + 1)
        backtrack("", 0, 0)
        return res

class Solution4:
    def letterCasePermutation(self, s):
        res = []
        def backtrack(idx, path):
            if idx == len(s):
                res.append("".join(path))
                return
            if s[idx].isalpha():
                path.append(s[idx].lower())
                backtrack(idx + 1, path)
                path.pop()
                path.append(s[idx].upper())
                backtrack(idx + 1, path)
                path.pop()
            else:
                path.append(s[idx])
                backtrack(idx + 1, path)
                path.pop()
        backtrack(0, [])
        return res

class Solution5:
    def combine(self, n, k):
        res = []
        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return res

class Solution6:
    def permute(self, nums):
        res = []
        def backtrack(path, remaining):
            if not remaining:
                res.append(path[:])
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        backtrack([], nums)
        return res

class Solution7:
    def subsets(self, nums):
        res = []
        nums.sort()
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return res

class Solution8:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        def backtrack(start, current_sum, path):
            if current_sum == target:
                res.append(path[:])
                return
            if current_sum > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, current_sum + candidates[i], path)
                path.pop()
        backtrack(0, 0, [])
        return res

class Solution9:
    def partition(self, s):
        res = []
        def is_palindrome(sub):
            return sub == sub[::-1]
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for i in range(start + 1, len(s) + 1):
                sub = s[start:i]
                if is_palindrome(sub):
                    path.append(sub)
                    backtrack(i, path)
                    path.pop()
        backtrack(0, [])
        return res

class Solution10:
    def exist(self, board, word):
        if not board: return False
        m, n = len(board), len(board[0])
        def backtrack(i, j, k):
            if k == len(word): return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            temp, board[i][j] = board[i][j], '#'
            res = (backtrack(i+1, j, k+1) or 
                   backtrack(i-1, j, k+1) or 
                   backtrack(i, j+1, k+1) or 
                   backtrack(i, j-1, k+1))
            board[i][j] = temp
            return res
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0): return True
        return False

class Solution11:
    def solveNQueens(self, n):
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        pos_diag = set()
        neg_diag = set()
        
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = 'Q'
                backtrack(r + 1)
                board[r][c] = '.'
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
        backtrack(0)
        return res

class Solution12:
    def solveSudoku(self, board):
        def isValid(r, c, k):
            for i in range(9):
                if board[r][i] == k: return False
                if board[i][c] == k: return False
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == k: return False
            return True
        
        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        for k in range(1, 10):
                            if isValid(i, j, k):
                                board[i][j] = k
                                if backtrack(): return True
                                board[i][j] = 0
                        return False
            return True
        backtrack()

class Solution13:
    def findPath(self, m, n):
        res = []
        if m[0][0] == 0 or m[n-1][n-1] == 0: return []
        
        def backtrack(r, c, path):
            if r == n - 1 and c == n - 1:
                res.append(path)
                return
            
            # Mark visited
            temp = m[r][c]
            m[r][c] = 0
            
            # D, L, R, U
            moves = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]
            for move, dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and m[nr][nc] == 1:
                    backtrack(nr, nc, path + move)
            
            m[r][c] = temp
            
        backtrack(0, 0, "")
        return res

class Solution14:
    def graphColoring(self, graph, m, n):
        colors = [0] * n
        def is_safe(v, c):
            for i in range(n):
                if graph[v][i] == 1 and colors[i] == c:
                    return False
            return True
        
        def backtrack(v):
            if v == n: return True
            for c in range(1, m + 1):
                if is_safe(v, c):
                    colors[v] = c
                    if backtrack(v + 1): return True
                    colors[v] = 0
            return False
        return backtrack(0)

class Solution15:
    def solveKnightTour(self, n):
        board = [[-1 for _ in range(n)] for _ in range(n)]
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        def is_safe(x, y):
            return 0 <= x < n and 0 <= y < n and board[x][y] == -1
            
        def backtrack(x, y, move_count):
            if move_count == n * n:
                return True
            
            # Warnsdorff's heuristic
            next_moves = []
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if is_safe(nx, ny):
                    count = 0
                    for ddx, ddy in moves:
                        if is_safe(nx + ddx, ny + ddy):
                            count += 1
                    next_moves.append((count, nx, ny))
            
            next_moves.sort()
            
            for _, nx, ny in next_moves:
                board[nx][ny] = move_count
                if backtrack(nx, ny, move_count + 1):
                    return True
                board[nx][ny] = -1
            return False

        board[0][0] = 0
        if backtrack(0, 0, 1):
            return board
        return []

# ============ INPUT PARSER ============

def parse_input(problem_num, input_str):
    lines = input_str.strip().split('\n')
    
    if problem_num == 1:
        return (int(lines[0]),)
    elif problem_num == 2:
        return (lines[0],)
    elif problem_num == 3:
        return (int(lines[0]),)
    elif problem_num == 4:
        return (lines[0],)
    elif problem_num == 5:
        n, k = map(int, lines[0].split())
        return (n, k)
    elif problem_num == 6:
        n = int(lines[0])
        nums = list(map(int, lines[1].split()))
        return (nums,)
    elif problem_num == 7:
        if not lines or lines[0] == "": return ([],)
        n = int(lines[0])
        if n == 0: return ([],)
        nums = list(map(int, lines[1].split()))
        return (nums,)
    elif problem_num == 8:
        n, target = map(int, lines[0].split())
        candidates = list(map(int, lines[1].split()))
        return (candidates, target)
    elif problem_num == 9:
        return (lines[0],)
    elif problem_num == 10:
        m, n = map(int, lines[0].split())
        board = []
        for i in range(m):
            board.append(list(lines[i+1]))
        word = lines[m+1]
        return (board, word)
    elif problem_num == 11:
        return (int(lines[0]),)
    elif problem_num == 12:
        board = []
        for i in range(9):
            board.append(list(map(int, lines[i].split())))
        return (board,)
    elif problem_num == 13:
        n = int(lines[0])
        m = []
        for i in range(n):
            m.append(list(map(int, lines[i+1].split())))
        return (m, n)
    elif problem_num == 14:
        n, m = map(int, lines[0].split())
        graph = []
        for i in range(n):
            graph.append(list(map(int, lines[i+1].split())))
        return (graph, m, n)
    elif problem_num == 15:
        return (int(lines[0]),)

def run_solution(problem_num, args):
    if problem_num == 1:
        sol = Solution1()
        return " ".join(sol.generateBinaryStrings(*args))
    elif problem_num == 2:
        sol = Solution2()
        return " ".join(sol.permuteString(*args))
    elif problem_num == 3:
        sol = Solution3()
        res = sol.generateParenthesis(*args)
        res.sort()
        return " ".join(res)
    elif problem_num == 4:
        sol = Solution4()
        res = sol.letterCasePermutation(*args)
        res.sort()
        return " ".join(res)
    elif problem_num == 5:
        sol = Solution5()
        res = sol.combine(*args)
        return " ".join([",".join(map(str, c)) for c in res])
    elif problem_num == 6:
        sol = Solution6()
        res = sol.permute(*args)
        res.sort()
        return " ".join([",".join(map(str, c)) for c in res])
    elif problem_num == 7:
        sol = Solution7()
        res = sol.subsets(*args)
        res = [sorted(s) for s in res]
        res.sort()
        return " ".join([",".join(map(str, s)) for s in res])
    elif problem_num == 8:
        sol = Solution8()
        res = sol.combinationSum(*args)
        res = [sorted(c) for c in res]
        res.sort()
        return " ".join([",".join(map(str, c)) for c in res])
    elif problem_num == 9:
        sol = Solution9()
        res = sol.partition(*args)
        res.sort()
        return " ".join([",".join(p) for p in res])
    elif problem_num == 10:
        sol = Solution10()
        return "true" if sol.exist(*args) else "false"
    elif problem_num == 11:
        sol = Solution11()
        res = sol.solveNQueens(*args)
        output = [" ".join(board) for board in res]
        output.sort()
        return " ".join(output)
    elif problem_num == 12:
        sol = Solution12()
        board = args[0]
        sol.solveSudoku(board)
        return "\n".join([" ".join(map(str, row)) for row in board])
    elif problem_num == 13:
        sol = Solution13()
        res = sol.findPath(*args)
        res.sort()
        return " ".join(res)
    elif problem_num == 14:
        sol = Solution14()
        return "true" if sol.graphColoring(*args) else "false"
    elif problem_num == 15:
        sol = Solution15()
        res = sol.solveKnightTour(*args)
        if not res: return ""
        return "\n".join([" ".join(map(str, row)) for row in res])

# ============ MAIN TEST RUNNER ============

def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    print("=" * 60)
    print("BACKTRACKING - FINAL VERIFICATION")
    print("=" * 60)
    
    total_tests = 0
    passed_tests = 0
    
    for i in range(1, 16):
        filepath = os.path.join(folder, f'{i}.json')
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            problem = data['problems'][0]
            title = problem['title']
            test_cases = problem['testCases']
            
            print(f"P{i}: {title}...", end=" ")
            
            problem_passed = True
            for tc in test_cases:
                total_tests += 1
                input_str = tc['input']
                expected = tc['expectedOutput']
                
                args = parse_input(i, input_str)
                actual = run_solution(i, args)
                
                if actual.strip() != expected.strip():
                    problem_passed = False
                    print(f"\n  FAIL on input: {input_str[:20]}...")
                    print(f"  Exp: {expected[:50]}...")
                    print(f"  Got: {actual[:50]}...")
                    break
            
            if problem_passed:
                print("PASS")
                passed_tests += 5
            
        except Exception as e:
            print(f"\n  ERROR: {str(e)}")
    
    print("=" * 60)
    print(f"RESULTS: {passed_tests}/{total_tests} tests passed")
    if passed_tests == total_tests:
        print("ALL PROBLEMS PASSED! ✓")
    else:
        print("SOME TESTS FAILED")

if __name__ == '__main__':
    main()
