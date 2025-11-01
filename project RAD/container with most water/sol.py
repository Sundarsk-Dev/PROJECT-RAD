from typing import List

def maxArea(height: List[int]) -> int:
    """
    Finds the maximum area of water a container can hold using the Two-Pointer Greedy method.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(height)
    if n < 2:
        return 0
    
    # 1. Initialization
    left_ptr, right_ptr = 0, n - 1
    max_area = 0
    
    # 2. Greedy Movement Loop
    while left_ptr < right_ptr:
        
        # Current dimensions
        h_L = height[left_ptr]
        h_R = height[right_ptr]
        width = right_ptr - left_ptr
        
        # Calculate current area (limited by the shorter height)
        current_area = min(h_L, h_R) * width
        
        # Update maximum area found so far
        max_area = max(max_area, current_area)
        
        # 3. Move the pointer corresponding to the shorter line (Greedy choice)
        if h_L < h_R:
            # The height limit is h_L. Move L inward, hoping for a taller line.
            left_ptr += 1
        else:
            # The height limit is h_R (or they are equal). Move R inward.
            right_ptr -= 1
            
    return max_area

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 4, 5, 18, 17, 6], 17), # Height 5 (index 3) and Height 17 (index 5). Width 2. Area 10.
                                       # Height 2 (index 0) and Height 6 (index 6). Width 6. Area 12.
                                       # Max is actually 17 (lines 18 and 17, width 1, area 17). Wait, no.
                                       # Max is [2, 3, 4, 5, 18, 17, 6]. 
                                       # Index 4 (18) and Index 6 (6). Area min(18, 6) * 2 = 12.
                                       # Index 1 (3) and Index 6 (6). Area min(3, 6) * 5 = 15.
                                       # Index 0 (2) and Index 5 (17). Area min(2, 17) * 5 = 10.
                                       # Index 1 (3) and Index 5 (17). Area min(3, 17) * 4 = 12.
                                       # Index 1 (3) and Index 4 (18). Area min(3, 18) * 3 = 9.
                                       # Index 2 (4) and Index 6 (6). Area min(4, 6) * 4 = 16. <--- Max
        ([2, 3, 4, 5, 18, 17, 6], 16) # Corrected expected value is 16
    ]

    print("--- Container With Most Water (Two-Pointer Greedy) Test Results ---")
    
    for height, expected in test_cases:
        result = maxArea(height)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Heights: {height} -> Max Area: {result}, Status: {status}")