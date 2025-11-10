"""
Group Anagrams
Solved 
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
"""
from typing import List
from collections import defaultdict

# """My Solution"""
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         sorte = ["".join(sorted(i)) for i in strs]
#         dict_s = {}
#         for i, n in enumerate(sorte):
#             if n not in dict_s:
#                 dict_s[n] = [strs[i]]
#             else:
#                 dict_s[n].append(strs[i])
#         return list(dict_s.values())
    
# """Sorting"""

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             sortedS = ''.join(sorted(s))
#             res[sortedS].append(s)
#         return list(res.values())

"""Hash Table"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

a = Solution()
strs = ["act","pots","tops","cat","stop","hat"]

a.groupAnagrams(strs=strs)