from typing import List

def numDecodings(s: str) -> int:    
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0

    dp_i_minus_2 = 1  # Equivalent to DP[0] = 1
    dp_i_minus_1 = 1 if s[0] != '0' else 0 # Equivalent to DP[1]

    for i in range(2, n + 1):
        
        # Calculate Ways_1: Single digit (s[i-1])
        # This is the single character at the current end of the string.
        ways_1 = 0
        single_digit = s[i-1]
        if '1' <= single_digit <= '9':
            ways_1 = dp_i_minus_1 # Adds ways from DP[i-1]

        # Calculate Ways_2: Two digits (s[i-2] and s[i-1])
        # This is the two-character segment ending at the current position.
        ways_2 = 0
        two_digits = int(s[i-2:i])
        if 10 <= two_digits <= 26:
            ways_2 = dp_i_minus_2 # Adds ways from DP[i-2]

        # Final DP[i] = Ways_1 + Ways_2
        dp_i = ways_1 + ways_2
        
        # If the current DP result is 0, no further decoding is possible
        if dp_i == 0:
            return 0

        # Shift the DP variables for the next iteration
        dp_i_minus_2 = dp_i_minus_1
        dp_i_minus_1 = dp_i
        
    # The final result is the current DP[i-1] (which holds the DP[N] value)
    return dp_i_minus_1

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ("12", 2),       # "AB" (1, 2), "L" (12)
        ("226", 3),      # "BBF" (2 2 6), "VF" (22 6), "BZ" (2 26)
        ("0", 0),        # Invalid start
        ("10", 1),       # "J" (10). Not "A0"
        ("102", 1),      # "JA" (10 2). Not "1 0 2"
        ("27", 1),       # "BG" (2 7). Not "W" (27)
        ("1", 1),
        ("120", 1),      # "LT" (12 0) is wrong. "AT" (1 20). Result: 1
        ("1111", 5)      # (1,1,1,1), (11,1,1), (1,11,1), (1,1,11), (11,11)
    ]

    print("--- Decode Ways (Dynamic Programming) Test Results ---")
    
    for s, expected in test_cases:
        result = numDecodings(s)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Input: '{s}' -> Ways: {result}, Status: {status}")