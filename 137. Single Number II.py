# coding=utf-8
#  Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 三进制异或？

        # 解法一：
        # 其实异或运算的本质就是 求和 % base。 比如 1 ^ 1 = 0  其实就是 (1+1) % 2 = 0。
        # 因此只要按位求和，最后再将每位结果 模除 3，再转换为二进制即是答案x。
        # 但是这样需要用到O(digits）的额外内存
        d = [0 for i in xrange(32)]
        for x in nums:
            for j in xrange(32):
                if (((1 << j) & x) > 0):
                    d[j] += 1
        ans = 0
        for j in xrange(32):
            t = d[j] % 3
            if (t == 1):
                ans = ans + (1 << j)
            elif (t != 0):
                return -1
        return ans


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 三进制异或？

        # 解法二：
        #     这个算法是有改进的空间的，可以使用掩码变量：
        #
        # ones   代表第ith 位只出现一次的掩码变量
        # twos  代表第ith 位只出现两次次的掩码变量
        # threes  代表第ith 位只出现三次的掩码变量

        ones, twos, threes = 0, 0, 0
        for num in nums:
            # 1.在读入num之前已经出现了一次，且跟num上为1的位相同；2.或者之前出现两次，且跟num上为1的位不同 -> 出现两次
            twos |= ones & num
            # 1.在读入num之前已经出现了一次，且跟num上为1的位不同；2.或者之前没出现，读入num出现了 -> 出现一次
            ones ^= num
            threes = ones & twos
            # 对于ones 和 twos 把出现了3次的位置设置为0 （取反之后1的位置为0）
            ones &= ~threes
            twos &= ~threes
        return ones
