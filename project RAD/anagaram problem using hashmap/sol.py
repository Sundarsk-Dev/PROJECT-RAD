from typing import List,Dict
from collections import defaultdict

def anagrap(strs:list[str])->List[List[str]]:
    anagram:Dict[str,List[str]]=defaultdict(list)
    for word in strs:
        key="".join(sorted(word))
        anagram[key].append(word)
    return list(anagram.values())
    
if __name__ == "__main__":
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], 3),
        (["", ""], 1),
        (["a"], 1),
        (["abc", "bca", "cab", "xyz"], 2),
        (["listen", "silent", "enlist", "hello"], 2),
    ]
    

    for strs, expected_group_count in test_cases:
        result = anagrap(strs)
        result_group_count = len(result)
        
        # We only check the number of groups, as the internal order can vary
        status = "PASSED" if result_group_count == expected_group_count else f"FAILED (Expected {expected_group_count} groups, Got {result_group_count})"
        
        # To make the output clean, we sort the inner lists and the outer list
        # This is for display verification only, not part of the algorithm logic
        display_result = sorted([sorted(group) for group in result])
        
        print(f"Input: {strs}\nGroups: {display_result}, Status: {status}\n")
