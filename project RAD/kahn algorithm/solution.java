import java.util.*;

public class Sol {

    public static int[] findOrder(int numCourses, int[][] prerequisites) {
        // Step 1: Build graph and in-degree array
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        int[] inDegree = new int[numCourses];

        for (int[] pre : prerequisites) {
            int course = pre[0];
            int prereq = pre[1];
            adj.get(prereq).add(course);
            inDegree[course]++;
        }

        // Step 2: Initialize queue with all nodes having in-degree 0
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }

        int[] order = new int[numCourses];
        int index = 0;

        // Step 3: Process the queue (Kahn’s Algorithm)
        while (!queue.isEmpty()) {
            int prereqCourse = queue.poll();
            order[index++] = prereqCourse;

            for (int dependentCourse : adj.get(prereqCourse)) {
                inDegree[dependentCourse]--;
                if (inDegree[dependentCourse] == 0) {
                    queue.offer(dependentCourse);
                }
            }
        }

        // Step 4: If all courses are included → success, else cycle
        if (index == numCourses) {
            return order;
        } else {
            return new int[0]; // cycle detected
        }
    }

    public static void main(String[] args) {
        int[][][] testCases = {
            {{1,0},{2,0},{3,1},{3,2}},
            {{1,0}},
            {{1,0},{0,1}},
            {}
        };
        int[] numCoursesList = {4, 2, 2, 1};

        System.out.println("--- Course Schedule II (Topological Sort) Test Results ---");
        for (int i = 0; i < testCases.length; i++) {
            int[] result = findOrder(numCoursesList[i], testCases[i]);
            System.out.println("Courses: " + numCoursesList[i] + ", Result: " + Arrays.toString(result));
        }
    }
}
