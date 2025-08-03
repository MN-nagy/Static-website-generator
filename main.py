from typing import List


def subset_sum(nums: List[int], target: int) -> bool:
    return find_subset_sum(nums, target, len(nums) - 1)


def find_subset_sum(nums: List[int], target: int, index: int) -> bool:
    if target == 0:
        return True
    if index < 0:
        return False
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    else:
        res1 = find_subset_sum(nums, target, index - 1)
        res2 = find_subset_sum(nums, target - nums[index], index - 1)
        if res1 == True or res2 == True:
            return True
        else:
            return False
