public class sol {

    public static boolean isPalindrome(String s) {
        if (s == null || s.isEmpty()) {
            return true;
        }

        int left = 0;
        int right = s.length() - 1;

        while (left < right) {

            // 1️⃣ Skip non-alphanumeric characters on the left
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            // 2️⃣ Skip non-alphanumeric characters on the right
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            // 3️⃣ Compare characters (case-insensitive)
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }

            // 4️⃣ Move inward
            left++;
            right--;
        }

        // ✅ If we reach here, all characters matched
        return true;
    }

    // --- Test cases ---
    public static void main(String[] args) {
        String[] testStrings = {
                "A man, a plan, a canal: Panama",
                "race a car",
                " ",
                "Madam",
                "0P",
                "a.",
                ".a"
        };

        for (String s : testStrings) {
            System.out.println("Input: \"" + s + "\" -> " + isPalindrome(s));
        }
    }
}
