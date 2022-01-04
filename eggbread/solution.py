import time
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
    """
    프로그래머스 : 프린터
    Θ(n)
    Queue 사용 문제
    """
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
if __name__ == "__main__":
    test = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(test))
