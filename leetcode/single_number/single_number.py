import collections


def singleNumber(nums):
    length = len(nums)
    if length == 1 and nums[0] > 0:
        return 1
    if length == 1 and nums[0] < 0:
        return -1
    temp = collections.defaultdict(list)
    for s in nums:
        temp[s].append(s)
    for i in nums:
        if len(temp[i]) == 1:
            return i


print(singleNumber([-1, -1, -2]))

