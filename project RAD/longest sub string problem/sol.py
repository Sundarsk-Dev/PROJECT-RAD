from typing import List

def lcs(text1:str,text2:str) -> int:
    m=len(text1)
    n=len(text2)
    dp=[[0]*(n+1)for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
    

if __name__ == "__main__":
    test_cases = [
        ("abcde", "ace", 3),      # LCS: "ace"
        ("abc", "abc", 3),        # LCS: "abc"
        ("abc", "def", 0),        # LCS: ""
        ("bl", "yby", 1),         # LCS: "b"
        ("zxabcdezy", "yzabcdezx", 6) # LCS: "abcdez"
    ]

    print("--- Longest Common Subsequence Test Results ---")
    all_passed = True
    
    for text1, text2, expected in test_cases:
        result = lcs(text1, text2)
        
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"'{text1}' vs '{text2}' -> Length: {result}, Status: {status}")
        
        if result != expected:
            all_passed = False
            
    if all_passed:
        print("\n✅ All test cases passed successfully!")
    else:
        print("\n❌ Some test cases failed.")