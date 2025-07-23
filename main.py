def sum(nums):
    if not nums:
        return 0
    return nums[0] + sum(nums[1:])
