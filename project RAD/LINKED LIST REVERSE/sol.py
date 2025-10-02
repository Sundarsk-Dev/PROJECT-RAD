from typing import Optional
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next = next
class LinkedListUtility:
    def reverseList(self,head:Optional[ListNode])->Optional[ListNode]:
        previous=None
        current=head
        while current:
            next_node =current.next
            current.next=previous
            previous = current
            current = next_node
            print(f"Reversed Node: {previous.val} -> New Next: {previous.next.val if previous.next else 'NULL'}")
        return previous
def printList(head: Optional[ListNode]):
    """Prints the linked list from head to tail."""
    current = head
    output = []
    while current:
        output.append(str(current.val))
        current = current.next
    print("List: " + " -> ".join(output) + " -> NULL")


# --- Main Execution ---
if __name__ == "__main__":
    
    # 1. Setup the initial list: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    solver = LinkedListUtility()
    
    print("=" * 40)
    print("  Problem: Reverse a Linked List")
    print("=" * 40)
    
    print("Original List State:")
    printList(head)
    
    # 2. Perform the reversal
    new_head = solver.reverseList(head)
    
    # 3. Print the result
    print("\nFinal List State:")
    printList(new_head)
    print("=" * 40)

