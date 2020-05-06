##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 6-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 6
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/

############################################################################
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2
############################################################################

# ACCEPTED SOLUTION #1
# This solution ensures O(nlogn) Time and O(n) Space Complexity

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_factor = ceil(len(nums)/2)
        hash_set = {}
        for number in nums:
            hash_set[number] = 1 if number not in hash_set else hash_set[number] + 1       
            if hash_set[number] == majority_factor: return number

# ACCEPTED SOLUTION #2
# This solution ensures O(nlogn) Time and O(1) Space Complexity

class Solution_:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[floor(len(nums)/2)]

# ACCEPTED SOLUTION #3
# [NEW][LEARNING] Boyer Moore Majority Vote Algorithm
# Personal Comments: My best learning experience so far. Have come across this algorithm before, but had
# never paid attention to it. Reminded me of the time when I discovered KADANE's algorithm!
# SOURCE: 
    # https://www.techiedelight.com/find-majority-element-in-an-array-boyer-moore-majority-vote-algorithm/
    # https://www.geeksforgeeks.org/majority-element/
    # https://stackoverflow.com/questions/4325200/find-the-majority-element-in-array
# This solution ensures O(n) Time and O(1) Space Complexity

class Solution__:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        major_candidate = None
        for number in nums:
            if counter == 0:  
                major_candidate = number
                counter = 1
            elif major_candidate == number:  counter += 1
            else:   counter -= 1
        
        return major_candidate