public class sol {

    public static int numDecodings(String s) {
        if (s == null || s.length() == 0)
            return 0;
        int n = s.length();
        // If first char is '0', no valid decoding
        if (s.charAt(0) == '0')
            return 0;

        // dp[i-2] and dp[i-1]
        int dp_i_minus_2 = 1; // dp[0]
        int dp_i_minus_1 = 1; // dp[1] (since s.charAt(0) != '0')

        for (int i = 2; i <= n; i++) {
            int ways1 = 0;
            char singleChar = s.charAt(i - 1);
            if (singleChar >= '1' && singleChar <= '9') {
                ways1 = dp_i_minus_1;
            }

            int ways2 = 0;
            int twoDigits = Integer.parseInt(s.substring(i - 2, i)); // s[i-2:i]
            if (twoDigits >= 10 && twoDigits <= 26) {
                ways2 = dp_i_minus_2;
            }

            int dp_i = ways1 + ways2;
            if (dp_i == 0)
                return 0; // no possible decoding from here

            dp_i_minus_2 = dp_i_minus_1;
            dp_i_minus_1 = dp_i;
        }

        return dp_i_minus_1;
    }

    // --- Test driver ---
    public static void main(String[] args) {
        String[] inputs = { "12", "226", "0", "10", "102", "27", "1", "120", "1111" };
        int[] expected = { 2, 3, 0, 1, 1, 1, 1, 1, 5 };

        System.out.println("--- Decode Ways Test Results ---");
        for (int i = 0; i < inputs.length; i++) {
            int res = numDecodings(inputs[i]);
            String status = (res == expected[i]) ? "PASSED" : "FAILED (Expected: " + expected[i] + ")";
            System.out.printf("Input: '%s' -> Ways: %d, %s%n", inputs[i], res, status);
        }
    }
}
