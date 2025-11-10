"""Valid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false"""

"""My Solution"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        an1 = {}
        an2 = {}
        if len(s) != len(t):
            return False
        for i,j in enumerate(s):
            if j not in an1:
                an1[j] = 1
            if j in an1:
                an1[j] += 1
            if t[i] not in an2:
                an2[t[i]] = 1
            if j in an1:
                an2[t[i]] += 1
        if an1 != an2:
            return False
        return True
    
"""Sorting"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
"""Hash Map"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
"""Hash Table (Using Array)"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True