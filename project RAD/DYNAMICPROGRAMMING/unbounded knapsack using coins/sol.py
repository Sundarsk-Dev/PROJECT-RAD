from typing import List

def coinChange_optimal(coins: List[int], amount: int) -> int:
    """
    Calculates the minimum number of coins required to make up the total amount 
    using Dynamic Programming.
    
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    if amount == 0:
        return 0
    
    # Initialize DP array of size (amount + 1).
    # The sentinel value is 'amount + 1', which represents infinity, 
    # as the max possible number of coins is 'amount' (using only 1-unit coins).
    SENTINEL = amount + 1
    dp = [SENTINEL] * (amount + 1)
    
    # Base Case: 0 coins needed for amount 0
    dp[0] = 0
    
    # Iterate through every amount from 1 up to the target amount
    for i in range(1, amount + 1):
        
        # For each amount 'i', check every coin denomination
        for coin in coins:
            
            # Check if the coin can be used (i.e., coin value is <= current amount i)
            if i >= coin:
                
                # Apply the recurrence relation:
                # dp[i] = min( current_dp[i], dp[i - coin] + 1 )
                # +1 represents using the current 'coin'
                
                # We update dp[i] only if using the current coin leads to a smaller 
                # number of coins than what we've already found.
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # The result is at the end of the DP array.
    final_result = dp[amount]
    
    # If the result is still the sentinel, it means the amount is unreachable.
    return final_result if final_result <= amount else -1

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5], 11, 3),      # Coins: 5+5+1 = 3 coins
        ([2], 3, -1),            # Cannot make 3 with only 2-unit coins
        ([1], 0, 0),             # Amount is 0
        ([1, 5, 10, 25], 63, 6), # Coins: 25+25+10+1+1+1 = 6 coins
        ([186, 419, 83, 408], 6249, 20) # Larger test case
    ]

    print("--- Coin Change (Minimum Coins) Test Results ---")
    all_passed = True
    
    for coins, amount, expected in test_cases:
        result = coinChange_optimal(coins, amount)
        
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Coins: {coins}, Amount: {amount} -> Result: {result}, Status: {status}")
        
        if result != expected:
            all_passed = False
            
    if all_passed:
        print("\n✅ All test cases passed successfully!")
    else:
        print("\n❌ Some test cases failed.")