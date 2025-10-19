public class MedianOfTwoSortedArrays {

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Make sure nums1 is smaller to reduce binary search space
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.length;
        int n = nums2.length;
        int halfLen = (m + n + 1) / 2;

        int low = 0, high = m;

        while (low <= high) {
            int i = (low + high) / 2;
            int j = halfLen - i;

            // Left max and right min for both arrays
            int leftMax1 = (i == 0) ? Integer.MIN_VALUE : nums1[i - 1];
            int leftMax2 = (j == 0) ? Integer.MIN_VALUE : nums2[j - 1];

            int rightMin1 = (i == m) ? Integer.MAX_VALUE : nums1[i];
            int rightMin2 = (j == n) ? Integer.MAX_VALUE : nums2[j];

            // Check if partition is correct
            if (leftMax1 <= rightMin2 && leftMax2 <= rightMin1) {
                // Found correct partition
                if ((m + n) % 2 == 1) {
                    // Odd total length
                    return Math.max(leftMax1, leftMax2);
                } else {
                    // Even total length
                    return (Math.max(leftMax1, leftMax2) + Math.min(rightMin1, rightMin2)) / 2.0;
                }
            }
            // Adjust binary search range
            else if (leftMax1 > rightMin2) {
                high = i - 1; // too many elements from nums1
            } else {
                low = i + 1; // too few elements from nums1
            }
        }

        return 0.0; // Should never reach here if inputs are valid
    }

    // --- Test Cases ---
    public static void main(String[] args) {
        int[][] nums1Cases = {
                { 1, 3 }, { 1, 2 }, { 0, 0 }, {}, { 100 }, { 1, 2, 3, 4, 5 }
        };
        int[][] nums2Cases = {
                { 2 }, { 3, 4 }, { 0, 0 }, { 1 }, { 1, 2, 3, 4, 5 }, { 100 }
        };
        double[] expected = { 2.0, 2.5, 0.0, 1.0, 3.5, 3.5 };

        System.out.println("--- Median of Two Sorted Arrays Test Results ---");
        for (int t = 0; t < nums1Cases.length; t++) {
            double result = findMedianSortedArrays(nums1Cases[t], nums2Cases[t]);
            System.out.printf("Case %d: Median = %.2f | Expected = %.2f | %s%n",
                    t + 1, result, expected[t],
                    (Math.abs(result - expected[t]) < 1e-6 ? "PASSED" : "FAILED"));
        }
    }
}
