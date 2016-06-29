__author__ = 'BackToLiew'


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num_idx = {}
        for i in range(len(num)):
            num_idx[num[i]] = i

        print num_idx
        for index1 in range(len(num)):
            if ((target - num[index1]) in num_idx) and (index1 != num_idx[target - num[index1]]):
                return index1 + 1, num_idx[target - num[index1]] + 1


'''
class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1

        return -1, -1
'''

num = [3, 2, 4]
target = 6
a = Solution()
result = Solution.twoSum(a, num, target)
print result
