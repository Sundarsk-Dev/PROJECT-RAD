class Solution {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public boolean jumpedOn(ListNode head) {
        // Step 1: Convert Linked List to Array
        int[] arr = toArray(head);
        int n = arr.length;

        if (n == 0) return true;

        boolean[] visited = new boolean[n];

        int current = 0;
        int visitCount = 0;

        while (!visited[current]) {
            visited[current] = true;
            visitCount++;

            if (visitCount == n) {
                return true;  // visited all nodes
            }

            int jump = arr[current];
            current = mod(current + jump, n);
        }

        // If we reached a visited index early → bad cycle
        return false;
    }

    // Helper: Convert linked list to array
    private int[] toArray(ListNode head) {
        java.util.ArrayList<Integer> list = new java.util.ArrayList<>();
        ListNode curr = head;
        while (curr != null) {
            list.add(curr.val);
            curr = curr.next;
        }
        // convert List<Integer> → int[]
        return list.stream().mapToInt(i -> i).toArray();
    }

    // Proper modulo for negative values
    private int mod(int a, int n) {
        int r = a % n;
        return r < 0 ? r + n : r;
    }
}
