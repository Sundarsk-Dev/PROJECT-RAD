from typing import List, Dict
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups anagrams using a Hash Map where the key is the sorted version 
    of the word (the canonical key).
    
    Time Complexity: O(N * K log K), where N is the number of strings and 
                     K is the average length of a string (due to sorting each string).
    Space Complexity: O(N * K), for storing the map and the resulting groups.
    """
    # Use defaultdict to automatically initialize a list for a new key
    # Key: Sorted string (e.g., "aet"), Value: List of original strings
    anagram_groups: Dict[str, List[str]] = defaultdict(list)
    
    for word in strs:
        # 1. Create the Canonical Key: Sort the characters and join them back into a string
        # Example: "eat" -> ['e', 'a', 't'] -> ['a', 'e', 't'] -> "aet"
        key = "".join(sorted(word))
        
        # 2. Use the key to group the original word in the Hash Map
        anagram_groups[key].append(word)
        
    # 3. Return all the grouped lists (the values of the Hash Map)
    return list(anagram_groups.values())

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], 3),
        (["", ""], 1),
        (["a"], 1),
        (["abc", "bca", "cab", "xyz"], 2),
        (["listen", "silent", "enlist", "hello"], 2),
    ]

    print("--- Group Anagrams Test Results ---")
    
    for strs, expected_group_count in test_cases:
        result = groupAnagrams(strs)
        result_group_count = len(result)
        
        # We only check the number of groups, as the internal order can vary
        status = "PASSED" if result_group_count == expected_group_count else f"FAILED (Expected {expected_group_count} groups, Got {result_group_count})"
        
        # To make the output clean, we sort the inner lists and the outer list
        # This is for display verification only, not part of the algorithm logic
        display_result = sorted([sorted(group) for group in result])
        
        print(f"Input: {strs}\nGroups: {display_result}, Status: {status}\n")