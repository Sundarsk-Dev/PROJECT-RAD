import java.util.PriorityQueue;

class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }
}

public class MergeKSortedLists {

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0)
            return null;

        // Min-heap: order by node value
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);

        // 1. Insert the head of each list into the heap
        for (ListNode head : lists) {
            if (head != null) {
                minHeap.offer(head);
            }
        }

        // Dummy node to simplify result construction
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        // 2. Process heap until empty
        while (!minHeap.isEmpty()) {
            // Extract smallest node
            ListNode node = minHeap.poll();

            // Append it to the merged list
            current.next = node;
            current = current.next;

            // If that node has a next, push it into the heap
            if (node.next != null) {
                minHeap.offer(node.next);
            }
        }

        return dummy.next;
    }

    // Helper functions to test
    public static ListNode arrayToList(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (int val : arr) {
            curr.next = new ListNode(val);
            curr = curr.next;
        }
        return dummy.next;
    }

    public static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + (head.next != null ? " -> " : ""));
            head = head.next;
        }
        System.out.println();
    }

    // --- Test the Implementation ---
    public static void main(String[] args) {
        ListNode l1 = arrayToList(new int[] { 1, 4, 5 });
        ListNode l2 = arrayToList(new int[] { 1, 3, 4 });
        ListNode l3 = arrayToList(new int[] { 2, 6 });

        ListNode[] lists = new ListNode[] { l1, l2, l3 };

        MergeKSortedLists solution = new MergeKSortedLists();
        ListNode result = solution.mergeKLists(lists);

        System.out.println("--- Merge K Sorted Lists (Min-Heap) ---");
        printList(result); // Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
    }
}
