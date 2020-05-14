##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 14-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 14
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3329/

############################################################################
# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
############################################################################

# ACCEPTED SOLUTION #1
# Personal Comments: Had always coded Tries purely in C++-14
# But coding it out in Python was wuite liberating!
# Was quite disappointed seeing everyone use Python Dictionaries for NEW NODE
# and LeetCode not having good cases to test that out.
# [NEW-LEARNING][SOURCE]: https://www.geeksforgeeks.org/trie-insert-and-search/

class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
        self.is_end_of_world = False

class Trie:
    get_index = lambda x: ord(x) - ord('a')
    get_node = lambda: TrieNode()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.get_node()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ite = self.root
        for alphabet in [Trie.get_index(character) for character in word]:
            if not ite.children[alphabet]:  ite.children[alphabet] = Trie.get_node()
            ite = ite.children[alphabet]
        ite.is_end_of_world = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ite = self.root
        for alphabet in [Trie.get_index(character) for character in word]:
            if not ite.children[alphabet]:  return False
            ite = ite.children[alphabet]
        return ite != None and ite.is_end_of_world 
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ite = self.root
        for alphabet in [Trie.get_index(character) for character in prefix]:
            if not ite.children[alphabet]:  return False
            ite = ite.children[alphabet]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



# ACCEPTED SOLUTION #2
# Personal Comments: 
# Using Python Dictionaries for CHILDREN ARRAY for NEW NODE
# Since alphabets are only 26, small trade off for LOOKUP Time
# will make code more readable

class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.is_end_of_world = False

class Trie:
    get_node = lambda: TrieNode()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.get_node()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ite = self.root
        for alphabet in word:
            if alphabet not in ite.children:  ite.children[alphabet] = Trie.get_node()
            ite = ite.children[alphabet]
        ite.is_end_of_world = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ite = self.root
        for alphabet in word:
            if alphabet not in ite.children:  return False
            ite = ite.children[alphabet]
        return ite != None and ite.is_end_of_world 
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ite = self.root
        for alphabet in prefix:
            if alphabet not in ite.children:  return False
            ite = ite.children[alphabet]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)