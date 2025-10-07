import java.util.*;

public class sol {

    /**
     * Computes the length of the Longest Common Subsequence (LCS)
     * using 2D Dynamic Programming.
     *
     * Time Complexity: O(m * n)
     * Space Complexity: O(m * n)
     */
    public static int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();

        // Initialize the DP table (m+1 rows, n+1 columns)
        int[][] dp = new int[m + 1][n + 1];

        // Fill the DP table bottom-up
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {

                // Case 1: Characters Match
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }
                // Case 2: Characters Mismatch
                else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        // Final result is in the bottom-right cell
        return dp[m][n];
    }

    // --- Test Runner ---
    public static void main(String[] args) {
        List<TestCase> testCases = Arrays.asList(
                new TestCase("abcde", "ace", 3), // LCS: "ace"
                new TestCase("abc", "abc", 3), // LCS: "abc"
                new TestCase("abc", "def", 0), // LCS: ""
                new TestCase("bl", "yby", 1), // LCS: "b"
                new TestCase("zxabcdezy", "yzabcdezx", 6) // LCS: "abcdez"
        );

        System.out.println("--- Longest Common Subsequence Test Results ---");
        boolean allPassed = true;

        for (TestCase t : testCases) {
            int result = longestCommonSubsequence(t.text1, t.text2);
            String status = (result == t.expected)
                    ? "PASSED"
                    : "FAILED (Expected: " + t.expected + ", Got: " + result + ")";
            System.out.printf("'%s' vs '%s' -> Length: %d, Status: %s%n",
                    t.text1, t.text2, result, status);

            if (result != t.expected)
                allPassed = false;
        }

        if (allPassed)
            System.out.println("\n✅ All test cases passed successfully!");
        else
            System.out.println("\n❌ Some test cases failed.");
    }

    // --- Helper class for test cases ---
    static class TestCase {
        String text1;
        String text2;
        int expected;

        TestCase(String text1, String text2, int expected) {
            this.text1 = text1;
            this.text2 = text2;
            this.expected = expected;
        }
    }
}
