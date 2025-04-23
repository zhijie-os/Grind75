# 211. Design Add and Search Words Data Structure
class WordDictionary:

    def __init__(self):
        self.trie = {}    
    
    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = True 

    def search(self, word: str) -> bool:
        q = [self.trie]
        nextLevel = []

        for c in word:
            if not q:
                return False

            while q:
                curr = q.pop(0) # search the first
                if c == '.':
                    for k,v in curr.items():
                        if k != '*':
                            nextLevel.append(v)
                else:
                    if c in curr:
                        nextLevel.append(curr[c])

            q = nextLevel
            nextLevel = []

        for i in q:
            if '*' in i:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)