class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_map = {}
        i = 0
        j = i 
        max_t = 0
        for j in range(n):
            # if it is not in the char_map, then add it to the char_map, check for max
            if (s[j] not in char_map) or (char_map[s[j]] < i):
                char_map[s[j]] = j
                if j -i + 1 > max_t:
                    max_t = j-i+1 
            else:
            # if it is already in the char_map, advance the i to the one next to he previous found
                i = char_map[s[j]] + 1
                char_map[s[j]] = j
        return max_t
