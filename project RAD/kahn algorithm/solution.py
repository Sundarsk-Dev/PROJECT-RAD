from typing import List, Dict
from collections import deque

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Returns a course schedule using Kahn's algorithm (BFS-based Topological Sort).
    
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    
    # 1. Build the Graph (Adjacency List) and In-Degree Array
    
    # Graph: Key = Prerequisite, Value = List of Courses that depend on it
    adj: Dict[int, List[int]] = {i: [] for i in range(numCourses)}
    
    # In-degree: Array/list where index is the course and value is the count of its prerequisites
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        # Edge: prereq -> course (must take prereq before course)
        adj[prereq].append(course)
        in_degree[course] += 1
        
    # 2. Initialize the Queue with all courses having in-degree 0
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    
    result_order = []
    
    # 3. Process the Queue (BFS)
    while queue:
        prereq_course = queue.popleft()
        result_order.append(prereq_course)
        
        # Process all dependent courses (neighbors)
        for dependent_course in adj[prereq_course]:
            
            # Decrement the dependency count
            in_degree[dependent_course] -= 1
            
            # If a course has no remaining prerequisites, it's ready to be taken
            if in_degree[dependent_course] == 0:
                queue.append(dependent_course)
                
    # 4. Final Check (Cycle Detection)
    # If we haven't included all courses, there must be a cycle.
    if len(result_order) == numCourses:
        return result_order
    else:
        # Cycle detected (e.g., A needs B, B needs A)
        return []

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], 4), # Valid: [0, 1, 2, 3] or [0, 2, 1, 3]
        (2, [[1, 0]], 2),                         # Valid: [0, 1]
        (2, [[1, 0], [0, 1]], 0),                 # Cycle: 1 needs 0, 0 needs 1. Result: []
        (1, [], 1),                               # Trivial case: [0]
    ]

    print("--- Course Schedule II (Topological Sort) Test Results ---")
    
    for num_courses, prereqs, expected_len in test_cases:
        result = findOrder(num_courses, prereqs)
        
        # Check based on length to determine success/cycle
        status = "PASSED" if len(result) == expected_len else f"FAILED (Expected len {expected_len}, Got len {len(result)})"
        
        print(f"Courses: {num_courses}, Prereqs: {prereqs} -> Order: {result}, Status: {status}\n")
        