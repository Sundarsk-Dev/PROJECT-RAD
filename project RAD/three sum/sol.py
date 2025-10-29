from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in an array that sum to zero using Sorting + Two Pointers.
    
    Time Complexity: O(N^2)
    Space Complexity: O(1) (excluding output storage)
    """
    n = len(nums)
    if n < 3:
        return []
    
    # 1. Sort the array (O(N log N))
    nums.sort()
    
    results = []

    # 2. Iterate through the array with the anchor 'i'
    for i in range(n - 2): # Stop two positions before the end to allow L and R pointers
        
        # 3. Duplicate Check (Anchor 'i'): Skip if the current anchor is the same as the previous
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # Optimization: If nums[i] is already positive, the sum cannot be zero or positive.
        if nums[i] > 0:
            break
            
        # Define the target sum for the remaining two numbers
        target = 0 - nums[i]
        
        # 4. Initialize Two Pointers
        L, R = i + 1, n - 1
        
        # 5. Search Loop
        while L < R:
            current_sum = nums[L] + nums[R]
            
            if current_sum == target:
                # Found Triplet
                results.append([nums[i], nums[L], nums[R]])
                
                # Duplicate Check (Pointers): Move L and R past duplicates
                # We must use L+1 < R and R-1 > L to ensure they don't cross
                L += 1
                R -= 1
                
                while L < R and nums[L] == nums[L - 1]:
                    L += 1
                while L < R and nums[R] == nums[R + 1]:
                    R -= 1
                    
            elif current_sum < target:
                # Sum is too small, need a larger number, move left pointer right
                L += 1
            else: # current_sum > target
                # Sum is too large, need a smaller number, move right pointer left
                R -= 1
                
    return results

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([1, 2, 3, -4, -3, 0], [[-3, 0, 3], [-4, 1, 3], [-4, 2, 2], [-4, 3, 1], [-3, 1, 2], [-4, 0, 4]]),
        ([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]), 
        ([1, 2, -2, -1], []) # No sum to 0
    ]

    # Note: The expected output order may vary, but the content must match the sets.
    # The output from the function will be naturally sorted due to the implementation.
    
    print("--- 3Sum (Sorting + Two Pointers) Test Results ---")
    
    for nums, expected in test_cases:
        # Sort expected results for comparison consistency
        expected_sorted = sorted([sorted(t) for t in expected])
        
        result = threeSum(nums)
        # Sort actual results
        result_sorted = sorted([sorted(t) for t in result])
        
        status = "PASSED" if result_sorted == expected_sorted else f"FAILED (Expected: {expected_sorted}, Got: {result_sorted})"
        
        print(f"Nums: {nums} -> Result: {result}, Status: {status}")