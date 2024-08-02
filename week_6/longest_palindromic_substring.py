class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            _str = self.check_palindrome_centre(s,i)
            if len(_str) > len(result):
                result = _str
        return result

    def check_palindrome_centre(self, s, index):
        # check odds
        left = index - 1
        right = index + 1
        odd_str = s[index]
        while left >= 0 and right < len(s) and s[left] == s[right]:
            odd_str = ''.join([s[left], odd_str,s[right]])
            left -= 1
            right += 1
        
        # check evens
        left = index 
        right = index + 1
        even_str = ""
        while left >= 0 and right < len(s)  and s[left] == s[right]:
            even_str = ''.join([s[left], even_str,s[right]])
            left -= 1
            right += 1

        if len(odd_str) > len(even_str):
            return odd_str
        else:
            return even_str


