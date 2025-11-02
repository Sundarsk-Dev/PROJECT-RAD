from collections import deque, defaultdict
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determines if all courses can be finished using Topological Sort (Kahn's Algorithm / BFS).
    
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    
    # 1. Build the Graph (Adjacency List) and In-Degree Array
    # graph[b] = list of courses that depend on b (must be taken AFTER b)
    graph = defaultdict(list)
    # in_degree[a] = number of prerequisites required for course a
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        # Dependency: prereq -> course
        graph[prereq].append(course)
        in_degree[course] += 1

    # 2. Initialize Queue: Add all nodes with in-degree 0
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)
            
    finished_count = 0
    
    # 3. Process (BFS)
    while queue:
        curr_course = queue.popleft()
        finished_count += 1
        
        # Update Neighbors (Courses that depend on curr_course)
        for neighbor_course in graph[curr_course]:
            # This prerequisite is now satisfied
            in_degree[neighbor_course] -= 1
            
            # If all prerequisites are met, add to queue
            if in_degree[neighbor_course] == 0:
                queue.append(neighbor_course)
                
    # 4. Result Check: If we finished all courses, there was no cycle
    return finished_count == numCourses

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        (2, [[1, 0]], True),                       # Simple dependency: 0 -> 1
        (2, [[1, 0], [0, 1]], False),             # Cycle: 0 -> 1 -> 0
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True), # Complex DAG: 0->1, 0->2, 1->3, 2->3
        (3, [[1, 0], [2, 1], [0, 2]], False),     # Cycle: 0 -> 1 -> 2 -> 0
        (1, [], True)                              # No courses, no prereqs
    ]

    print("--- Course Schedule (Topological Sort / Kahn's Algorithm) Test Results ---")
    
    for num_c, prereqs, expected in test_cases:
        result = canFinish(num_c, prereqs)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Courses: {num_c}, Prereqs: {prereqs} -> Possible: {result}, Status: {status}")