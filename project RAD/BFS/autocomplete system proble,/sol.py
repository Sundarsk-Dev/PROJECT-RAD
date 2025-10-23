from typing import List, Dict, Optional, Tuple
import collections

# --- 1. Trie Node Structure ---
class TrieNode:
    def __init__(self):
        # Maps character to the next TrieNode
        self.children: Dict[str, TrieNode] = collections.defaultdict(TrieNode)
        # Stores hit count for sentences ending at this node.
        self.counts: collections.defaultdict[str, int] = collections.defaultdict(int)

# --- 2. Autocomplete System Class ---
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.current_query: str = ""
        self.current_node: Optional[TrieNode] = self.root
        
        # Build the initial Trie
        for s, t in zip(sentences, times):
            self._insert(s, t)

    def _insert(self, sentence: str, time: int):
        """Helper to insert a sentence into the Trie."""
        node = self.root
        for char in sentence:
            node = node.children[char]
        # Store the sentence and update its count at the final node
        node.counts[sentence] += time

    def _dfs_search(self, node: TrieNode) -> List[Tuple[int, str]]:
        """Helper to collect all (count, sentence) pairs reachable from a node."""
        results = []
        # DFS to traverse all children
        for child_node in node.children.values():
            results.extend(self._dfs_search(child_node))
        
        # Collect results from the current node's ending sentences
        for sentence, count in node.counts.items():
            results.append((-count, sentence)) # Use -count for Min-Heap/Min-Sort behavior
        
        return results

    def input(self, c: str) -> List[str]:
        # Case 1: End of Query
        if c == '#':
            if self.current_query:
                # Update the count for the completed sentence
                self._insert(self.current_query, 1)
            
            # Reset state for the next query
            self.current_query = ""
            self.current_node = self.root
            return []
        
        # Case 2: Continuing the Query
        self.current_query += c
        
        # If the last character led to a dead end, all future searches will be empty
        if self.current_node is None:
            return []

        # Traverse to the next node
        if c in self.current_node.children:
            self.current_node = self.current_node.children[c]
        else:
            # Dead end reached
            self.current_node = None
            return []

        # Find all sentences starting with the current query using DFS
        # We need the results from the current node AND all its children
        results = []
        if self.current_node:
            results.extend(self._dfs_search(self.current_node))

        # Add sentences that end *at* the current node's position
        for sentence, count in self.current_node.counts.items():
            results.append((-count, sentence))
        
        # Sort results: first by count (desc), then by sentence (alpha asc)
        # Sorting by tuple automatically handles this: (-count, sentence)
        results.sort()
        
        # Return the top 3 sentences
        return [s for count, s in results[:3]]

# --- Test Cases ---

if __name__ == "__main__":
    
    sentences = ["i love you", "i love python", "i like coffee", "best coffee ever"]
    times = [5, 3, 2, 8]
    
    acs = AutocompleteSystem(sentences, times)
    
    print("--- Autocomplete System Test ---")
    
    # 1. Start typing 'i'
    result1 = acs.input('i')
    # Expected: ["i love you", "i love python", "i like coffee"]
    print(f"Input 'i': {result1}")
    
    # 2. Continue with ' '
    result2 = acs.input(' ')
    # Expected: ["i love you", "i love python", "i like coffee"]
    print(f"Input ' ': {result2}")
    
    # 3. Continue with 'l' (i l)
    result3 = acs.input('l')
    # Expected: ["i love you", "i love python", "i like coffee"]
    print(f"Input 'l': {result3}")

    # 4. Finish and update count
    result4 = acs.input('#')
    # Expected: [] (The sentence "i l" is now recorded with count 1)
    print(f"Input '#': {result4}")

    # 5. Type a new popular prefix 'b'
    result5 = acs.input('b')
    # Expected: ["best coffee ever"]
    print(f"Input 'b': {result5}")