// Node structure
class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}

// Utility class
class LinkedListUtility {

    public ListNode reverseList(ListNode head) {
        ListNode previous = null;
        ListNode current = head;

        while (current != null) {
            // Step 1: Save next
            ListNode nextNode = current.next;

            // Step 2: Reverse pointer
            current.next = previous;

            // Step 3: Move previous
            previous = current;

            // Step 4: Move current
            current = nextNode;
        }

        return previous; // new head
    }

    // Print helper
    public void printList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " -> ");
            current = current.next;
        }
        System.out.println("NULL");
    }

    // Main execution
    public static void main(String[] args) {
        LinkedListUtility util = new LinkedListUtility();

        // Build list: 1->2->3->4->5->NULL
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        System.out.println("Original List:");
        util.printList(head);

        // Reverse
        ListNode newHead = util.reverseList(head);

        System.out.println("Reversed List:");
        util.printList(newHead);
    }
}
