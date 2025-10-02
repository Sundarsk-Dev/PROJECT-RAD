from typing import List

class RotatedArraySearch:
    """
    Implements the modified Binary Search algorithm to find a target 
    in a rotated sorted array in O(log n) time complexity.
    """
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        
        # Binary Search loop
        while left <= right:
            mid = left + (right - left) // 2
            
            # Case 1: Target found
            if nums[mid] == target:
                return mid
            
            # Case 2: Determine which side is sorted
            
            # Is the left side sorted? (nums[left] to nums[mid])
            if nums[left] <= nums[mid]:
                
                # Check if the target is within the sorted left half
                if nums[left] <= target < nums[mid]:
                    # Target is in the sorted left half, so eliminate the right half
                    right = mid - 1
                else:
                    # Target is not in the sorted left half, so it must be in the right (unsorted) half
                    left = mid + 1
            
            # Else: The right side must be sorted (nums[mid] to nums[right])
            else: 
                
                # Check if the target is within the sorted right half
                if nums[mid] < target <= nums[right]:
                    # Target is in the sorted right half, so eliminate the left half
                    left = mid + 1
                else:
                    # Target is not in the sorted right half, so it must be in the left (unsorted) half
                    right = mid - 1
        
        # If the loop completes, the target was not found
        return -1

# --- Example Execution ---
if __name__ == "__main__":
    solver = RotatedArraySearch()
    
    # Example 1: Target is in the sorted portion of the right half
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 1
    result1 = solver.search(nums1, target1)
    print(f"Array: {nums1}, Target: {target1} -> Index: {result1}") # Output: 5
    
    # Example 2: Target is in the sorted portion of the left half
    nums2 = [6, 7, 0, 1, 2, 3, 4, 5]
    target2 = 7
    result2 = solver.search(nums2, target2)
    print(f"Array: {nums2}, Target: {target2} -> Index: {result2}") # Output: 1
    
    # Example 3: Target not found
    nums3 = [11, 13, 15, 17]
    target3 = 12
    result3 = solver.search(nums3, target3)
    print(f"Array: {nums3}, Target: {target3} -> Index: {result3}") # Output: -1

    # Example 4: Edge case - target is the pivot/start of the array
    nums4 = [3, 1]
    target4 = 1
    result4 = solver.search(nums4, target4)
    print(f"Array: {nums4}, Target: {target4} -> Index: {result4}") # Output: 1