from typing import List

def climbStairs_optimal(n: int) -> int:
    """
    Calculates the number of distinct ways to climb n steps, where you can 
    climb 1 or 2 steps at a time. This uses the iterative Dynamic Programming 
    approach, recognizing the Fibonacci sequence pattern.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # 1. Handle Base Cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    # Base Case Initialization:
    # ways_i_minus_2 corresponds to F(n-2)
    ways_i_minus_2 = 1  # Ways to reach step 1 (F(1))
    
    # ways_i_minus_1 corresponds to F(n-1)
    ways_i_minus_1 = 2  # Ways to reach step 2 (F(2))
    
    # 2. Iterate from step 3 up to step n
    for i in range(3, n + 1):
        
        # F(n) = F(n-1) + F(n-2)
        current_ways = ways_i_minus_1 + ways_i_minus_2
        
        
        # The current F(n-1) becomes the new F(n-2)
        ways_i_minus_2 = ways_i_minus_1
        
        # The current F(n) becomes the new F(n-1)
        ways_i_minus_1 = current_ways
        
    # The final answer is stored in the last F(n-1) variable
    return ways_i_minus_1

# --- Test Cases ---

if __name__ == "__main__":
    
    test_cases = [
        (2, 2),    # n=2: (1+1), (2) -> 2 ways
        (3, 3),    # n=3: (1+1+1), (1+2), (2+1) -> 3 ways
        (4, 5),    # n=4: (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2) -> 5 ways
        (5, 8),    # n=5: F(5) = F(4) + F(3) = 5 + 3 -> 8 ways
        (10, 89),  # n=10: F(10) -> 89 ways
        (1, 1),    # Base case n=1
        (0, 0)     # Edge case n=0
    ]

    print("--- Climbing Stairs Optimal Solution Test Results ---")
    all_passed = True
    
    for n, expected in test_cases:
        result = climbStairs_optimal(n)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"n = {n}: Result = {result}, Status: {status}")
        
        if result != expected:
            all_passed = False
            
    if all_passed:
        print("\n✅ All test cases passed successfully!")
    else:

        print("\n❌ Some test cases failed.")
