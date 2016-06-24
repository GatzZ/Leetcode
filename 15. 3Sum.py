# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# Time limit exceeds..........................................
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         two_sum_dict = {}
#         N = len(nums)
#         res = set()
#         for i in xrange(N - 1):
#             for j in xrange(i + 1, N):
#                 key = nums[i] + nums[j]
#                 if key in two_sum_dict:
#                     two_sum_dict[key].append((i, j))
#                 else:
#                     two_sum_dict[key] = [(i, j)]
#
#         for i in xrange(N):
#             the_key = -nums[i]
#             if the_key in two_sum_dict:
#                 for idx1, idx2 in two_sum_dict[the_key]:
#                     if idx1 != i and idx2 != i:
#                         tmp = [nums[i], nums[idx1], nums[idx2]]
#                         min_tmp = min(tmp)
#                         max_tmp = max(tmp)
#                         res.add((min_tmp, -(min_tmp + max_tmp), max_tmp))
#         return [list(triple) for triple in res]
# Time limit exceeds..........................................


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N = len(nums)
        res = []
        for i in xrange(N - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = N - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


nums = [1, -1, -1, 0]
print Solution().threeSum(nums)
