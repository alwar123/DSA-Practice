# Kth Smallest Element
# GeeksforGeeks : https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1

# Example 1:
# Input: arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
# Output: 5

# Example 2:
# Input: arr = [7, 10, 4, 3, 20, 15], k = 3
# Output: 7

import heapq

class Solution:
    def kthSmallest(self, arr, k):
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, arr[i])

        for _ in range(k - 1):
            heapq.heappop(heap)

        return heap[0]
