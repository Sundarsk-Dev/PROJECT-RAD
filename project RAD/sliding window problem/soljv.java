import java.util.HashSet;
import java.util.Set;

public class soljv {
    public static int lengthOfLongestSubstring(String s) {
        Set<Character> charSet = new HashSet<>();

        int left = 0; // Left pointer
        int maxLength = 0; // Result

        // Right pointer expands window
        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            // Shrink window if duplicate found
            while (charSet.contains(currentChar)) {
                charSet.remove(s.charAt(left));
                left++;
            }

            // Add current char
            charSet.add(currentChar);

            // Update max length
            int currentLength = right - left + 1;
            maxLength = Math.max(maxLength, currentLength);
        }

        return maxLength;
    }

    public static void main(String[] args) {
        String s1 = "abcabcbb";
        String s2 = "bbbbb";
        String s3 = "pwwkew";
        String s4 = "dvdf";

        System.out.println("Longest unique substring in '" + s1 + "': " + lengthOfLongestSubstring(s1)); // 3
        System.out.println("Longest unique substring in '" + s2 + "': " + lengthOfLongestSubstring(s2)); // 1
        System.out.println("Longest unique substring in '" + s3 + "': " + lengthOfLongestSubstring(s3)); // 3
        System.out.println("Longest unique substring in '" + s4 + "': " + lengthOfLongestSubstring(s4)); // 3
    }
}
