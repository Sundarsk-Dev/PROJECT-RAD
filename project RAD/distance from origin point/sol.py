import heapq
from typing import List, Tuple

def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    """
    Finds the K closest points to the origin using a Max-Heap of size K.
    
    Time Complexity: O(N log K)
    Space Complexity: O(K)
    """
    # Max-Heap (simulated using Python's Min-Heap by negating the distance)
    # Heap stores: (-distance_squared, x, y)
    max_heap: List[Tuple[float, int, int]] = []
    
    for x, y in points:
        # Calculate squared distance (no need for sqrt, as D^2 preserves order)
        distance_squared = x**2 + y**2
        
        # We push the negative distance to simulate a Max-Heap (largest distance 
        # becomes the smallest negative number, which Python's Min-Heap handles)
        
        if len(max_heap) < K:
            # 1. Fill the heap until size K
            heapq.heappush(max_heap, (-distance_squared, x, y))
        else:
            # 2. Heap is full, check if the current point is closer than the current farthest (the root)
            # max_heap[0] is the root (the point with the greatest NEGATIVE distance, 
            # meaning the largest POSITIVE distance)
            farthest_distance = -max_heap[0][0] # Convert back to positive for comparison
            
            if distance_squared < farthest_distance:
                # If current point is closer, replace the farthest point
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-distance_squared, x, y))
                
    # 3. Extract the final K points from the heap
    result = []
    while max_heap:
        # We only care about the coordinates (x, y)
        neg_dist, x, y = heapq.heappop(max_heap)
        result.append([x, y])
        
    return result

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
        ([[6, 1], [1, 6], [2, 5]], 2, [[6, 1], [2, 5]]), # Distances: 37, 37, 29. Result should be 29 and one of 37s.
        ([[1, 1], [1, 1]], 1, [[1, 1]]), # Identical points
    ]

    print("--- K Closest Points to Origin Test Results ---")
    
    for points, K, expected_points in test_cases:
        result = kClosest(points, K)
        
        # Sort the results for deterministic comparison (since order doesn't matter)
        sorted_result = sorted(result)
        sorted_expected = sorted(expected_points)
        
        status = "PASSED" if sorted_result == sorted_expected else f"FAILED (Expected: {sorted_expected}, Got: {sorted_result})"
        
        print(f"Points: {points}, K = {K} -> Result: {sorted_result}, Status: {status}")