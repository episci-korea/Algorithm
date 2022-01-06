"""
13. Roman to integer
"""

class Solution:
    def romanToInt(self, s):
        romans = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
        }

        if len(s) == 1:
            return romans[s]

        left = 0
        right = left + 1
        res = 0

        while left < len(s) or right < len(s):
            if right >= len(s):
                v = self.check(s[left], "", romans)

            else:
                v = self.check(s[left], s[right], romans)

            if not v:
                res += romans[s[left]]
                left += 1
                right += 1
            else:
                res += v
                left += 2
                right += 2

        return res

    def check(self, left, right, romans):
        temp = left + right
        if temp in romans:
            return romans[temp]
        return 0


sol = Solution()
assert sol.romanToInt('III') == 3
assert sol.romanToInt('LVIII') == 58
assert sol.romanToInt('MCMXCIV') == 1994
