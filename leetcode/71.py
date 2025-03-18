# 71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        path += '/'
        stack = []
        curr = ""
        for c in path:
            if c == '/':
                if curr != "":
                    if curr == "..":
                        if len(stack)>0:
                            stack.pop() # go back for one directory
                    elif curr != ".":
                        stack.append(curr)
                    curr = ""
            else:
                curr += c
        result = ""
        for c in stack:
            result += "/"
            result += c
        if result=="":
            return "/"
        return result