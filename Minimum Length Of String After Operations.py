from collections import Counter

def minimumlength(s):
    count = Counter(s)
    for i in count:
        if count[i] % 2 == 0:
            count[i] = 2
        else:
            count[i] = 1
    
    return sum(count.values())