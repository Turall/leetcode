def rmelement(nums, val):
    for i, value in enumerate(nums):
        if value == val:
            nums.remove(value)
            rmelement(nums, val)

    return len(nums)

