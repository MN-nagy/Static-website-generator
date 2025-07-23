def find_minimum(nums):
    if not nums:
        return None
    min_n = float("inf")
    for num in nums:
        if num < min_n:
            min_n = num
    return min_n
