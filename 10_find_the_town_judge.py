##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 10-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 10
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/

############################################################################
# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

# Example 1:

# Input: N = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# Example 4:

# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1
# Example 5:

# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
 

# Note:

# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N
############################################################################

# ACCEPTED SOLUTION
# This solution ensures O(n) Time and O(n) Space Complexity
# Not a fan of this solution, and if I keep Space Complexity as O(1)
# needless to say, I'll be raising Time Complexity to atleast O(nlogn)
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        answer = -1
        if trust == []: answer = 1
        else:
            candidate = [0]*(N+1)
            for ele in trust:   
                candidate[ele[0]] = -2
                if candidate[ele[1]] != -2: candidate[ele[1]] += 1

            for index,ele in enumerate(candidate):
                if ele == N-1:  
                    answer = index
                    break
        return answer