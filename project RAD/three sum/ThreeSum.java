import java.util.*;

public class ThreeSum {
    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        int n = nums.length;
        if (n < 3)
            return results;

        Arrays.sort(nums); // Step 1: Sort

        for (int i = 0; i < n - 2; i++) {
            // Skip duplicate anchors
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            // Optimization: if nums[i] > 0, we can break
            if (nums[i] > 0)
                break;

            int left = i + 1, right = n - 1;
            int target = -nums[i];

            while (left < right) {
                int sum = nums[left] + nums[right];

                if (sum == target) {
                    results.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // Skip duplicates for left pointer
                    while (left < right && nums[left] == nums[left + 1])
                        left++;
                    // Skip duplicates for right pointer
                    while (left < right && nums[right] == nums[right - 1])
                        right--;

                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return results;
    }

    // --- Test ---
    public static void main(String[] args) {
        int[][] testCases = {
                { -1, 0, 1, 2, -1, -4 },
                { 0, 1, 1 },
                { 0, 0, 0 },
                { -2, 0, 1, 1, 2 },
                { 1, 2, -2, -1 }
        };

        for (int[] nums : testCases) {
            List<List<Integer>> result = threeSum(nums);
            System.out.println("Input: " + Arrays.toString(nums));
            System.out.println("Triplets: " + result);
            System.out.println();
        }
    }
}
