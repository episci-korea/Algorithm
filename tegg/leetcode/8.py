import re


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        match = re.match(r'^\s*([+|-]?\d+)', s)

        if match:
            integer = int(match.group())
            return max(-(1 << 31), min(integer, (1 << 31) - 1))

        return 0


sol = Solution()
assert sol.myAtoi("42") == 42
assert sol.myAtoi("-42") == -42
assert sol.myAtoi("4193 with words") == 4193
