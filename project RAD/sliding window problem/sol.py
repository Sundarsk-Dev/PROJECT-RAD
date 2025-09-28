def lengthls(s: str) -> int:
    charset = set()
    left =0
    maxlen = 0
    for right in range(len(s)):
        while s[right] in charset:
            charset.remove(s[left])
            left +=1
        charset.add(s[right])
        currentlen = right - left +1
        maxlen = max(maxlen,currentlen)
    return maxlen

s1="abcabc"
s2="bbbbbb"
print(f"Longest unique substring in '{s1}':{lengthls(s1)}")
print(f"Longest unique substring in '{s2}':{lengthls(s2)}")