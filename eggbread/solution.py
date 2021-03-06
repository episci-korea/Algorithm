import time
from summary import *
"""
Problem : Programmers 문자열 압축 lv2
Time : n^2
Solution : Searching
"""
def solution_20220101(s):
    minValue = len(s)
    for i in range(1, int(len(s)/2)+1):
        prev = s[:i]
        prev_head = 0
        prev_tail = i
        stack = 1
        n = len(s)
        for j in range(i,n,i):
            if prev == s[j:j+i]:
                stack += 1
            else:
                prev = s[j:j+i]
                prev_head = j
                prev_tail = j+i
                if stack > 1:
                    n -= i*(stack-1) - len(str(stack))
                    stack = 1
        if stack >1:
            n -= i * (stack - 1) - len(str(stack))
        if minValue > n:
            minValue = n
    return minValue

"""
Problem : Programmers 멀쩡한 사각형 lv2
Time : n
Solution : greatest common divisor
"""
def solution_20220102(w,h):
    g = gcd(w, h)
    return w*h - w-h+g

def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

"""
Problem : Programmers 거리두기 확인하기 lv2
Time : n^2
Solution : BFS
"""
from collections import deque
def bfs(p):
    start = []
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:
        queue = deque([s])
        visited = [[0] * 5 for i in range(5)]
        distance = [[0] * 5 for i in range(5)]
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution_20220103(places):
    answer = []
    for i in places:
        answer.append(bfs(i))
    return answer

"""
Problem : Programmers 프린터 lv2
Time : n
Solution : Queue
"""
def solution_20220104(priorities, location):
    answer = 0
    while True:
        if len(priorities) < 2:
            answer += 1
            break
        else:
            value = priorities[0]
            priorities.pop(0)
            if value >= max(priorities):
                answer += 1
                if location:
                    location -= 1
                else:
                    break
            else:
                if location:
                    location -= 1
                else:
                    location = len(priorities)
                priorities.append(value)
    return answer

"""
Problem : Programmers N으로 표현 lv3
Time : 
Solution : DP
"""
def solution_20220105(N, number):

    sets = [set()]
    answer = 9
    for i in range(1, 9):
        sets.append(set())
        sets[i].add(int(str(N) * i))
    if number == N:
        return 1
    for i in range(2, 8):
        for j in range(1, i):
            for a in sets[j]:
                for b in sets[i - j]:
                    sets[i].add(a + b)
                    sets[i].add(a - b)
                    sets[i].add(a * b)
                    if b:
                        sets[i].add(a // b)
        if number in sets[i]:
            if answer > i:
                answer = i
            break

    if answer == 9:
        return -1
    else:
        return answer

"""
Problem : Programmers 게임 맵 최단거리 lv2
Time : n
Solution : BFS, 방문체크를 큐에 넣을 때 해야 효율성이 올라간다.
"""
from collections import deque
def solution_20220106(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    q = deque([(0,0)])
    direction = [[1,0],[-1,0],[0,1],[0,-1]]
    while q:
        y, x = q.popleft()
        for vy, vx in direction:
            nx, ny = x + vx, y + vy
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and maps[ny][nx]:
                    maps[ny][nx] = maps[y][x] + 1
                    visited[ny][nx] = 1
                    q.append((ny,nx))
    return maps[-1][-1] if maps[-1][-1] != 1 else -1
"""
Problem : Programmers 나머지가 1이 되는 수 찾기 lv1
Time : n^0.5
Solution : divisor
"""
def solution_20220108(n):
    for i in range(2, int((n-1) ** (1 / 2)) + 1):
        if not (n-1) % i:
            return i
    return n - 1

"""
Problem : Programmers 최소직사각형 lv1
Time : n
Solution : Search
"""
def solution_20220109(sizes):
    max_width = max(max(size) for size in sizes)
    max_height = max(min(size) for size in sizes)
    return max_height * max_width

"""
Problem : Programmers 부족한 금액 계산하기 lv1
Time : 1
Solution : AP
"""
def solution_20220110(price, money, count):
    return max(0,price*(count+1)*count//2-money)

"""
Problem : Programmers 음양더하기 lv1
Time : n
Solution : Implementation
"""
def solution_20220111(absolutes, signs):
    return sum(list(map(lambda x:x[0] if x[1] else -1*x[0], zip(absolutes, signs))))

"""
Problem : Programmers 약수의 개수와 덧셈 lv1
Time : n^(1/2)
Solution : divisor
"""
def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        length = len(get_divisor(x))
        if length % 2:
            answer -= x
        else:
            answer += x
    return answer

"""
Problem : leetcode Word Pattern Easy
Time : n^2
Solution : dict
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import defaultdict
        d = defaultdict(str)
        words = s.split()
        if len(pattern) != len(words):
            return False
        for pat, word in zip(pattern, words):
            if pat not in d:
                if word in d.values():
                    return False
                d[pat] = word
            else:
                if d[pat] !=  word:
                    return False
        return True

if __name__ == "__main__":
    test = [["abba","dog cat cat dog"],["aaa","aa aa aa aa"]]
    for a,b in test:
        print(Solution().wordPattern(a,b))
