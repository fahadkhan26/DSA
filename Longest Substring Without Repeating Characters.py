def longestSubs(s):
    l = 0
    r = 0
    seen = {}
    maxlen = 0

    for r in range(len(s)):
        if s[r] in seen:
            while s[l] != s[r]:
                del seen[s[l]]
                l += 1
            l += 1
        else:
            maxlen = max(maxlen, r-l+1)
            seen[s[r]] = 1
            
    return maxlen