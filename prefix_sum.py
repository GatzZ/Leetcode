# coding=utf-8
# 给定浮点数组a,求一个数组b, b[i] = a[0] * a[1] *…*a[i – 1] * a[i + 1] * …*a[n – 1],不能使用除法，不允许再开数组

#
# def prefix_product(a):
#     """
#     type a: List
#     rtype: List
#     """
#     N = len(a)
#     b = [1 for i in xrange(N)]
#     # 1. compute prefix_sum
#     for i in xrange(N):
#         b[i] = a[i] * (b[i - 1] if i > 0 else 1)
#     print a
#     print b
#     # 2. compute suffix sum
#     tmp = 1
#     for i in xrange(N - 1, -1, -1):
#         b[i] = tmp * (b[i - 1] if i > 0 else 1)
#         tmp *= a[i]
#
#     return b

def prefix_product(a):
    """
    type a: List
    rtype: List
    """
    N = len(a)
    b = [1 for i in xrange(N)]
    # 1. compute suffix sum
    for i in xrange(N - 1, -1, -1):
        b[i] = a[i] * (b[i + 1] if i != N - 1 else 1)
    # 2. compute prefix_sum
    tmp = 1
    for i in xrange(N):
        b[i] = tmp * (b[i + 1] if i != N - 1 else 1)
        tmp *= a[i]

    return b


nums = [1, 1, 2, 3, 2, 3, 5, 6]
print prefix_product(nums)

tmp = reduce(lambda a, b: a * b, nums)
for i in xrange(len(nums)):
    nums[i] = tmp / nums[i]

print nums
