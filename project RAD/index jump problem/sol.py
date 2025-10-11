from typing import List

def canJump(nums: List[int]) -> bool:
    """
    Determines if the last index can be reached using the Greedy approach.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    if n == 0:
        return False
    if n == 1:
        return True
        
    # Initialize the goal to the last index of the array
    goal = n - 1
    
    # Iterate backwards from the second-to-last element down to the first element
    for i in range(n - 2, -1, -1):
        
        # Calculate the farthest reachable index from the current position 'i'
        farthest_jump = i + nums[i]
        
        # If the farthest jump can reach or pass the current goal, 
        # then this index 'i' becomes the new, closer goal.
        if farthest_jump >= goal:
            goal = i
            
    # After the loop, if the goal has been successfully moved all the way back to 
    # the start index (0), we can reach the end.
    return goal == 0

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([2, 3, 1, 1, 4], True),  # Can reach end: 0 -> 2 -> 3 or 4
        ([3, 2, 1, 0, 4], False), # Gets stuck at index 3 (value 0)
        ([0], True),              # Trivial case, already at end
        ([1, 1, 0, 1], False),    # Gets stuck at index 2 (value 0)
        ([1, 0, 1], False),       # Gets stuck at index 1 (value 0)
        ([5, 0, 0, 0, 0], True),  # Jump from 0 directly to 4
    ]

    print("--- Jump Game (Greedy) Test Results ---")
    
    for nums, expected in test_cases:
        result = canJump(nums)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Nums: {nums} -> Can Reach End: {result}, Status: {status}")