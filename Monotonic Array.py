class Solution:
    def maxScore(self, s: str) -> int:
        maxScore = 0
        ones = s.count("1")
        zeros = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            maxScore = max(maxScore, zeros + ones)
        return maxScore
