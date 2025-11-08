from typing import List

MOD = 1337

def power(base: int, exponent: int) -> int:
    """
    Modular Exponentiation: Computes (base^exponent) % MOD 
    using the Binary Exponentiation (Exponentiation by Squaring) method.
    Time complexity: O(log exponent)
    """
    res = 1
    # Note: We must apply the modulo operation to the base before starting
    base %= MOD 
    
    while exponent > 0:
        # If exponent is odd, multiply the result by the current base
        if exponent % 2 == 1:
            res = (res * base) % MOD
        
        # Square the base and reduce modulo MOD
        base = (base * base) % MOD
        
        # Halve the exponent
        exponent //= 2
        
    return res

def superPow(a: int, b: List[int]) -> int:
    """
    Calculates (a^b) % 1337 where b is a large number represented as a list of digits.
    Time Complexity: O(|b|)
    """
    if not b:
        return 1
    
    # Base case: a is a multiple of 1337, result is 0
    if a == 0:
        return 0
    
    # Process digits of b iteratively (left to right)
    # The result at each step is (a^(processed_digits)) % MOD
    result = 1
    
    # Process each digit (d) in b
    for d in b:
        # The core recursive relation: (a^(prev * 10 + d)) = (a^prev)^10 * a^d
        
        # 1. Update based on the factor of 10: (result^10) % MOD
        # result is currently a^(prev). We raise it to the power of 10.
        # This represents the (a^prev)^10 part.
        result = power(result, 10)
        
        # 2. Update based on the new digit d: (a^d) % MOD
        # We multiply by a^d.
        term_d = power(a, d)
        
        # 3. Combine and apply modulo
        result = (result * term_d) % MOD
        
    return result

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        (2, [3], 8),                 # 2^3 % 1337 = 8
        (2, [1, 0], 1024),           # 2^10 % 1337 = 1024
        (2, [2, 0, 0], 480),         # 2^200 % 1337 = 480
        (3, [1, 2, 3], 1109),        # 3^123 % 1337 = 1109
        (2147483647, [1], 1022)      # 2147483647 % 1337 = 1022. 1022^1 % 1337 = 1022
    ]

    print("--- Super Pow (Modular Exponentiation) Test Results ---")
    
    for a, b, expected in test_cases:
        result = superPow(a, b)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        b_str = "".join(map(str, b))
        print(f"({a}^{b_str}) % {MOD} -> Result: {result}, Status: {status}")
