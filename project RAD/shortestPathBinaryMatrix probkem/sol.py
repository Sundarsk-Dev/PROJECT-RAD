from collections import deque
from typing import List

def shortestPathBinaryMatrix(grid:List[List[int]]) -> int:
    n=len(grid)
    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return -1
    if n==1:
        return 1
    queue=deque([(0,0,1)])
    
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0), 
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    grid[0][0]=1
    while queue:
        r,c,d=queue.popleft()
        if r==n-1 and c==n-1:
            return d
        for dr,dc in directions:
            nr,nc=r+dr,c+dc
            
            if 0<=nr<n and 0<= nc<n and grid[nr][nc]==0:
                queue.append((nr,nc,d+1))
                grid[nr][nc]=1
    return -1


if __name__ == "__main__":
    # Note: The grid is modified in-place, so deep copies are recommended for multiple tests 
    # if using the same grid array, but here we define separate inputs for simplicity.
    
    test_cases = [
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4), # Path: (0,0)->(0,1)->(0,2)->(1,2)->(2,2)
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1), # Blocked start
        ([[0]], 1),
        ([[0, 0, 0], [1, 0, 0], [1, 1, 0]], 3) # Path: (0,0)->(1,1)->(2,2) - diagonal is key
    ]

    print("--- Shortest Path in Binary Matrix (BFS) Test Results ---")
    
    import copy
    
    for original_grid, expected in test_cases:
        # Use a copy since the function modifies the grid in place
        grid_copy = copy.deepcopy(original_grid)
        
        result = shortestPathBinaryMatrix(grid_copy)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Grid: {original_grid[0]}... -> Path Length: {result}, Status: {status}\n")