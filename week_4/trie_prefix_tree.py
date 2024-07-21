class Trie:

    def __init__(self):
        self.trie = {}
        
    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {} # create new branch
            curr = curr[c] # go down one level
        curr["*"] = {} # mark the end of a word


    def search(self, word: str) -> bool:
        curr = self.trie
        for c in word:
            if c not in curr:
                 return False
            curr = curr[c]
        return "*" in curr
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for c in prefix:
            if c not in curr:
                 return False
            curr = curr[c]
        return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))