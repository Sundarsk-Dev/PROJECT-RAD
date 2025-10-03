class ClimbStairs {
    public int climbStairs(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;

        int ways_i_minus_2 = 1; // F(1)
        int ways_i_minus_1 = 2; // F(2)

        for (int i = 3; i <= n; i++) {
            int currentWays = ways_i_minus_1 + ways_i_minus_2;
            ways_i_minus_2 = ways_i_minus_1;
            ways_i_minus_1 = currentWays;
        }

        return ways_i_minus_1;
    }

    public static void main(String[] args) {
        ClimbStairs solver = new ClimbStairs();

        int[] tests = {2, 3, 4, 5, 10, 1, 0};
        for (int n : tests) {
            System.out.println("n = " + n + " -> Ways = " + solver.climbStairs(n));
        }
    }
}
