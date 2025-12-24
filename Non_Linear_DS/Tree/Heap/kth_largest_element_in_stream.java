// 703. Kth Largest Element in a Stream
// LeetCode: https://leetcode.com/problems/kth-largest-element-in-a-stream/

// Example:
// Input:
// ["KthLargest","add","add","add","add","add"]
// [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
// Output: [null,4,5,5,8,8]

import java.util.PriorityQueue;

class KthLargest {
    private PriorityQueue<Integer> pq;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        pq = new PriorityQueue<>(); // min heap

        for (int num : nums) {
            pq.offer(num);
            if (pq.size() > k) {
                pq.poll();
            }
        }
    }

    public int add(int val) {
        pq.offer(val);
        if (pq.size() > k) {
            pq.poll();
        }
        return pq.peek();
    }
}
// Time Complexity:
// Constructor: O(n log k)
// add(): O(log k)

// Space Complexity: O(k)