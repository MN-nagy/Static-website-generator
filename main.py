def sum(nums):
    return 0 if not nums else nums[0] + sum(nums[1:])
