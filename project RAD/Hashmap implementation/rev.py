from typing import List

def twoSum_Sorted(numbers: List[int], target: int) -> List[int]:
    """
    Finds the two indices that sum to the target in a SORTED array 
    using the Two-Pointer technique.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    
    # 1. Initialization (0-based indices)
    left_ptr, right_ptr = 0, len(numbers) - 1
    
    while left_ptr < right_ptr:
        current_sum = numbers[left_ptr] + numbers[right_ptr]
        
        if current_sum == target:
            # Found: Return 1-based indices
            return [left_ptr + 1, right_ptr + 1]
        
        elif current_sum < target:
            # Sum is too small, move left pointer to increase the sum
            left_ptr += 1
        
        else: # current_sum > target
            # Sum is too large, move right pointer to decrease the sum
            right_ptr -= 1
            
    # Per constraints, this line should not be reached.
    return []

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]) # [4, 4] at 1-based indices 4 and 5
    ]

    print("--- Two Sum II (Two Pointers on Sorted Array) Test Results ---")
    
    for numbers, target, expected in test_cases:
        result = twoSum_Sorted(numbers, target)
        
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Numbers: {numbers}, Target: {target} -> Indices: {result}, Status: {status}")
