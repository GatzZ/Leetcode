#  Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.

# solution 1 48ms
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # keep nums[0,...N-1] = [1,..,N]
        N = len(nums)
        i = 0
        while i < N:
            if nums[i] == i + 1:  # it's ok, just increcse i
                i += 1
            elif nums[i] < i + 1 or nums[i] > N or nums[i] == nums[nums[i] - 1]:  # drop this
                nums[i] = nums[N - 1]
                N -= 1
            else:  # swap to right position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return N + 1


# solution 2 #47ms
# class Solution(object):
#     def firstMissingPositive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # keep nums[0,...N-1] = [1,..,N]
#         N = len(nums)
#         for i in xrange(N):
#             while nums[i] > 0 and nums[i] <= N and nums[i] != nums[nums[i] - 1]:
#                 j = nums[i] - 1
#                 nums[i], nums[j] = nums[j], nums[i]
#                 #nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i] # not ok, because num[i] - 1 will change index
#         for i in xrange(N):
#             if nums[i] != i + 1:
#                 return i + 1
#         return N + 1



nums = [1, 2, 0]
nums = [2, 1]

print Solution().firstMissingPositive(nums)
