# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # put numbers to N + 1 buckets, for 1...N buckets, the range shape is [ ), for N + 1 bucket range shape is []
        N = len(nums)
        if N <= 1:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        max_gap = max_num - min_num
        buckets = [[] for i in xrange(N + 1)]
        for i in xrange(N):
            if nums[i] == max_num:
                idx = N
            else:
                idx = (nums[i] - min_num) * (N + 1) / (max_gap)  # a trick to avoid float division
            buckets[idx].append(nums[i])

        res = 0
        for i in xrange(1, N):  # first and last bucket must be non-empty
            if not buckets[i]:
                left_idx = i - 1
                right_idx = i + 1
                while not buckets[left_idx]:
                    left_idx -= 1
                while not buckets[right_idx]:
                    right_idx += 1
                tmp = min(buckets[right_idx]) - max(buckets[left_idx])
                if tmp > res:
                    res = tmp
                    # print sorted(nums)
                    # print max(buckets[left_idx])
                    # print min(buckets[right_idx])
        return res


nums = [15252, 16764, 27963, 7817, 26155, 20757, 3478, 22602, 20404, 6739, 16790, 10588, 16521, 6644, 20880, 15632,
        27078, 25463, 20124, 15728, 30042, 16604, 17223, 4388, 23646, 32683, 23688, 12439, 30630, 3895, 7926, 22101,
        32406, 21540, 31799, 3768, 26679, 21799, 23740]
print Solution().maximumGap(nums)
