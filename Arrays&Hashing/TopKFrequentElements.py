"""
Top K Frequent Elements
Solved 
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]

"""

from typing import List
from collections import defaultdict, Counter
import heapq

"""My Solution"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for j in nums:
            freq[j] +=1
        sf = dict(freq)
        ordenado = sorted(sf.items(), key=lambda x: x[1], reverse=True)
        return [ i[0] for j,i in enumerate(ordenado[:k])]

"""Sorting"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
    
"""Min-Heap"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

""" Bucket Sort """

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

"""Other Solution"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        con = Counter(nums)
        ordenado = [(valor, clave) for clave, valor in con.most_common()]
        print(ordenado[0][0])
        return [ordenado[i][1] for i in range(k)]

a = Solution()
nums = [1,2,2,3,3,3,3]
k = 2
a.topKFrequent(nums,k)
