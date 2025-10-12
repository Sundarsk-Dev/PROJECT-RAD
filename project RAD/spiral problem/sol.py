from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """
    Returns all elements of a matrix in spiral order using four boundary pointers.
    
    Time Complexity: O(m * n)
    Space Complexity: O(1) (excluding the result array)
    """
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    result = []
    
    # Initialize the four boundary pointers
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    
    while top <= bottom and left <= right:
        
        # 1. Go Right (Top Row)
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        
        # 2. Go Down (Right Column)
        if top <= bottom: # Check if there's still a row to process
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1
            
        # 3. Go Left (Bottom Row)
        if top <= bottom and left <= right: # Check if there's still a column/row to process
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1
            
        # 4. Go Up (Left Column)
        if top <= bottom and left <= right: # Final check
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
            
    return result

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ([[1], [2], [3]], [1, 2, 3]), # Vertical (N x 1)
        ([[1, 2, 3]], [1, 2, 3]), # Horizontal (1 x N)
        ([[1]], [1]),
    ]

    print("--- Spiral Matrix Traversal Test Results ---")
    
    for matrix, expected in test_cases:
        result = spiralOrder(matrix)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Matrix: {matrix}")
        print(f"Spiral Order: {result}, Status: {status}\n")