from typing import List

class StackSyntaxChecker:
    """
    Validates a string for correctly ordered and closed brackets using a Stack.
    The 'verbose' mode acts as a stack visualizer for the project.
    """
    
    def isValid(self, s: str, verbose: bool = False) -> bool:
        
        # O(1) Quick Fail Check: Must have an even number of characters
        if len(s) % 2 != 0:
            if verbose: print(f"FAIL: Odd length string ({len(s)}). Cannot be valid.")
            return False
        
        # Stack (Implemented using a list/array)
        stack: List[str] = []
        
        # Hash Map for O(1) look-up of corresponding opening bracket
        mapping = {")": "(", "}": "{", "]": "["}
        
        if verbose: 
            print("=" * 40)
            print(f"Input String: '{s}'")
            print("--- Stack Trace ---")

        for char in s:
            
            # 1. If the character is an Opening Bracket: Push to the stack
            if char in mapping.values():
                stack.append(char)
                if verbose: print(f"  PUSH: '{char}' -> Stack: {stack}")
            
            # 2. If the character is a Closing Bracket: Check the stack
            elif char in mapping.keys():
                
                # Check A (Empty Stack): Closing bracket found, but no open bracket to match
                if not stack:
                    if verbose: print(f"  FAIL: Closing '{char}' on an EMPTY stack.")
                    return False
                
                # Pop the top element and check for a mismatch
                top_element = stack.pop()
                expected_open = mapping[char]
                
                # Check B (Mismatched Pair): The popped open bracket doesn't match the required type
                if top_element != expected_open:
                    if verbose: print(f"  FAIL: Closing '{char}', but last open was '{top_element}'. Expected '{expected_open}'")
                    return False
                
                if verbose: print(f"  MATCH: Pop '{top_element}' for '{char}' -> Stack: {stack}")

            # Note: Non-bracket characters are ignored by default.

        # 3. Final Check: The stack must be empty after processing all characters
        if verbose: 
            print("--- End of String ---")
            print(f"Final Stack State: {stack}")
            
        if stack:
            if verbose: print("FAIL: Stack is NOT empty. Unclosed brackets remain.")
            return False
        else:
            if verbose: print("SUCCESS: Stack is empty. All brackets closed correctly.")
            return True

# --- Execution Examples (Project Visualization) ---
if __name__ == "__main__":
    checker = StackSyntaxChecker()
    
    # --- Example 1: Valid String ---
    s1 = "([{}])"
    print("\n" + "=" * 40)
    print(f"TEST 1: Valid String (Result: {checker.isValid(s1, verbose=True)})")
    
    # --- Example 2: Invalid (Mismatched) ---
    s2 = "([)]"
    print("\n" + "=" * 40)
    print(f"TEST 2: Invalid - Mismatched (Result: {checker.isValid(s2, verbose=True)})")
    
    # --- Example 3: Invalid (Unclosed) ---
    s3 = "{[}"
    print("\n" + "=" * 40)
    print(f"TEST 3: Invalid - Unclosed (Result: {checker.isValid(s3, verbose=True)})")
    
    # --- Example 4: Invalid (Early Close) ---
    s4 = "])"
    print("\n" + "=" * 40)
    print(f"TEST 4: Invalid - Early Close (Result: {checker.isValid(s4, verbose=True)})")