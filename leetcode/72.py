# 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        return self.minDistanceH(word1, word2, 0, 0, dp)

    def minDistanceH(self, word1, word2, p1, p2, dp):
        if p1 == len(word1) and p2 == len(word2):
            return 0
        elif p2 == len(word2):
            return len(word1) - p1 # delete all remaining
        elif p1 == len(word1):
            return len(word2) - p2 # inserting all the missing
        if p1 >= len(word1):
            return sys.maxsize
        if p2 >= len(word2):
            return sys.maxsize
        if dp[p1][p2] != -1:
            return dp[p1][p2]

        minDist = sys.maxsize
        # replace
        dists = []
        dists.append(self.minDistanceH(word1, word2, p1+1, p2+1, dp)+1)
        # remove
        dists.append(self.minDistanceH(word1, word2, p1+1, p2, dp)+1)
        # insert
        dists.append(self.minDistanceH(word1, word2, p1, p2+1, dp)+1)
        # matched on first char
        if word1[p1] == word2[p2]:
            dists.append(self.minDistanceH(word1, word2, p1+1, p2+1, dp))

        dp[p1][p2] = min(dists)
        print(p1, p2, dists)
        return dp[p1][p2]
