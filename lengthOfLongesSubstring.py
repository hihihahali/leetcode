def lengthOfLongestSubstring(str):
    maxlen = 1
    sub = ""
    for x in str:
        if x not in sub:
            sub = sub + x
            maxlen = max(maxlen, len(sub))
        else:
            sub = sub.split(x)[1] + x
    return maxlen


haha = "abcabcbb"
hihi = lengthOfLongestSubstring(haha)
print(hihi)

