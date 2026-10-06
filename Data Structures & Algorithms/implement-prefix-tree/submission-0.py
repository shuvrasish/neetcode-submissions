class TrieNode:
    def __init__(self, val: str = "", children: Optional[List[Optional["TrieNode"]]] = None):
        self.val = val
        self.children = children if children else [None] * 26
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def _index(self, char: str) -> int:
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        node: TrieNode = self.root

        for char in word:
            ind: int = self._index(char)
            if not node.children[ind]:
                node.children[ind] = TrieNode(char)
            node = node.children[ind]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            ind = self._index(char)
            if node.children[ind]:
                node = node.children[ind]
            else:
                return False
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            ind = self._index(char)
            if node.children[ind]:
                node = node.children[ind]
            else:
                return False
        return True
        