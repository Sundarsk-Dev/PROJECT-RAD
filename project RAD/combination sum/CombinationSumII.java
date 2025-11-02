import java.util.*;

public class CombinationSumII {

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates); // Step 1: Sort for pruning
        List<List<Integer>> results = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), results);
        return results;
    }

    private void backtrack(int[] candidates, int remaining, int startIndex,
            List<Integer> combination, List<List<Integer>> results) {
        // Base Case 1: Found a valid combination
        if (remaining == 0) {
            results.add(new ArrayList<>(combination));
            return;
        }

        // Base Case 2: Remaining < 0 → invalid path
        if (remaining < 0)
            return;

        // Explore candidates
        for (int i = startIndex; i < candidates.length; i++) {

            // Duplicate Pruning
            if (i > startIndex && candidates[i] == candidates[i - 1])
                continue;

            // Early stop if number is too large
            if (candidates[i] > remaining)
                break;

            // Choose
            combination.add(candidates[i]);

            // Recurse: move to next index (each element can be used once)
            backtrack(candidates, remaining - candidates[i], i + 1, combination, results);

            // Unchoose (backtrack)
            combination.remove(combination.size() - 1);
        }
    }

    // --- Test Cases ---
    public static void main(String[] args) {
        CombinationSumII solver = new CombinationSumII();

        int[][] candidatesList = {
                { 10, 1, 2, 7, 6, 1, 5 },
                { 2, 5, 2, 1, 2 },
                { 1, 1, 1, 1, 1, 1, 1 }
        };

        int[] targets = { 8, 5, 2 };

        System.out.println("--- Combination Sum II (Backtracking with Duplicate Pruning) ---");
        for (int i = 0; i < candidatesList.length; i++) {
            List<List<Integer>> results = solver.combinationSum2(candidatesList[i], targets[i]);
            System.out.println("Candidates: " + Arrays.toString(candidatesList[i]) +
                    ", Target: " + targets[i]);
            System.out.println("Results: " + results);
            System.out.println();
        }
    }
}
