class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        new_root = self.root
        for ch in word:
            alpha_index = ord(ch) - ord('a')
            if new_root.children[alpha_index] == None:
                new_root.children[alpha_index] = TrieNode()
            new_root = new_root.children[alpha_index]
        new_root.is_end = True
        

    def search(self, word: str) -> bool:
        new_root = self.root
        for ch in word:
            alpha_index = ord(ch) - ord('a')
            if new_root.children[alpha_index] is None:
                return False
            new_root = new_root.children[alpha_index]
        if new_root.is_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        new_root = self.root
        for ch in prefix:
            alpha_index = ord(ch) - ord('a')
            if new_root.children[alpha_index] == None:
                return False
            new_root = new_root.children[alpha_index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
