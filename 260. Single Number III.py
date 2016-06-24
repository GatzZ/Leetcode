#  Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
# Find the two elements that appear only once.
#
# For example:
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x_xor_y = reduce(lambda a, b: a ^ b, nums)
        x = 0
        y = 0
        diff_bit = 32
        # if x_xor_y[i] == 1, then x[i] != y[i]. and we can separate nums into two groups(num[i] == 1, num[i] != 1)
        for i in xrange(32):
            if (x_xor_y >> i) & 1 == 1:
                diff_bit = i
                break
        for num in nums:
            if (num >> diff_bit) & 1 == 1:
                x ^= num
            else:
                y ^= num
        return x, y


nums = [1, 2, 1, 3, 2, 5]
print Solution().singleNumber(nums)
