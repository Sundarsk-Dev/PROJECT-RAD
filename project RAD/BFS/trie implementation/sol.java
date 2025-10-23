import java.util.HashMap;
import java.util.Map;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEndOfWord = false;
}

class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Insert a word into the Trie
    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEndOfWord = true;
    }

    // Helper to traverse the Trie
    private TrieNode traverse(String key) {
        TrieNode node = root;
        for (char c : key.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return null; // path breaks
            }
            node = node.children.get(c);
        }
        return node;
    }

    // Search for a full word
    public boolean search(String word) {
        TrieNode node = traverse(word);
        return node != null && node.isEndOfWord;
    }

    // Check if any word starts with a given prefix
    public boolean startsWith(String prefix) {
        return traverse(prefix) != null;
    }

    // --- For testing ---
    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("apple");
        trie.insert("app");
        trie.insert("apply");
        trie.insert("banana");

        System.out.println("--- Implement Trie Test Results ---");
        System.out.println("Search 'apple': " + trie.search("apple") + " (Expected: true)");
        System.out.println("Search 'app': " + trie.search("app") + " (Expected: true)");
        System.out.println("Search 'apps': " + trie.search("apps") + " (Expected: false)");
        System.out.println("StartsWith 'app': " + trie.startsWith("app") + " (Expected: true)");
        System.out.println("StartsWith 'bat': " + trie.startsWith("bat") + " (Expected: false)");
        System.out.println("StartsWith 'ban': " + trie.startsWith("ban") + " (Expected: true)");

        Trie trie2 = new Trie();
        trie2.insert("application");
        System.out
                .println("\nSearch 'app' after inserting 'application': " + trie2.search("app") + " (Expected: false)");
    }
}
