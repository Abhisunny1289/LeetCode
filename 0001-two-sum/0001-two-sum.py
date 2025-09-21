class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]