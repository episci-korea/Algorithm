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


if __name__ == "__main__":
    test = []
    for t in test:
        print(solution(t))
