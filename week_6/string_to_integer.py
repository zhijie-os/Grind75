class Solution:
    def myAtoi(self, s: str) -> int:
        # remove the leading whitespace
        s = s.strip()

        if len(s) == 0:
            return 0

        # interpret signedness
        sign = 1
        if s[0] == "-":
            s = s[1::]
            sign = -1
        elif s[0] == "+":
            s = s[1::]

        # skipping the zeros
        while s and s[0] == "0":
            s = s[1::]


        str_no_digits = ""
        for i in s:
            if ord(i) >= ord('0') and ord(i) <= ord('9'):
                str_no_digits+=i
            else:
                break

        result = sign * self.read_int(str_no_digits)
        if result < -2**31:
            return -2**31
        elif result > 2**31-1:
            return 2**31-1
        else:
            return result
        return sign * self.read_int(str_no_digits)

    def read_int(self, s):
        acc = 0
        base = 1
        for i in range(len(s)-1, -1, -1):
            acc += (ord(s[i]) - ord('0'))* base
            base *= 10
        return acc