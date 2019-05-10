def rmdub(nums):
    length = len(nums)
    if length < 2:
        return length
    temp = 0
    for i in range(length):
        if nums[temp] != nums[i]:
            temp += 1
            nums[temp] = nums[i]

    return temp + 1

