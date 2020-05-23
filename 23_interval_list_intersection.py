##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 23-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 23
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/

############################################################################
# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

# Example 1:



# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

# Note:

# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
############################################################################

# ACCEPTED SOLUTION
# Quite the generic solution it seems!
# Everyone seems to have submitted the exact same code in different languages!
# Ensures O(n) Time and O(1) Space complexity

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        l_a = len(A)
        l_b = len(B)
        i,j = 0,0
        answer = []
        while i < l_a and j < l_b:
            if (A[i][0] <= B[j][0] and A[i][1] >= B[j][0]) or (A[i][0] >= B[j][0] and A[i][0] <= B[j][1]):  answer.append([max(A[i][0],B[j][0]),min(A[i][1],B[j][1])])
            if A[i][1] <= B[j][1]:  i+=1
            else:   j+=1
        return answer




# MORE SOLUTIONS FROM OTHER SUBMISSIONS:
# I got this solution from the submissions detail page
# Quite a different approach, really loved the variety
# considering almost all solutions were same
# Don't know the author!

from collections import deque

class Solution:
    
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        
        a_intervals = deque(A)
        b_intervals = deque(B)
        
        intersections = []
        
        a = a_intervals.popleft()
        b = b_intervals.popleft()
        
        while a and b:
            a_start, a_end = a[0], a[1]
            b_start, b_end = b[0], b[1]
            
            max_start = max(a_start, b_start)
            min_end = min(a_end, b_end)
        
            if max_start <= min_end:
                intersections.append([max_start, min_end])
            
            '''pop the one with the min end'''
            if a_end < b_end:
                if not a_intervals:
                    break
                a = a_intervals.popleft()
            else:
                if not b_intervals:
                    break
                b = b_intervals.popleft()
                
        return intersections