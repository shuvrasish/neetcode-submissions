class TrieNode:
    def __init__(self, val: str = "", children: Optional[List[Optional["TrieNode"]]] = None):
        self.val: str = val
        self.children: Optional[List[Optional["TrieNode"]]] = children if children else [None] * 26
        self.is_end: bool = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def _index(self, char: str) -> int:
        return ord(char) - ord('a')
        

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            ind = self._index(char)

            if not node.children[ind]:
                node.children[ind] = TrieNode(char)
            node = node.children[ind]
        
        node.is_end = True


    def search(self, word: str) -> bool:
        def dfs(node: Optional[TrieNode], wordIndex: int) -> bool:
            if wordIndex == len(word):
                return node.is_end

            char = word[wordIndex]

            if char != ".":
                ind = self._index(char)

                if not node.children[ind]:
                    return False
                return dfs(node.children[ind], wordIndex + 1)

            found = False
            for child in node.children:
                if not child:
                    continue
                found = found or dfs(child, wordIndex + 1)
                if found:
                    return True
            return False

        return dfs(self.root, 0)
