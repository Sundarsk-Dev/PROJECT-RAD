# File: app.py

from flask import Flask, render_template, request, redirect, url_for
import time
import random
import re

app = Flask(__name__)

# --- Core Hash Map Logic Classes (Same as before, modified for class methods) ---

class WordFrequencyAnalyzer:
    """Calculates word frequencies in a text using a Hash Map."""
    
    @staticmethod
    def analyze_text(text: str) -> list:
        """Processes the text and returns a list of top word frequencies."""
        
        # Clean the text: convert to lowercase and remove non-alphanumeric/space
        cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
        words = cleaned_text.split()
        
        # Hash Map Implementation: O(N) Frequency Counting
        word_counts = {}
        for word in words:
            if word: # Ensure word is not an empty string
                word_counts[word] = word_counts.get(word, 0) + 1
        
        # Prepare for display: sort and get top results
        top_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10]
        
        # Return as a list of dictionaries for easier display in HTML
        return [{"word": w, "count": c} for w, c in top_words]

# Hash Map stores the state globally for the Rate Limiter: 
# { user_id: [request_count, first_request_timestamp] }
USER_DATA_MAP = {} 
MAX_REQUESTS = 5
TIME_WINDOW = 60 # seconds

class RateLimiter:
    """Manages the O(1) state lookup for the API Rate Limiter."""

    @staticmethod
    def is_request_allowed(user_id: str) -> bool:
        current_time = time.time()

        # O(1) Hash Map Lookup
        if user_id not in USER_DATA_MAP:
            # New user: initialize state
            USER_DATA_MAP[user_id] = [1, current_time]
            return True
        else:
            count, start_time = USER_DATA_MAP[user_id]
            
            # Check if the time window has passed
            if current_time - start_time >= TIME_WINDOW:
                # Reset the window: O(1) update
                USER_DATA_MAP[user_id] = [1, current_time]
                return True
            
            # Check if the user is within the limit
            elif count < MAX_REQUESTS:
                # Within limit: O(1) update
                USER_DATA_MAP[user_id][0] += 1
                return True
            
            else:
                # Exceeded limit
                return False

# --- Flask Routes ---

@app.route('/', methods=['GET', 'POST'])
def home():
    """Route for the Word Frequency Analyzer."""
    pitch = "O(N) Frequency Counter: Uses a Hash Map to count word occurrences in a single, efficient pass, avoiding slow nested loops."
    frequencies = []
    input_text = ""

    if request.method == 'POST':
        input_text = request.form.get('text_input', '')
        if input_text:
            frequencies = WordFrequencyAnalyzer.analyze_text(input_text)

    return render_template('index.html', 
                           pitch=pitch, 
                           frequencies=frequencies, 
                           input_text=input_text)

@app.route('/rate-limiter', methods=['GET', 'POST'])
def rate_limiter_ui():
    """Route for the API Rate Limiter Simulator."""
    global USER_DATA_MAP
    pitch = f"O(1) State Manager: Uses a Hash Map to look up user request status instantly, critical for high-throughput systems. Limit: {MAX_REQUESTS} reqs/{TIME_WINDOW}s."
    result = None
    user_id = ""

    if request.method == 'POST':
        if 'reset' in request.form:
            # Reset button pressed
            USER_DATA_MAP = {}
            result = "SYSTEM RESET: All user tracking data cleared."
        else:
            # Request button pressed
            user_id = request.form.get('user_id', 'Unknown')
            is_allowed = RateLimiter.is_request_allowed(user_id)
            
            if is_allowed:
                result = f"✅ ALLOWED: User {user_id} request accepted."
            else:
                result = f"❌ DENIED: User {user_id} is rate-limited."
    
    # Format the current user data map for display
    # (UserID, Count, Time Remaining)
    display_data = []
    current_time = time.time()
    for uid, (count, start_time) in USER_DATA_MAP.items():
        time_elapsed = current_time - start_time
        time_left = max(0, TIME_WINDOW - time_elapsed)
        
        display_data.append({
            'id': uid,
            'count': count,
            'time_left': f"{time_left:.2f}s"
        })

    return render_template('rate_limiter.html', 
                           pitch=pitch, 
                           result=result, 
                           user_data=display_data,
                           user_id=user_id)


if __name__ == '__main__':
    # You can run this by saving it as app.py and running 'python app.py' 
    # then navigating to http://127.0.0.1:5000/
    app.run(debug=True)