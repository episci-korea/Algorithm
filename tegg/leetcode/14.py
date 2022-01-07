class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref = []

        for st in zip(*strs):
            if len(set(st)) == 1:
                pref.append(st[0])
            else:
                break

        return ''.join(pref)


sol = Solution()
assert sol.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert sol.longestCommonPrefix(["dog","racecar","car"]) == ""
