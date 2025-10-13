from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges all overlapping intervals using a sort-and-merge greedy approach.
    
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    if not intervals:
        return []
    
    # Step 1: Sort the intervals based on their start time
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Initialize the result with the first interval
    merged = [intervals[0]]
    
    # Step 3: Iterate through the rest of the intervals
    for current_interval in intervals[1:]:
        
        # Get the last merged interval to compare against
        last_merged_interval = merged[-1]
        
        # Check for overlap: current interval's start <= last merged interval's end
        if current_interval[0] <= last_merged_interval[1]:
            # Overlap found! Merge by updating the end time of the last merged interval
            # The new end time is the maximum of the two end times
            last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
        else:
            # No overlap! Add the current interval as a new one
            merged.append(current_interval)
            
    return merged

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]), # Touching intervals are also considered overlapping
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 4], [0, 1]], [[0, 4]]),
        ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]), # No overlap
        ([[1, 8], [2, 5]], [[1, 8]]) # Interval fully contained
    ]

    print("--- Merge Intervals Test Results ---")
    
    for intervals, expected in test_cases:
        result = merge(intervals)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Input: {intervals}\nOutput: {result}, Status: {status}\n")