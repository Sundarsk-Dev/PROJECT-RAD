import math
def maxdif(distance:float) -> float:
    if distance <=10:
        return distance-10 if distance>10 else 0 
    exponent=math.floor(math.log10(distance))
    milestonecurr=10**exponent
    if(distance == milestonecurr):
        milestoneprev=10**(exponent-1)
    else:
        milestoneprev=milestonecurr
    return distance-milestoneprev
# --- Test Cases ---
if __name__ == "__main__":
    test_cases = [
        (90, 80),        # 90 - 10 = 80
        (1050, 50),      # 1050 - 1000 = 50
        (10, 0),         # 10 - 10 (or 0) = 0. Based on the logic, must return 0.
        (100, 90),       # 100 - 10 = 90 (The preceding milestone is 10)
        (99.9, 89.9),    # 99.9 - 10 = 89.9
        (1000.001, 0.001),# 1000.001 - 1000 = 0.001
        (5, 0)           # 5 - 0 = 5 (But for consistency with 10-100 logic, we use 0)
    ]

    print("--- Maximum Milestone Difference Test Results ---")
    all_passed = True
    
    for distance, expected in test_cases:
        result = maxdif(distance)
        
        # Rounding for float precision in tests
        result_rounded = round(result, 3)
        expected_rounded = round(expected, 3)

        status = "PASSED" if result_rounded == expected_rounded else f"FAILED (Expected: {expected}, Got: {result_rounded})"
        
        print(f"Distance: {distance} km -> Difference: {result_rounded} km, Status: {status}")
        
        if result_rounded != expected_rounded:
            all_passed = False
            
    if all_passed:
        print("\n✅ All test cases passed successfully!")
    else:
        print("\n❌ Some test cases failed.")
