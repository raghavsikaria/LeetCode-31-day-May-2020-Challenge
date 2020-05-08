##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 8-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 8
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/

############################################################################
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Example 1:

# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Example 2:

# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
 
# Constraints:

# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.
############################################################################

# ACCEPTED SOLUTION
# This solution ensures O(n) Time and O(1) Space Complexity
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        answer = True
        if not len(coordinates) == 2:
            p1 = coordinates[0]
            p2 = coordinates[1]
            if p2[0] == p1[0]:  answer = all([False for p in coordinates if p[0] != p1[0]])
            else:
                slope = float((p2[1] - p1[1])/(p2[0] - p1[0]))
                for point in coordinates[2:]:
                    if float(point[1] - p1[1]) != slope * (point[0] - p1[0]):
                        answer = False
                        break
            
        return answer