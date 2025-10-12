import java.util.*;

public class sol {
    public static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();

        if (matrix == null || matrix.length == 0) {
            return result;
        }

        int rows = matrix.length;
        int cols = matrix[0].length;

        int top = 0, bottom = rows - 1;
        int left = 0, right = cols - 1;

        while (top <= bottom && left <= right) {
            // 1. Go Right
            for (int c = left; c <= right; c++) {
                result.add(matrix[top][c]);
            }
            top++;

            // 2. Go Down
            if (top <= bottom) {
                for (int r = top; r <= bottom; r++) {
                    result.add(matrix[r][right]);
                }
                right--;
            }

            // 3. Go Left
            if (top <= bottom && left <= right) {
                for (int c = right; c >= left; c--) {
                    result.add(matrix[bottom][c]);
                }
                bottom--;
            }

            // 4. Go Up
            if (top <= bottom && left <= right) {
                for (int r = bottom; r >= top; r--) {
                    result.add(matrix[r][left]);
                }
                left++;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[][][] testCases = {
                { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } },
                { { 1, 2, 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 } },
                { { 1 }, { 2 }, { 3 } },
                { { 1, 2, 3 } },
                { { 1 } }
        };

        int[][] expectedResults = {
                { 1, 2, 3, 6, 9, 8, 7, 4, 5 },
                { 1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7 },
                { 1, 2, 3 },
                { 1, 2, 3 },
                { 1 }
        };

        System.out.println("--- Spiral Matrix Traversal Test Results ---");
        for (int i = 0; i < testCases.length; i++) {
            List<Integer> result = spiralOrder(testCases[i]);
            System.out.println("Matrix: " + Arrays.deepToString(testCases[i]));
            System.out.println("Spiral Order: " + result + "\n");
        }
    }
}
