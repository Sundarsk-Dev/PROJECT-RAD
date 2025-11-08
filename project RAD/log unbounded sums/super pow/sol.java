import java.util.*;

public class SuperPow {
    private static final int MOD = 1337;

    // --- Modular Exponentiation ---
    private static int power(int base, int exponent) {
        long result = 1;
        long b = base % MOD;

        while (exponent > 0) {
            if ((exponent & 1) == 1) {
                result = (result * b) % MOD;
            }
            b = (b * b) % MOD;
            exponent >>= 1; // Divide exponent by 2
        }

        return (int) result;
    }

    // --- Super Power Calculation ---
    public static int superPow(int a, int[] b) {
        if (a == 0) return 0;

        int result = 1;

        for (int digit : b) {
            // Step 1: raise result to the power of 10
            result = power(result, 10);

            // Step 2: multiply by a^digit
            int term = power(a, digit);

            // Step 3: combine
            result = (result * term) % MOD;
        }

        return result;
    }

    // --- Testing ---
    public static void main(String[] args) {
        int[][] testDigits = {
            {3},
            {1, 0},
            {2, 0, 0},
            {1, 2, 3},
            {1}
        };
        int[] testBases = {2, 2, 2, 3, 2147483647};
        int[] expected = {8, 1024, 480, 1109, 1022};

        System.out.println("--- Super Pow (Modular Exponentiation) Test Results ---");

        for (int i = 0; i < testBases.length; i++) {
            int a = testBases[i];
            int[] b = testDigits[i];
            int result = superPow(a, b);

            System.out.println(
                "(" + a + "^" + Arrays.toString(b).replaceAll("[\\[\\], ]", "") + 
                ") % " + MOD + " = " + result + 
                " -> " + (result == expected[i] ? "PASSED" : "FAILED (Expected: " + expected[i] + ")")
            );
        }
    }
}

