import heapq
from typing import List

def minMeetingRooms(intervals: List[List[int]]) -> int:
    """
    Finds the minimum number of meeting rooms required using a Min-Heap.
    
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    
    if not intervals:
        return 0

    # 1. Sort by start time (O(N log N))
    # Note: Using lambda for custom key
    intervals.sort(key=lambda x: x[0])

    # 2. Initialize Min-Heap to store the end times of occupied rooms
    # The heap stores the *earliest* end time at the root.
    min_heap: List[int] = [] 

    # 3. Start processing: The first meeting always needs a room
    # We only care about its end time
    heapq.heappush(min_heap, intervals[0][1])

    # 4. Process Remaining Meetings
    for i in range(1, len(intervals)):
        start_time = intervals[i][0]
        end_time = intervals[i][1]
        
        # Check the room with the earliest end time (root of the heap)
        earliest_end_time = min_heap[0] 

        # Check Availability: If the current meeting starts AT or AFTER 
        # the earliest meeting ends, we can reuse that room.
        if start_time >= earliest_end_time:
            # Reuse the room: Pop the old end time
            heapq.heappop(min_heap)
        
        # Occupy Room (either the reused one or a new one): Push the new end time
        heapq.heappush(min_heap, end_time)

    # 5. Result: The size of the heap is the max number of concurrent meetings
    return len(min_heap)

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5], [8, 9], [8, 11], [10, 15]], 3), # Max concurrency is at time 8 (meetings [1,5], [8,9], [8,11])
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 1), # No overlap
        ([], 0)
    ]

    print("--- Meeting Rooms II (Min-Heap) Test Results ---")
    
    for intervals, expected in test_cases:
        result = minMeetingRooms(intervals)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Intervals: {intervals} -> Rooms: {result}, Status: {status}")