def twosum(nums, target):
    temp = {}
    for i in range(len(nums)):
        temp[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in temp:
            if temp[target - nums[i]] != i:
                return [i, temp[target - nums[i]]]
    return []


print(twosum([3, 2, 4, 2, 3], 6))

