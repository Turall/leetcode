# def canjump(nums):
#     a = nums[0]
#     length = len(nums)
#     if length % a == 0:
#         return True
#     return False


def canjump(nums):
    temp = 0
    for i, value in enumerate(nums):
        if i > temp:
            break
        temp = max(temp, i + value)
    return temp >= len(nums) - 1


arr = [2, 2, 1,  4, 9]

print(canjump(arr))
