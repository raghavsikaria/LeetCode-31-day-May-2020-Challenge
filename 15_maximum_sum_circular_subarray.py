##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 15-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 15
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/

############################################################################
# Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

# Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

# Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)


# Example 1:

# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
# Example 2:

# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
# Example 3:

# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
# Example 4:

# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
# Example 5:

# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
 

# Note:

# -30000 <= A[i] <= 30000
# 1 <= A.length <= 30000
############################################################################

# ACCEPTED SOLUTION
# [NEW-LEARNING][SOURCE]: 
#   https://www.geeksforgeeks.org/maximum-contiguous-circular-sum/
#   https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/633058/Java-or-C%2B%2B-or-Python3-or-With-detailed-explanation-or-O(N)-time-or-O(1)
# [Personal Comments]: This has to be my best learning so far!
# After knowing Kadane's Algorithm for 5 years, the question took me
# right back to school. The beautiful solution/explanation by logan138
# in the above LeetCode link is enlightening to say the least.
# I am all praises to the brilliance of this solution.

class Solution:
    def get_max_and_min_subarray_sum(self,array):
        # KADANE'S ALGORITHM
        local_max, global_max = array[0], array[0]
        local_min, global_min = array[0], array[0]
        sum_of_array = array[0]
        
        for number in array[1:]:
            local_max = max(number,number+local_max)
            global_max = max(global_max,local_max)

            local_min = min(number,number+local_min)
            global_min = min(global_min,local_min)
            
            sum_of_array += number

        return global_max, global_min, sum_of_array
        
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_sum, min_sum, sum_array = self.get_max_and_min_subarray_sum(A)
        answer = max_sum if sum_array == min_sum else max(sum_array-min_sum,max_sum)
        return answer