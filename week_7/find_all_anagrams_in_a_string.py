class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        n = len(p)
        result = []
        p_table = {}
        for i in p:
            if i not in p_table:
                p_table[i] = 1
            else:
                p_table[i] += 1
        
        s_table = {}
        for i in range(n):
            if s[i] not in s_table:
                s_table[s[i]] = 1
            else:
                s_table[s[i]] += 1
        
        if self.verifyAnagram(p_table, s_table):
            result.append(0)

        for i in range(n,len(s)):
            # remove the first
            if s[i-n] in s_table:
                s_table[s[i-n]] -= 1
            # add the new 
            if s[i] in s_table:
                s_table[s[i]] += 1
            else:
                s_table[s[i]] = 1
            if self.verifyAnagram(p_table, s_table):
                result.append(i - n + 1)
        return result
    
    def verifyAnagram(self,p_t, s_t):
        for k, v in p_t.items():
            if k not in s_t or v != s_t[k]:
                return False
        return True

        