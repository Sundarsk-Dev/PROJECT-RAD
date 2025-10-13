import java.util.*;

class Sol {

    public List<int[]> merge(int[][] intervals) {
        // 🛑 Step 1: Handle empty input
        if (intervals == null || intervals.length == 0)
            return new ArrayList<>();

        // 🧩 Step 2: Sort intervals by their start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        // 🧠 Step 3: Create a list to store merged intervals
        List<int[]> merged = new ArrayList<>();

        // 🧱 Step 4: Add the first interval to start
        merged.add(intervals[0]);

        // 🌀 Step 5: Go through all the remaining intervals
        for (int i = 1; i < intervals.length; i++) {
            int[] current = intervals[i];
            int[] lastMerged = merged.get(merged.size() - 1);

            // 🔍 Check if they overlap (current start <= last merged end)
            if (current[0] <= lastMerged[1]) {
                // ✅ Merge them: update the end of the last merged interval
                lastMerged[1] = Math.max(lastMerged[1], current[1]);
            } else {
                // ❌ No overlap, just add as a new interval
                merged.add(current);
            }
        }

        return merged;
    }

    // 🧪 --- Test Cases ---
    public static void main(String[] args) {
        Sol sol = new Sol();

        int[][][] testCases = {
                { { 1, 3 }, { 2, 6 }, { 8, 10 }, { 15, 18 } },
                { { 1, 4 }, { 4, 5 } },
                { { 1, 4 }, { 0, 4 } },
                { { 1, 4 }, { 0, 1 } },
                { { 1, 2 }, { 3, 4 }, { 5, 6 } },
                { { 1, 8 }, { 2, 5 } }
        };

        int[][][] expectedResults = {
                { { 1, 6 }, { 8, 10 }, { 15, 18 } },
                { { 1, 5 } },
                { { 0, 4 } },
                { { 0, 4 } },
                { { 1, 2 }, { 3, 4 }, { 5, 6 } },
                { { 1, 8 } }
        };

        System.out.println("--- Merge Intervals Test Results ---\n");

        for (int t = 0; t < testCases.length; t++) {
            List<int[]> result = sol.merge(testCases[t]);
            System.out.print("Input: ");
            printIntervals(testCases[t]);
            System.out.print("Output: ");
            printIntervals(result);
            System.out.println();
        }
    }

    private static void printIntervals(int[][] intervals) {
        System.out.print("[");
        for (int i = 0; i < intervals.length; i++) {
            System.out.print(Arrays.toString(intervals[i]));
            if (i < intervals.length - 1)
                System.out.print(", ");
        }
        System.out.println("]");
    }

    private static void printIntervals(List<int[]> intervals) {
        System.out.print("[");
        for (int i = 0; i < intervals.size(); i++) {
            System.out.print(Arrays.toString(intervals.get(i)));
            if (i < intervals.size() - 1)
                System.out.print(", ");
        }
        System.out.println("]");
    }
}
