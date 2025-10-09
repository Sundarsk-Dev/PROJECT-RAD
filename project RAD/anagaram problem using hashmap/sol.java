import java.util.*;

public class sol {

    public static List<List<String>> groupAnagrams(String[] strs) {
        // Step 1: Create a HashMap to store key (sorted word) → list of words
        Map<String, List<String>> map = new HashMap<>();

        for (String word : strs) {
            // Step 2: Convert word to char array, sort it, and make a key
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            // Step 3: Add the original word into the correct group in the map
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }

        // Step 4: Return all grouped lists
        return new ArrayList<>(map.values());
    }

    public static void main(String[] args) {
        // --- Test Cases ---
        String[][] testCases = {
                { "eat", "tea", "tan", "ate", "nat", "bat" },
                { "", "" },
                { "a" },
                { "abc", "bca", "cab", "xyz" },
                { "listen", "silent", "enlist", "hello" }
        };

        int[] expectedGroups = { 3, 1, 1, 2, 2 };

        System.out.println("--- Group Anagrams Test Results ---");

        for (int i = 0; i < testCases.length; i++) {
            List<List<String>> result = groupAnagrams(testCases[i]);
            int groupCount = result.size();

            String status = (groupCount == expectedGroups[i]) ? "PASSED"
                    : "FAILED (Expected " + expectedGroups[i] + ", Got " + groupCount + ")";

            // For clean display, sort each group and then the outer list
            for (List<String> group : result) {
                Collections.sort(group);
            }
            result.sort(Comparator.comparing(o -> o.get(0)));

            System.out.println("Input: " + Arrays.toString(testCases[i]));
            System.out.println("Groups: " + result);
            System.out.println("Status: " + status + "\n");
        }
    }
}
