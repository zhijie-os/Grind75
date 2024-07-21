class Solution:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t == "+":
                r = stack.pop()
                l = stack.pop()
                stack.append(l+r)
            elif t == "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(l-r)
            elif t == "*":
                r = stack.pop()
                l = stack.pop()
                stack.append(l*r)
            elif t =="/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l/r))
            else:
                stack.append(int(t))
        return stack[0]

s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))