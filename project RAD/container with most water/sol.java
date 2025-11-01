import java.util.*;

public class ContainerWithMostWater {
    public static int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int hLeft = height[left];
            int hRight = height[right];
            int width = right - left;
            int currentArea = Math.min(hLeft, hRight) * width;

            maxArea = Math.max(maxArea, currentArea);

            // Move the pointer at the shorter line
            if (hLeft < hRight) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }

    public static void main(String[] args) {
        int[][] testCases = {
                { 1, 8, 6, 2, 5, 4, 8, 3, 7 },
                { 1, 1 },
                { 4, 3, 2, 1, 4 },
                { 1, 2, 1 },
                { 2, 3, 4, 5, 18, 17, 6 }
        };

        int[] expected = { 49, 1, 16, 2, 17 }; // or 16 depending on the test case definition

        for (int i = 0; i < testCases.length; i++) {
            int result = maxArea(testCases[i]);
            System.out.println("Input: " + Arrays.toString(testCases[i]));
            System.out.println("Max Area: " + result + " | Expected: " + expected[i]);
            System.out.println();
        }
    }
}
