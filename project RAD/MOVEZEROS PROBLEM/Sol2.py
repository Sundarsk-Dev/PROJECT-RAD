from typing import List

def moveZeroes_Swapping(nums: List[int]) -> None:
    """
    Moves all zeroes to the end of the array in-place using the Swapping Two-Pointer method.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    
    # last_non_zero_found_at acts as the "write" pointer for non-zero numbers.
    last_non_zero_found_at = 0
    n = len(nums)
    
    # Iterate with 'i' (the "read" pointer)
    for i in range(n):
        # If we find a non-zero element
        if nums[i] != 0:
            # If i and last_non_zero_found_at are the same, no swap is needed, 
            # but the assignment/swap is safe.
            if i != last_non_zero_found_at:
                # Swap the non-zero element with the element at the "write" position.
                # The element at last_non_zero_found_at will be a zero (or a non-zero 
                # that has already been correctly placed).
                nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
            
            # Increment the position where the next non-zero element should be placed.
            last_non_zero_found_at += 1

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 0, 1], [1, 0, 0, 0]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([0], [0]),
        ([1, 0], [1, 0])
    ]

    print("--- MOVE ZEROS (Swapping Two-Pointer) Revision ---")
    
    for input_nums, expected in test_cases:
        # Create a copy since the function modifies the list in-place
        nums_copy = list(input_nums)
        moveZeroes_Swapping(nums_copy)
        
        status = "PASSED" if nums_copy == expected else f"FAILED (Expected: {expected}, Got: {nums_copy})"
        
        print(f"Input: {input_nums} -> Result: {nums_copy}, Status: {status}")
