import random
from typing import List, Any

def reservoir_sample_k_1(stream: List[Any]) -> Any:
    """
    Selects one item from a stream (list) such that all items have 
    equal probability of being selected (1/N).
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if not stream:
        return None

    # Initialize the result with the first element (i=1)
    result = stream[0]
    
    # Start loop from the second element (index 1, which is the 2nd item, i=2)
    for i in range(1, len(stream)):
        
        # Current stream size is i + 1 (since 0-indexed)
        stream_size = i + 1
        
        # Generate a random number j between 0 and stream_size - 1 (inclusive)
        # This gives us a 1/stream_size chance of selecting the current item.
        j = random.randrange(0, stream_size)
        
        # If the random index is 0 (1 out of stream_size times), replace the result
        if j == 0:
            result = stream[i]
            
    return result

# --- Test Case Simulation ---

if __name__ == "__main__":
    # Test stream of unknown length
    test_stream = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
    N = len(test_stream)
    
    # Run the sampling many times to demonstrate equal probability
    NUM_RUNS = 100000
    counts = {item: 0 for item in test_stream}
    
    for _ in range(NUM_RUNS):
        selection = reservoir_sample_k_1(test_stream)
        counts[selection] += 1

    expected_count = NUM_RUNS / N
    
    print("--- Reservoir Sampling (k=1) Simulation ---")
    print(f"Total Items (N): {N}, Total Runs: {NUM_RUNS}")
    print(f"Expected Count per Item: {expected_count:.2f}\n")

    for item, count in counts.items():
        diff = abs(count - expected_count)
        print(f"Item: {item:<12} | Actual Count: {count:<6} | Deviation: {diff:.2f}")

    print("\nSince the actual counts are close to the expected count, the probability is uniform.")
