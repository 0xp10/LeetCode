'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''
# First solution
def containsDuplicate(nums:list)-> bool:
    mySet = set()
    for i in nums:
        if i in mySet:
            return True
        else:
            mySet.add(i)

print(containsDuplicate([1,1]))

# Second soulution
def containsDuplicate(nums:list)-> bool:
    return len(nums) != len(set(nums))

print(containsDuplicate([1,1]))
