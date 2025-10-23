from typing import Dict, Optional
import collections

# --- 1. Trie Node Definition ---

class TrieNode:
    def __init__(self):
        # Using a defaultdict for children simplifies insertion
        self.children: Dict[str, TrieNode] = collections.defaultdict(TrieNode)
        # Flag to mark if this node completes an inserted word
        self.is_end_of_word: bool = False

# --- 2. Trie Class Implementation ---

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts the word into the trie."""
        node = self.root
        for char in word:
            # If the char is not in children, defaultdict creates a new TrieNode
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True

    def _traverse(self, key: str) -> Optional[TrieNode]:
        """Helper function to traverse the trie for a given key (word or prefix)."""
        node = self.root
        for char in key:
            if char not in node.children:
                return None  # Path broken
            node = node.children[char]
        return node

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie."""
        node = self._traverse(word)
        # Word is found only if the full path exists AND it's marked as an end-of-word
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """Returns True if there is any word that starts with the given prefix."""
        node = self._traverse(prefix)
        # Prefix is found if the full path exists
        return node is not None

# --- 3. Test Cases ---

if __name__ == "__main__":
    trie = Trie()
    
    # 1. Insert words
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apply")
    trie.insert("banana")

    print("--- Implement Trie Test Results ---")
    
    # Test 1: Search for an existing full word
    print(f"Search 'apple': {trie.search('apple')} (Expected: True)")
    
    # Test 2: Search for a prefix that is NOT an end-of-word
    print(f"Search 'app': {trie.search('app')} (Expected: True)") # 'app' was inserted
    
    # Test 3: Search for a non-existent word
    print(f"Search 'apps': {trie.search('apps')} (Expected: False)")
    
    # Test 4: Check if any word starts with an existing prefix
    print(f"StartsWith 'app': {trie.startsWith('app')} (Expected: True)")
    
    # Test 5: Check if any word starts with a non-existent prefix
    print(f"StartsWith 'bat': {trie.startsWith('bat')} (Expected: False)")
    
    # Test 6: Check for another existing prefix
    print(f"StartsWith 'ban': {trie.startsWith('ban')} (Expected: True)")
    
    # Test 7: Search for a word that is a prefix of another, but not marked as end-of-word
    trie2 = Trie()
    trie2.insert("application")
    print(f"\nSearch 'app' after inserting 'application': {trie2.search('app')} (Expected: False)")s