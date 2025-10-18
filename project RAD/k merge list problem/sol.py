import heapq
from typing import List, Optional, Tuple

# --- 1. Linked List Definition ---

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- 2. Main Solution Function ---

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges K sorted linked lists using a Min-Heap (Priority Queue).
    
    Time Complexity: O(N log K), where N is the total number of nodes and K is the number of lists.
    Space Complexity: O(K) for the heap.
    """
    if not lists:
        return None

    # Min-Heap stores: (node_value, unique_id, node_object)
    # The unique_id is necessary for comparison stability if node objects themselves are not comparable
    min_heap: List[Tuple[int, int, ListNode]] = []
    unique_id = 0

    # 1. Initial Fill: Insert the head of every non-empty list into the heap
    for head in lists:
        if head:
            # heapq is a min-heap, we push the value and the node object
            heapq.heappush(min_heap, (head.val, unique_id, head))
            unique_id += 1
            
    # Dummy node to start building the result list
    dummy = ListNode(0)
    current = dummy

    # 2. Extraction and Insertion Loop
    while min_heap:
        
        # Extract the node with the smallest value
        val, _, node = heapq.heappop(min_heap)
        
        # Append the extracted node to the result list
        current.next = node
        current = current.next
        
        # Check if the extracted node has a successor in its original list
        if node.next:
            # Insert the next node into the heap
            heapq.heappush(min_heap, (node.next.val, unique_id, node.next))
            unique_id += 1
            
    # The merged list starts from the dummy node's next pointer
    return dummy.next

# --- 3. Helper Functions for Testing ---

def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Converts a Python list to a linked list."""
    if not arr:
        return None
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Converts a linked list back to a Python list."""
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

# --- 4. Test Cases ---

if __name__ == "__main__":
    
    # Input lists as Python arrays
    list1 = [1, 4, 5]
    list2 = [1, 3, 4]
    list3 = [2, 6]
    
    # Convert arrays to Linked Lists
    l1 = list_to_linked_list(list1)
    l2 = list_to_linked_list(list2)
    l3 = list_to_linked_list(list3)

    test_lists = [l1, l2, l3]
    expected_result = [1, 1, 2, 3, 4, 4, 5, 6]

    print("--- Merge K Sorted Lists Test ---")
    print(f"Input Lists (as arrays): {list1}, {list2}, {list3}")
    
    merged_head = mergeKLists(test_lists)
    actual_result = linked_list_to_list(merged_head)
    
    status = "PASSED" if actual_result == expected_result else "FAILED"
    
    print(f"Expected Result: {expected_result}")
    print(f"Actual Result:   {actual_result}")
    print(f"Status: {status}")
    
    # Test Case 2: Empty lists and single elements
    test_lists_2 = [
        list_to_linked_list([]), 
        list_to_linked_list([10]), 
        list_to_linked_list([5, 15])
    ]
    expected_result_2 = [5, 10, 15]
    
    merged_head_2 = mergeKLists(test_lists_2)
    actual_result_2 = linked_list_to_list(merged_head_2)
    
    status_2 = "PASSED" if actual_result_2 == expected_result_2 else "FAILED"
    
    print("\n--- Test Case 2 ---")
    print(f"Expected Result: {expected_result_2}")
    print(f"Actual Result:   {actual_result_2}")
    print(f"Status: {status_2}")