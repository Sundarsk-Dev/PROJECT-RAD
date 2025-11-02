from typing import List

class CombinationSumII:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # 1. Sort the candidates (Essential for duplicate pruning)
        candidates.sort()
        
        results = []
        
        def backtrack(start_index: int, combination: List[int], remaining: int):
            
            # Base Case 1: Success
            if remaining == 0:
                results.append(list(combination)) # Deep copy the combination
                return

            # Base Case 2: Failure/Pruning
            if remaining < 0:
                return

            # Recursive Step: Loop through remaining candidates
            for i in range(start_index, len(candidates)):
                
                # CRUCIAL DUPLICATE PRUNING:
                # If the current element is the same as the previous element, 
                # we skip it to prevent duplicate combinations.
                # The condition i > start_index ensures we only skip duplicates
                # that are siblings in the recursion tree, not the first occurrence.
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                # Optimization: Further pruning if the current number is too large
                if candidates[i] > remaining:
                    break
                
                # 1. Choose
                combination.append(candidates[i])
                
                # 2. Recurse: Use i + 1 because each number can only be used once
                backtrack(i + 1, combination, remaining - candidates[i])
                
                # 3. Unchoose (Backtrack)
                combination.pop()

        backtrack(0, [], target)
        return results

# --- Test Cases ---

if __name__ == "__main__":
    solver = CombinationSumII()
    
    test_cases = [
        ([10, 1, 2, 7, 6, 1, 5], 8, [
            [1, 7], [1, 2, 5], [2, 6], [1, 1, 6]
        ]),
        ([2, 5, 2, 1, 2], 5, [
            [1, 2, 2], [5]
        ]),
        ([1, 1, 1, 1, 1, 1, 1], 2, [
            [1, 1]
        ]),
        ([3, 1, 3, 5, 1, 1], 6, [
            [1, 1, 4], [1, 5], [3, 3] # Note: Sorted input [1, 1, 1, 3, 3, 5]
        ])
    ]

    print("--- Combination Sum II (Backtracking with Duplicate Pruning) Test Results ---")
    
    for candidates, target, expected in test_cases:
        result = solver.combinationSum2(candidates, target)
        
        # Sort results for consistent comparison
        result_sorted = sorted(map(sorted, result))
        expected_sorted = sorted(map(sorted, expected))
        
        status = "PASSED" if result_sorted == expected_sorted else f"FAILED (Expected: {expected_sorted}, Got: {result_sorted})"
        
        print(f"Candidates: {candidates}, Target: {target} -> Status: {status}")