'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

def twoSum(nums:list,target:int)-> list[int]:
    calcSum = 0
    dicResult = {}

    for i in range(len(nums)):
        calcSum = target - nums[i]
        if calcSum in dicResult:
            return [dicResult[calcSum],i]
        dicResult[nums[i]] = i
    return []

print(twoSum([1,2,3,4,5],9))