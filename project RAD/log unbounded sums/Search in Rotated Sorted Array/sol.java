public class RotatedBinarySearch {

    public static int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            // Case 1: Target found
            if (nums[mid] == target) {
                return mid;
            }

            // Case 2: Left half is sorted
            if (nums[low] <= nums[mid]) {
                // Target lies in the left half
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                } else { // Target lies in the right half
                    low = mid + 1;
                }
            }
            // Case 3: Right half is sorted
            else {
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }

        // Target not found
        return -1;
    }

    public static void main(String[] args) {
        int[][] testArrays = {
            {4, 5, 6, 7, 0, 1, 2},
            {4, 5, 6, 7, 0, 1, 2},
            {4, 5, 6, 7, 0, 1, 2},
            {1, 3},
            {3, 1},
            {1},
            {5, 1, 3},
            {7, 8, 1, 2, 3, 4, 5, 6}
        };

        int[] targets = {0, 3, 6, 3, 1, 1, 3, 1};
        int[] expected = {4, -1, 2, 1, 1, 0, 2, 2};

        System.out.println("--- Search in Rotated Sorted Array Test Results ---");

        for (int i = 0; i < testArrays.length; i++) {
            int result = search(testArrays[i], targets[i]);
            String status = (result == expected[i])
                    ? "PASSED"
                    : "FAILED (Expected: " + expected[i] + ", Got: " + result + ")";
            System.out.println("Input: " + java.util.Arrays.toString(testArrays[i]) +
                               ", Target: " + targets[i] +
                               " -> Index: " + result +
                               ", Status: " + status);
        }
    }
}
