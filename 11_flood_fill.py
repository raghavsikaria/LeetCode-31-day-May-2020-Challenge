##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 11-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 11
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/

############################################################################
# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

# Example 1:
# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
# Note:

# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
############################################################################

# ACCEPTED SOLUTION #1
# RECURSION - FLOOD FILL
# This solution ensures O(n^2) Time and O(n^2) Space Complexity
# Although it's a linear function of n^2 Time, as same node
# might be visited multiple times
# NOTE: Space complexity perhaps needs more analysis
# Since all recursion calls are maintained in recursion
# stack in memory
class Solution:
    def flood_fill_util(self,m,x,y,new_color,old_color,nr,nc):
        if x < 0 or x >= nr or y < 0 or y >= nc or m[x][y] != old_color or m[x][y] == new_color:    return
        m[x][y] = new_color
        self.flood_fill_util(m,x-1,y,new_color,old_color,nr,nc)
        self.flood_fill_util(m,x+1,y,new_color,old_color,nr,nc)
        self.flood_fill_util(m,x,y-1,new_color,old_color,nr,nc)
        self.flood_fill_util(m,x,y+1,new_color,old_color,nr,nc)        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, columns = len(image),len(image[0])
        old_color = image[sr][sc]
        self.flood_fill_util(image,sr,sc,newColor,old_color,rows,columns)
        return image

# ACCEPTED SOLUTION #2
# ITERATION - BFS
# This solution ensures O(n^2) Time and O(n^2) Space Complexity
class Solution_:                
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        nr, nc = len(image),len(image[0])
        old_color = image[sr][sc]
        
        possible_neighbours = [[0,1],[0,-1],[1,0],[-1,0]]
        q = [[sr,sc]]
        image[sr][sc] = newColor
        while(q != []):
            parent_node = q[0]
            q.pop(0)
            
            for n in possible_neighbours:
                x = parent_node[0] + n[0]
                y = parent_node[1] + n[1]
                
                if not (x < 0 or x >= nr or y < 0 or y >= nc or image[x][y] != old_color or image[x][y] == newColor):
                    image[x][y] = newColor
                    q.append([x,y])
        
        return image