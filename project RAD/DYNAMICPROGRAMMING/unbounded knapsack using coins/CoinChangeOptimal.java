import java.util.Arrays;

public class CoinChangeOptimal {

    public int coinChange(int[] coins, int amount) {
        if (amount == 0)
            return 0;

        int SENTINEL = amount + 1; // acts as "infinity"
        int[] dp = new int[amount + 1];

        // Fill dp array with "infinity"
        Arrays.fill(dp, SENTINEL);

        // Base case: 0 coins to make amount 0
        dp[0] = 0;

        // Build the dp array
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i >= coin) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] == SENTINEL ? -1 : dp[amount];
    }

    // --- Testing ---
    public static void main(String[] args) {
        CoinChangeOptimal solver = new CoinChangeOptimal();

        int[][] testCoins = {
                { 1, 2, 5 },
                { 2 },
                { 1 },
                { 1, 5, 10, 25 },
                { 186, 419, 83, 408 }
        };
        int[] testAmounts = { 11, 3, 0, 63, 6249 };
        int[] expectedResults = { 3, -1, 0, 6, 20 };

        System.out.println("--- Coin Change (Minimum Coins) Test Results ---");
        boolean allPassed = true;

        for (int i = 0; i < testCoins.length; i++) {
            int result = solver.coinChange(testCoins[i], testAmounts[i]);
            String status = (result == expectedResults[i]) ? "PASSED"
                    : "FAILED (Expected: " + expectedResults[i] + ", Got: " + result + ")";
            System.out.printf("Coins: %s, Amount: %d -> Result: %d, Status: %s%n",
                    Arrays.toString(testCoins[i]), testAmounts[i], result, status);
            if (result != expectedResults[i])
                allPassed = false;
        }

        if (allPassed) {
            System.out.println("\n✅ All test cases passed successfully!");
        } else {
            System.out.println("\n❌ Some test cases failed.");
        }
    }
}
