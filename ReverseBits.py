__author__ = 'BackToLiew'


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)


n = 2
a = Solution()
print a.reverseBits(2)

# return int(bin(n)[2:].zfill(32)[::-1], 2)
