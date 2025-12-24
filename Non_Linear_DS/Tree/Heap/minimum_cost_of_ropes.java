// Minimum Cost of Ropes
// GeeksforGeeks: https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1

// Example 1:
// Input: [4, 3, 2, 6]
// Output: 29

// Example 2:
// Input: [4, 2, 7, 6, 9]
// Output: 62

// Example 3:
// Input: [10]
// Output: 0

import java.util.PriorityQueue;

class Solution {
    public static int minCost(int[] arr) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < arr.length; i++) {
            pq.add(arr[i]);
        }

        int ans = 0;
        while (pq.size() > 1) {
            int a = pq.poll();
            int b = pq.poll();
            ans += a + b;
            pq.add(a + b);
        }

        return ans;
    }
}

// Time Complexity: O(n log n)
// Space Complexity: O(n)
