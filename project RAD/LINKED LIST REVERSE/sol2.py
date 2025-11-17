from typing import Optional

# Conceptual Singly Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverses a singly linked list iteratively using three pointers.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # 1. Initialize Pointers
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head
    
    # Iterate until we reach the end of the original list
    while curr is not None:
        
        # 1. Save Next: Temporarily store the next node
        next_node = curr.next
        
        # 2. Reverse Link: Change the current node's pointer direction
        curr.next = prev
        
        # 3. Advance Pointers: Move prev and curr one step forward
        prev = curr
        curr = next_node
        
    # When curr is None, prev is pointing to the last node processed, 
    # which is the new head.
    return prev

# --- Test Cases ---

if __name__ == "__main__":
    
    # Helper to create list from array
    def create_list(arr):
        if not arr: return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper to convert list to array for easy verification
    def list_to_array(head):
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        return arr

    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1])
    ]

    print("--- Reverse Linked List (Iterative 3-Pointer) Revision ---")
    
    for input_arr, expected_arr in test_cases:
        head = create_list(input_arr)
        new_head = reverseList(head)
        result_arr = list_to_array(new_head)
        
        status = "PASSED" if result_arr == expected_arr else f"FAILED (Expected: {expected_arr}, Got: {result_arr})"
        
        print(f"Input: {input_arr} -> Result: {result_arr}, Status: {status}")
