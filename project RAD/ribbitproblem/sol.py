def jumpedOn(head: SinglyLinkedListNode) -> bool:
    # 1. Convert Linked List to Array
    arr = convert_list_to_array(head)
    n = len(arr)
    
    if n == 0:
        return True # Or handle as per problem spec for empty list

    # Set to track visited indices
    visited = set()
    
    # Start at index 0
    current_index = 0
    
    while current_index not in visited:
        # Add current index to visited set
        visited.add(current_index)
        
        # Check if we have successfully visited all N nodes
        if len(visited) == n:
            return True # All nodes visited

        # Get jump value (v) and calculate the next index
        jump_value = arr[current_index]
        
        # Apply the jump rule: (i + v) mod n
        # Note: In Python, % handles negative numbers correctly for cyclic indices
        next_index = (current_index + jump_value) % n 
        
        # Move to the next index
        current_index = next_index
        
    # If the loop breaks because current_index is already in visited,
    # it means a cycle was found before all nodes were visited.
    return False

# Time Complexity: O(N) for conversion and O(N) for the single-pass cycle check. Total O(N).
# Space Complexity: O(N) to store the array and the visited set.
