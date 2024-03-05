"""
Contains Duplicate I

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

https://leetcode.com/problems/contains-duplicate/description/

"""
nums = [1, 1, 2, 3, 4, 5]


def contains_duplicate(nums):
    nums_map = {}
    for num in nums:
        if num in nums_map.values():
            return True
        else:
            nums_map[nums.index(num)] = num
    return False


print(contains_duplicate(nums))

