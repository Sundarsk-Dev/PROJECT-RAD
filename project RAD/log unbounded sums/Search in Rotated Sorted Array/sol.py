from typing import List

def search(nums:List[int],target:int)-> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2


        if nums[mid] == target:
            return mid


        

        if nums[low] <= nums[mid]:
            
       
            if nums[low] <= target < nums[mid]:
       
                high = mid - 1
            else:
                
                low = mid + 1
        

        else: # nums[low] > nums[mid], meaning the rotation point is in the left half
            
            # Check if the target is within the sorted RIGHT HALF's range
            if nums[mid] < target <= nums[high]:
                # Target is here, discard the left half
                low = mid + 1
            else:
                # Target must be in the UNSORTED LEFT HALF
                high = mid - 1
                
    # Target not found
    return -1
    

if __name__ == "__main__":
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),      # Target in right half (after pivot)
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),     # Target not present
        ([4, 5, 6, 7, 0, 1, 2], 6, 2),      # Target in left half (before pivot)
        ([1, 3], 3, 1),                     # Small array
        ([3, 1], 1, 1),                     # Small array rotated
        ([1], 1, 0),                        # Single element
        ([5, 1, 3], 3, 2),                  # Target at the end
        ([7, 8, 1, 2, 3, 4, 5, 6], 1, 2)    # Large array, target near pivot
    ]

    print("--- Search in Rotated Sorted Array (Modified Binary Search) Test Results ---")
    
    for nums, target, expected in test_cases:
        result = search(nums, target)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Nums: {nums}, Target: {target} -> Index: {result}, Status: {status}")