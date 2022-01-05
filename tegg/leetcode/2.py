"""
2. Two sum
"""

class Solution:
    def twoSum(self, nums, target):
        if len(nums) < 2 or len(nums) > 10000:
            print('constraints error! 1')
            return 0
        elif min(nums) < -1000000000 or max(nums) > 1000000000:
            print('constraints error! 2')
            return 0
        elif target < -1000000000 or target > 1000000000:
            print('constraints error! 3')
            return 0
        else:
            d={}
            for k in range(len(nums)):
                d[nums[k]]=k

            for i in range(len(nums)):
                c = target - nums[i]

                if c in d and d[c] != i:
                    return [i, d[c]]
                else:
                    continue


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))
