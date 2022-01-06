"""
9. Palindrome number
"""

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        strx = str(x)
        rstrx = strx[::-1]

        if strx == rstrx:
            return True
        else:
            return False


sol = Solution()
assert sol.isPalindrome(121) is True
assert sol.isPalindrome(-121) is False
assert sol.isPalindrome(10) is False
