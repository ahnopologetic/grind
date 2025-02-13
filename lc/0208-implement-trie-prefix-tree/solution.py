class Trie:

    def __init__(self):
        self.storage = {}

    def insert(self, word: str) -> None:
        self.storage[word] = True
        

    def search(self, word: str) -> bool:
        return word in self.storage.keys()
        

    def startsWith(self, prefix: str) -> bool:
        good = [k.startswith(prefix) for k in self.storage.keys()]
        return any(good)
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
