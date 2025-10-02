class RotatedArraySearch {

    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Case 1: Found target
            if (nums[mid] == target) {
                return mid;
            }

            // Case 2: Left half is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1; // target in left half
                } else {
                    left = mid + 1; // target in right half
                }
            }
            // Case 3: Right half is sorted
            else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1; // target in right half
                } else {
                    right = mid - 1; // target in left half
                }
            }
        }
        return -1; // not found
    }

    // Example usage
    public static void main(String[] args) {
        RotatedArraySearch solver = new RotatedArraySearch();

        int[] nums1 = {4, 5, 6, 7, 0, 1, 2};
        System.out.println(solver.search(nums1, 1)); // Output: 5

        int[] nums2 = {6, 7, 0, 1, 2, 3, 4, 5};
        System.out.println(solver.search(nums2, 7)); // Output: 1

        int[] nums3 = {11, 13, 15, 17};
        System.out.println(solver.search(nums3, 12)); // Output: -1

        int[] nums4 = {3, 1};
        System.out.println(solver.search(nums4, 1)); // Output: 1
    }
}
