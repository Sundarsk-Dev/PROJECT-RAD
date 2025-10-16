from typing import List
def ispal(s:str)->bool:
    if not s:
        return True
    left,right=0,len(s)-1
    
    while left<right:
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower()!=s[right].lower():
            return False:
        left+=1
        right-=1
    return True

if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True), # Empty string or string with only spaces is a valid palindrome
        ("Madam", True),
        ("0P", False), # '0' vs 'P'
        ("a.", True),
        (".a", True)
    ]

    print("--- Valid Palindrome (Two Pointers) Test Results ---")
    
    for s, expected in test_cases:
        result = isPalindrome(s)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Input: '{s}' -> Result: {result}, Status: {status}\n"
        r
        