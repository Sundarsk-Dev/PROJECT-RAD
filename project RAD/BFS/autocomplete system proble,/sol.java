import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    Map<String, Integer> counts = new HashMap<>();
}

class AutocompleteSystem {
    private TrieNode root;
    private TrieNode currentNode;
    private StringBuilder currentQuery;

    public AutocompleteSystem(String[] sentences, int[] times) {
        root = new TrieNode();
        currentNode = root;
        currentQuery = new StringBuilder();

        for (int i = 0; i < sentences.length; i++) {
            insert(sentences[i], times[i]);
        }
    }

    private void insert(String sentence, int time) {
        TrieNode node = root;
        for (char c : sentence.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.counts.put(sentence, node.counts.getOrDefault(sentence, 0) + time);
    }

    private List<Map.Entry<String, Integer>> dfsSearch(TrieNode node) {
        List<Map.Entry<String, Integer>> result = new ArrayList<>();
        result.addAll(node.counts.entrySet());

        for (TrieNode child : node.children.values()) {
            result.addAll(dfsSearch(child));
        }

        return result;
    }

    public List<String> input(char c) {
        // Case 1: End of sentence
        if (c == '#') {
            insert(currentQuery.toString(), 1);
            currentQuery = new StringBuilder();
            currentNode = root;
            return new ArrayList<>();
        }

        // Case 2: Add character to query
        currentQuery.append(c);

        if (currentNode == null)
            return new ArrayList<>();

        if (!currentNode.children.containsKey(c)) {
            currentNode.children.put(c, new TrieNode());
            currentNode = currentNode.children.get(c);
            return new ArrayList<>();
        }

        currentNode = currentNode.children.get(c);
        List<Map.Entry<String, Integer>> allResults = dfsSearch(currentNode);

        // Sort by count desc, then alphabetically
        allResults.sort((a, b) -> {
            if (!a.getValue().equals(b.getValue())) {
                return b.getValue() - a.getValue();
            }
            return a.getKey().compareTo(b.getKey());
        });

        List<String> top3 = new ArrayList<>();
        for (int i = 0; i < Math.min(3, allResults.size()); i++) {
            top3.add(allResults.get(i).getKey());
        }

        return top3;
    }

    public static void main(String[] args) {
        String[] sentences = { "i love you", "i love python", "i like coffee", "best coffee ever" };
        int[] times = { 5, 3, 2, 8 };

        AutocompleteSystem acs = new AutocompleteSystem(sentences, times);

        System.out.println("Input: i -> " + acs.input('i'));
        System.out.println("Input:  (space) -> " + acs.input(' '));
        System.out.println("Input: l -> " + acs.input('l'));
        System.out.println("Input: # -> " + acs.input('#'));
        System.out.println("Input: b -> " + acs.input('b'));
    }
}
