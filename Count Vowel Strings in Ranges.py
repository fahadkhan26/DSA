def vowelStrings(words, queries):
    result = []
    vowels = ["a", "e", "i", "o", "u"]
    prefix_sum = [0]
    sm = 0

    for i in range(len(words)):
        if words[i][0] in vowels and words[i][-1] in vowels:
            sm += 1
        prefix_sum.append(sm)

    for left, right in queries:
        result.append((prefix_sum[right+1] - prefix_sum[left]))
    
    return result