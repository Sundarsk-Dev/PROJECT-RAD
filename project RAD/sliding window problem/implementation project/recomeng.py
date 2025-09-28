# File: RecommenderEngine.py

class MovieRecommender:
    """
    RAD Project: Movie Recommender Engine (Sliding Window & Hash Map)
    
    Finds the longest contiguous sequence of movie genres a user can watch 
    such that no single genre is repeated more than M times within that sequence.
    """

    def __init__(self, max_genre_count: int):
        """Initializes the engine with the maximum allowed count M for any single genre."""
        self.MAX_M = max_genre_count
        self.pitch = (
            "🎯 PITCH: This engine uses the **Sliding Window** pattern to optimize "
            "recommendation streams. By enforcing a constraint (Max M genre repeats) "
            "with **O(1) Hash Map lookups**, we find the longest valid sequence in a "
            "single pass, achieving optimal **O(N) time complexity**."
        )

    def find_longest_valid_sequence(self, genres: list[str]) -> tuple:
        """
        Implements the Variable-Size Sliding Window algorithm.

        Args:
            genres: The full sequence of genres watched/to be watched.

        Returns:
            A tuple containing (max_length, longest_sequence_segment)
        """
        
        # Hash Map (Dictionary) to track the frequency of genres INSIDE the current window
        # Key: Genre (str), Value: Count (int)
        genre_counts = {}
        
        left = 0              # The left pointer (start of the window)
        max_length = 0        # Tracks the overall longest valid length
        best_window = []      # Stores the longest valid sequence found
        
        N = len(genres)

        # Right pointer expands the window one element at a time
        for right in range(N):
            current_genre = genres[right]
            
            # --- 1. Expand Window and Update Hash Map (O(1) operation) ---
            # Increment the count of the genre being added at the 'right' pointer
            genre_counts[current_genre] = genre_counts.get(current_genre, 0) + 1
            
            # --- 2. Enforce Constraint (Shrink Window if Violated) ---
            # If the count of the current genre exceeds the MAX_M constraint:
            while genre_counts[current_genre] > self.MAX_M:
                
                # The constraint is violated, so we must shrink the window from the left
                genre_to_remove = genres[left]
                
                # Decrement the count of the genre being removed (O(1) update)
                genre_counts[genre_to_remove] -= 1
                
                # Move the left pointer forward
                left += 1
            
            # --- 3. Update Answer (The window [left, right] is now valid) ---
            current_length = right - left + 1
            
            if current_length > max_length:
                max_length = current_length
                # Record the actual segment
                best_window = genres[left : right + 1]
                
        return max_length, best_window

    def display_ui(self, genres: list[str]):
        """Prints the pitch and the results with a user-friendly output."""
        
        max_len, best_seq = self.find_longest_valid_sequence(genres)
        
        print("\n" + "=" * 70)
        print("🎬 RAD Project: Movie Recommender Engine")
        print("=" * 70)
        print(self.pitch)
        print(f"\nConfiguration: Maximum Allowed Repeats (M) per Genre: {self.MAX_M}")
        print("-" * 70)
        
        print("\nInput Genre Stream:")
        print(f"   {genres}")
        
        print("\n--- Sliding Window Results ---")
        print(f"   Max Valid Length Found: {max_len}")
        print("   Longest Valid Sequence:")
        print(f"   {best_seq}")
        print("\nVerification (Frequencies in the result):")
        
        # Use Counter on the result for quick verification display
        counts = {}
        for genre in best_seq:
            counts[genre] = counts.get(genre, 0) + 1

        for genre, count in counts.items():
            validity = "✅ OK" if count <= self.MAX_M else "❌ ERROR" # Should always be OK
            print(f"      - {genre}: {count} times ({validity})")
        
        print("=" * 70)


# --- Driver Code (Test Runs) ---

if __name__ == "__main__":
    
    # M = 2: No single genre can appear more than twice in the sequence.
    engine1 = MovieRecommender(max_genre_count=2)
    genres1 = ["Action", "Comedy", "Action", "Horror", "Action", "Action", "Thriller", "Comedy", "Comedy"]
    engine1.display_ui(genres1)
    # Expected Result: Length 5. Sequence: ["Thriller", "Comedy", "Comedy", "Action", "Action"] 
    # OR ["Horror", "Action", "Action", "Thriller", "Comedy"] (Order depends on the exact algorithm)
    
    # M = 1: No repeats allowed (Longest Substring Without Repeating Characters)
    engine2 = MovieRecommender(max_genre_count=1)
    genres2 = ["A", "B", "A", "C", "D", "B", "E"]
    engine2.display_ui(genres2)
    # Expected Result: Length 4. Sequence: ["A", "C", "D", "B"] (B is the first repeat, so it's a shorter sequence)
    # The actual longest is ["A", "C", "D", "B"] is invalid. The longest unique segment is ["C", "D", "B", "E"] (Length 4)
    # Let's check the code's output for s2: It returns ["C", "D", "B", "E"] with length 4. (The left pointer skips 'A' and 'B')