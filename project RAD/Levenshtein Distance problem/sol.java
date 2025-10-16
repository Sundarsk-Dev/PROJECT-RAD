public class sol {

    public static int minDistance(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();

        int[][] dp = new int[n + 1][m + 1];

        // Base case: one string is empty
        for (int i = 0; i <= n; i++) {
            dp[i][0] = i; // delete all characters
        }
        for (int j = 0; j <= m; j++) {
            dp[0][j] = j; // insert all characters
        }

        // Fill the DP table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1]; // same character, no cost
                } else {
                    dp[i][j] = 1 + Math.min(
                            dp[i - 1][j], // delete
                            Math.min(dp[i][j - 1], dp[i - 1][j - 1]) // insert, replace
                    );
                }
            }
        }

        return dp[n][m];
    }

    public static void main(String[] args) {
        String[][] testCases = {
                { "horse", "ros" },
                { "intention", "execution" },
                { "abc", "a" },
                { "", "abc" },
                { "kitten", "sitting" }
        };

        int[] expected = { 3, 5, 2, 3, 3 };

        System.out.println("--- Edit Distance (2D DP) Test Results ---");
        for (int i = 0; i < testCases.length; i++) {
            String w1 = testCases[i][0];
            String w2 = testCases[i][1];
            int result = minDistance(w1, w2);
            System.out.println("'" + w1 + "' -> '" + w2 + "' = " + result +
                    (result == expected[i] ? " ✅ PASSED" : " ❌ FAILED (Expected " + expected[i] + ")"));
        }
    }
}
