# coding=utf-8
# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -∞.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#
# click to show spoilers.
# Note:
#
# Your solution should be in logarithmic complexity.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #for nums[start...end], we keep nums[start - 1] < nums[start] and nums[end] > nums[end + 1]
        start, end = 0, len(nums) - 1
        while 1:
            if start==end:
                return start
            mid = (start + end) / 2
            if nums[mid] > nums[mid + 1]: #we keep nums[start - 1] < nums[start] and nums[mid] > nums[mid + 1]
                end = mid
            else: # nums[mid] <= nums[mid + 1]
                start = mid + 1


a = [1,2,3,1]
print Solution().findPeakElement(a)
