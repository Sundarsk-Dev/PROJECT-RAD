import java.util.*;

public class MeetingRoomsII {

    public static int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0)
            return 0;

        // 1. Sort by start time
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        // 2. Min-heap to track earliest end time
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        // 3. Add first meeting's end time
        minHeap.add(intervals[0][1]);

        // 4. Process the rest
        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            // If the room is free (meeting ended)
            if (start >= minHeap.peek()) {
                minHeap.poll(); // Free one room
            }

            // Add the current meeting's end time
            minHeap.add(end);
        }

        // 5. The heap size = number of rooms required
        return minHeap.size();
    }

    public static void main(String[] args) {
        int[][][] testCases = {
                { { 0, 30 }, { 5, 10 }, { 15, 20 } },
                { { 7, 10 }, { 2, 4 } },
                { { 1, 5 }, { 8, 9 }, { 8, 11 }, { 10, 15 } },
                { { 1, 2 }, { 2, 3 }, { 3, 4 }, { 4, 5 } }
        };
        int[] expected = { 2, 1, 3, 1 };

        System.out.println("--- Meeting Rooms II (Min-Heap) Test Results ---");
        for (int i = 0; i < testCases.length; i++) {
            int result = minMeetingRooms(testCases[i]);
            System.out.printf("Test %d -> Rooms: %d, Expected: %d, %s%n",
                    i + 1, result, expected[i],
                    (result == expected[i] ? "PASSED" : "FAILED"));
        }
    }
}
