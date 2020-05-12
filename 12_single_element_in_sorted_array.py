##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 12-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 12
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/

############################################################################
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

# Example 1:

# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: [3,3,7,7,10,11,11]
# Output: 10
 

# Note: Your solution should run in O(log n) time and O(1) space.
############################################################################

# ACCEPTED SOLUTION #1
# This solution ensures O(n) Time and O(1) Space Complexity
# XOR Approach
# NOTE: But here we don't make use of the information
# that the Array is sorted
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        answer = 0
        for i in nums:   answer ^= i
        return answer

# ACCEPTED SOLUTION #2
# MODIFIED Binary Search
# PERSONAL COMMENTS: Had never modified a Binary Search for 
# this type of use. Blew my mind completely.
# [NEW LEARNING][SOURCE]: https://www.geeksforgeeks.org/find-the-element-that-appears-once-in-a-sorted-array/
class Solution_:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        answer = -1
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            if low == high: 
                answer = nums[low]
                break
            mid = low + (high - low)//2
            if mid%2 == 0:
                if nums[mid] == nums[mid+1]:    low = mid + 2
                else:   high = mid
            else:
                if nums[mid] == nums[mid-1]:    low = mid + 1
                else:   high = mid - 1
        return answer