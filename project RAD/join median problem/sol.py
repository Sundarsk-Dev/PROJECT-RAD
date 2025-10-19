from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Finds the median of two sorted arrays using binary search on the partition.
    
    Time Complexity: O(log(min(M, N)))
    Space Complexity: O(1)
    """
    
    # Ensure nums1 is the shorter array (M <= N) to minimize the binary search space
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    
    m, n = len(nums1), len(nums2)
    
    # 'k' is the required length of the left partition in the conceptual merged array
    # If M+N is odd, we need k = (M+N+1)//2 elements on the left.
    # If M+N is even, we need k = (M+N)//2 elements on the left.
    half_len = (m + n + 1) // 2 
    
    # Binary search range for the partition index 'i' in nums1
    low, high = 0, m
    
    while low <= high:
        # i is the partition index in nums1 (number of elements on the left side)
        i = (low + high) // 2
        # j is the required partition index in nums2
        j = half_len - i
        
        # Define the four boundary elements for checking the partition
        # Use -float('inf') and float('inf') to handle boundary conditions (i=0, i=M, j=0, j=N)
        
        # LeftMaxes
        left_max1 = nums1[i-1] if i > 0 else -float('inf')
        left_max2 = nums2[j-1] if j > 0 else -float('inf')
        
        # RightMins
        right_min1 = nums1[i] if i < m else float('inf')
        right_min2 = nums2[j] if j < n else float('inf')
        
        # Condition Check for Perfect Partition: LeftMax <= RightMin
        if left_max1 <= right_min2 and left_max2 <= right_min1:
            # PERFECT PARTITION FOUND!
            
            # The median is derived from the boundary elements:
            
            # 1. Left Max: The maximum of the left partition is the larger of the two LeftMaxes
            max_left = max(left_max1, left_max2)
            
            # If total length is odd, the median is the Max Left element
            if (m + n) % 2 == 1:
                return float(max_left)
            
            # 2. Right Min: The minimum of the right partition is the smaller of the two RightMins
            min_right = min(right_min1, right_min2)
            
            # If total length is even, the median is the average of Max Left and Min Right
            return (max_left + min_right) / 2.0
        
        # Adjust binary search space
        elif left_max1 > right_min2:
            # nums1's left max is too big. Move i to the left.
            high = i - 1
        else: # left_max2 > right_min1
            # nums1's left max is too small (meaning nums2's left max is too big). Move i to the right.
            low = i + 1

    return 0.0 # Should not be reached if inputs are valid

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([1, 3], [2], 2.0),                        # Odd total length
        ([1, 2], [3, 4], 2.5),                     # Even total length
        ([0, 0], [0, 0], 0.0),                     # All same
        ([], [1], 1.0),                            # One empty
        ([100], [1, 2, 3, 4, 5], 3.5),             # Larger element in shorter array
        ([1, 2, 3, 4, 5], [100], 3.5),             # Symmetric test
    ]

    print("--- Median of Two Sorted Arrays (Binary Search) Test Results ---")
    
    for nums1, nums2, expected in test_cases:
        result = findMedianSortedArrays(nums1, nums2)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Nums1: {nums1}, Nums2: {nums2} -> Median: {result}, Status: {status}")miz.pro")