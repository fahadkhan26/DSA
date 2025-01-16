def numberOfSubstrings(s):
    lastSeen = [-1, -1, -1]
    count = 0
    for i in range(len(s)):
        lastSeen[ord(s[i]) - ord('a')] = i
        if -1 not in lastSeen:
            count += min(lastSeen) + 1
    return count