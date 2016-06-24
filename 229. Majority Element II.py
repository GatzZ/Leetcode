# coding=utf-8
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# The algorithm should run in linear time and in O(1) space.

# 如何找到所有出现次数严格大于总数1 / k的数？ 提示： 保存(k – 1)个数!!!!

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        candidate1 = -99999999999999
        candidate2 = -100000000000000
        count1 = 0
        count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        return [candidate for candidate in (candidate1, candidate2) if nums.count(candidate) > len(nums) / 3]


# why count(1) will not be canceled out? because candidate2 and count2 help us protect.
# < n/3 times happens：count1 -=1; count2 -=1
nums = [1, 1, 2, 3, 4]
print Solution().majorityElement(nums)
