class TrieNode:
    def __init__(self, children: Optional[List[Optional["TrieNode"]]] = None) -> None:
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r: int, c: int, node: Optional[TrieNode], word: str) -> None:
            if (
                r < 0 or c < 0 or r >= rows or c >= cols 
                or (r,c) in visited 
                or not node.children 
                or board[r][c] not in node.children
            ):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_end:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.discard((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)

