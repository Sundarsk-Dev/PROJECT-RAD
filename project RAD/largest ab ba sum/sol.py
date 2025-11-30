from typing import List
from functools import cmp_to_key

def largestNumber(nums: List[int]) -> str:
    """
    Arranges a list of integers to form the largest possible number using a custom comparator.
    
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    # 1. Convert all numbers to strings
    s_nums = [str(x) for x in nums]

    # Define the custom comparison logic
    def compare_func(x: str, y: str) -> int:
        """
        Custom comparator: Returns a negative value if x comes before y, 
        a positive value if y comes before x, and 0 if they are equal.
        
        We want to sort in DECREASING order based on the string (y + x) vs (x + y).
        If (y + x) > (x + y), it means y should come first, so we return a POSITIVE value.
        Python's cmp_to_key sorts based on the return value:
        - Negative: x comes first
        - Positive: y comes first (which means we want y - x to be positive)
        
        We use y+x vs x+y to reverse the default sort order for decreasing magnitude.
        """
        if x + y > y + x:
            return -1  # x should come first (x > y)
        elif x + y < y + x:
            return 1   # y should come first (y > x)
        else:
            return 0

    # 2. Sort the list of strings using the custom comparator
    # cmp_to_key converts the old cmp function (compare_func) into a modern key.
    s_nums.sort(key=cmp_to_key(compare_func))

    # 3. Join the sorted strings
    result = "".join(s_nums)

    # 4. Edge Case: If the number is "000...", it should be simplified to "0".
    if result and result[0] == '0':
        return "0"
        
    return result

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([10, 2], "210"),
        ([3, 30, 34, 5, 9], "9534330"),
        ([1, 10, 100], "110100"), # 1 is better than 10 or 100
        ([4, 42, 45], "45442"),   # 454 vs 445 -> 45 is better than 4; 424 vs 442 -> 442 is better than 424
        ([0, 0], "0"),
        ([824, 938, 110, 485, 360, 269, 685, 694, 915, 682], "938915824694685682485360269110") 
        # Large complex case
    ]

    print("--- Largest Number (Custom Comparator Sort) Test Results ---")
    
    for nums, expected in test_cases:
        result = largestNumber(nums)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Nums: {nums} -> Result: {result}, Status: {status}")
