#  Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end_here = nums[0]
        ans = nums[0]
        for i in xrange(1, len(nums)):
            end_here = max(end_here + nums[i], nums[i])
            ans = max(ans, end_here)
        return ans
