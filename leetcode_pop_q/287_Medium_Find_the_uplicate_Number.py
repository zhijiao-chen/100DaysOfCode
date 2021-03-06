"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
        return None

"""
solution II:
tortoise and hare
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare = tortoise = nums[0]
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if hare == tortoise:
                break
        tortoise = nums[0]
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]
        return hare