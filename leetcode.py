class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
    def search(self, word: str) -> bool:
        return self._search(word, 0, self.root)
    
    def _search(self, word, index, node):
        if index >= len(word):
            return node.is_end
        
        c = word[index]

        if c == '.':
            for child in node.children.values():
                if self._search(word, index + 1, child):
                    return True
            return False
        
        else:
            if c not in node.children:
                return False
            return self._search(word, index + 1, node.children[c])

            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)