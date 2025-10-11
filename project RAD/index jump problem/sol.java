public class sol {
    public static boolean canJump(int[] nums) {
        int n = nums.length;
        if (n == 0) return false;
        if (n == 1) return true;

        int goal = n - 1; // Start from the last index

        // Move backward through the array
        for (int i = n - 2; i >= 0; i--) {
            int farthestJump = i + nums[i];
            if (farthestJump >= goal) {
                goal = i; // Update goal
            }
        }

        // If goal reaches 0, we can jump to the end
        return goal == 0;
    }

    public static void main(String[] args) {
        int[][] testCases = {
            {2, 3, 1, 1, 4},
            {3, 2, 1, 0, 4},
            {0},
            {1, 1, 0, 1},
            {1, 0, 1},
            {5, 0, 0, 0, 0}
        };

        boolean[] expectedResults = {true, false, true, false, false, true};

        System.out.println("--- Jump Game (Greedy) Test Results ---");
        for (int t = 0; t < testCases.length; t++) {
            boolean result = canJump(testCases[t]);
            System.out.printf("Nums: %s -> Can Reach End: %b, Status: %s%n",
                java.util.Arrays.toString(testCases[t]),
                result,
                (result == expectedResults[t]) ? "PASSED" : "FAILED");
        }
    }
}
