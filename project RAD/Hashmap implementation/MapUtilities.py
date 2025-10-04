
from collections import Counter
import time
import random

# ==============================================================================
# 1. Project: Frequency Counter Utility (Word Cloud Generator)
#    Core Concept: Hash Map for O(1) frequency counting (Aggregation)
# ==============================================================================

class WordFrequencyAnalyzer:
    """Calculates word frequencies in a text using a Hash Map."""

    def __init__(self, text: str):
        self.text = text
        self.pitch = (
            "🎯 PITCH: This utility efficiently counts item frequencies in O(N) time. "
            "By mapping {word: count}, the Hash Map avoids slow O(N^2) nested loops "
            "or repeated searches, making it ideal for large text processing."
        )

    def analyze_text(self) -> dict:
        """Processes the text and returns a dictionary of word frequencies."""
        # Clean the text: convert to lowercase and remove punctuation
        cleaned_text = ''.join(
            char.lower() for char in self.text if char.isalnum() or char.isspace()
        )
        words = cleaned_text.split()
        
        # Implementation using Python's dict/Counter (which is a Hash Map)
        word_counts = {}
        for word in words:
            # Hash Map logic: O(1) lookup and O(1) update
            # Get the current count (or 0 if new) and increment it.
            word_counts[word] = word_counts.get(word, 0) + 1
            
        return word_counts

    def display_ui(self):
        """Displays the pitch and analysis results."""
        print("\n" + "=" * 70)
        print("📊 RAD Project 1: Word Cloud Generator (Frequency Counter)")
        print("=" * 70)
        print(self.pitch)
        print("\n--- Input Text Sample ---")
        print(f"'{self.text[:70]}...'")
        
        frequencies = self.analyze_text()
        
        print("\n--- Analysis Results (Top 5 Frequencies) ---")
        # Sort results for display
        top_words = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)[:5]
        
        for word, count in top_words:
            print(f"   '{word}': {count} times")
            
        print("-" * 70)

# ==============================================================================
# 2. Project: API Rate Limiter Simulator
#    Core Concept: Hash Map for O(1) state management (System Design)
# ==============================================================================

class RateLimiter:
    """Simulates an API rate limiting mechanism using a Hash Map."""

    def __init__(self, max_requests: int, time_window_seconds: int):
        # Hash Map stores the state: { user_id: [request_count, first_request_timestamp] }
        self.user_data = {} 
        self.MAX_REQUESTS = max_requests
        self.TIME_WINDOW = time_window_seconds
        self.pitch = (
            "🎯 PITCH: This tool models a critical system design component. "
            "By using a Hash Map, it achieves **O(1) time complexity per request**, "
            "as user status is instantly retrieved and updated, crucial for "
            "high-throughput, real-time server security and stability."
        )

    def is_request_allowed(self, user_id: str) -> bool:
        """Checks if a user is allowed to make a request."""
        current_time = time.time()

        if user_id not in self.user_data:
            # New user or window expired: initialize state
            self.user_data[user_id] = [1, current_time]
            return True
        else:
            count, start_time = self.user_data[user_id]
            
            # Check if the time window has passed
            if current_time - start_time >= self.TIME_WINDOW:
                # Reset the window: Allow request, start new count/time
                self.user_data[user_id] = [1, current_time]
                return True
            
            # Check if the user is within the limit
            elif count < self.MAX_REQUESTS:
                # Within limit: Allow request and increment count
                self.user_data[user_id][0] += 1
                return True
            
            else:
                # Exceeded limit
                return False

    def display_ui(self, requests_list: list[str]):
        """Displays the pitch and simulates request handling."""
        
        print("\n" + "=" * 70)
        print("🛑 RAD Project 2: API Rate Limiter Simulator")
        print("=" * 70)
        print(self.pitch)
        print(f"\nConfiguration: {self.MAX_REQUESTS} requests per {self.TIME_WINDOW} seconds.")
        print("-" * 70)
        
        
        results = []
        for i, user_id in enumerate(requests_list):
            is_allowed = self.is_request_allowed(user_id)
            status = "✅ ALLOWED" if is_allowed else "❌ DENIED (Rate Limited)"
            results.append(f"Request {i+1}: User {user_id} -> {status}")
            
            # Pause to simulate time passing for the Rate Limiter (optional, but illustrative)
            if i % 5 == 0 and i > 0:
                 time.sleep(0.01) # Small pause
        
        print("\n--- Simulation Results ---")
        for line in results:
             print(line)
        print("-" * 70)


# ==============================================================================
# --- Driver Code (Test Runs) ---
# ==============================================================================

if __name__ == "__main__":
    
    # 1. Test Word Frequency Analyzer
    article = (
        "The quick brown fox jumps over the lazy dog. "
        "The dog is very lazy. The quick fox is quick, "
        "but the quick brown fox is quicker than the lazy dog."
    )
    analyzer = WordFrequencyAnalyzer(article)
    analyzer.display_ui()
    
    # 2. Test API Rate Limiter
    # 3 requests allowed every 1 second
    limiter = RateLimiter(max_requests=3, time_window_seconds=1) 
    
    # User A sends 4 requests quickly (3 should pass, 1 should fail)
    # User B sends 1 request (should pass)
    # User A sends a 5th request (should fail)
    
    simulated_requests = [
        "UserA", "UserA", "UserB", "UserA", 
        "UserA",  # UserA's 4th request (DENY)
        "UserB",  # UserB's 2nd request (ALLOW)
        "UserA"   # UserA's 5th request (DENY)
    ]
    

    limiter.display_ui(simulated_requests) 
