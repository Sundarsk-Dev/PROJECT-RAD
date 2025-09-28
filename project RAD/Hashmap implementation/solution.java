import java.util.HashMap;
import java.util.Map;

public class solution {
    public static int[] twoSums(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int currNum = nums[i];
            int complement = target - currNum;

            // Check if the complement is already in the map
            if (seen.containsKey(complement)) {
                return new int[] { seen.get(complement), i };
            }

            // Store current number with its index
            seen.put(currNum, i);
        }

        return new int[] {}; // Return empty if no solution found
    }

    public static void main(String[] args) {
        int[] nums = { 2, 5, 6, 7, 11, 15 };
        int target = 9;
        int[] result = twoSums(nums, target);

        System.out.println("Two sum result: [" + result[0] + ", " + result[1] + "]");
    }
}
