from typing import List

def find_peak_element(nums: List[int]) -> int:
    """
    Finds the index of a peak element in an array using a modified Binary Search 
    (O(log n) time complexity).
    """
    n = len(nums)
    if n == 1:
        return 0
    
    left, right = 0, n - 1
    
    # The loop condition is strictly 'left < right'
    while left < right:
        mid = left + (right - left) // 2
        
        # Compare current element with its RIGHT neighbor
        
        # Case 1: Ascending Slope (nums[mid] < nums[mid + 1])
        # The peak must be further to the right. Discard the left half.
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
            
        # Case 2: Descending/Flat Slope (nums[mid] > nums[mid + 1])
        # The peak is either nums[mid] or somewhere in the left half.
        # We keep mid as a potential answer, so we discard the elements after mid.
        else:
            right = mid
            
    # When left == right, we have converged on a peak index
    return left

# --- Test Cases ---

if __name__ == "__main__":
    solver = find_peak_element
    
    test_cases = [
        ([1, 2, 3, 1], 2),      # Peak at index 2 (value 3)
        ([1, 2, 1, 3, 5, 6, 4], 5), # Two peaks (2 or 5). Should return 5
        ([1, 5, 1, 2, 1], 1),   # Peak at index 1 (value 5)
        ([10], 0),              # Single element array
        ([1, 2], 1),            # Peak at index 1 (value 2)
        ([2, 1], 0)             # Peak at index 0 (value 2)
    ]

    print("--- Find Peak Element Test Results ---")
    all_passed = True
    
    # Note: We only check if the returned index is *a* peak, not if it matches the expected index exactly
    for nums, expected_peak_index in test_cases:
        result_index = solver(nums)
        
        # Validation: Check if the element at result_index is actually a peak
        is_peak = True
        result_value = nums[result_index]
        n = len(nums)
        
        # Check left neighbor
        if result_index > 0 and nums[result_index - 1] > result_value:
            is_peak = False
        
        # Check right neighbor
        if result_index < n - 1 and nums[result_index + 1] > result_value:
            is_peak = False
        
        status = "PASSED" if is_peak else f"FAILED (Index {result_index} is not a peak)"
        
        print(f"Array: {nums} -> Index: {result_index} (Value: {result_value}), Status: {status}")
        
        if not is_peak:
            all_passed = False
            
    if all_passed:
        print("\n✅ All test cases passed successfully!")
    else:
        print("\n❌ Some test cases failed.")