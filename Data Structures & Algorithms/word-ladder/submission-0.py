class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        q = deque()
        q.append((beginWord, 1))

        wordSet.discard(beginWord)

        while q:
            currentWord, currDist = q.popleft()

            if currentWord == endWord:
                return currDist

            for charIndex in range(len(currentWord)):
                word_list = list(currentWord)
                
                for newCharDist in range(26):
                    word_list[charIndex] = chr(ord('a') + newCharDist)
                    newWord = "".join(word_list)
                    if newWord in wordSet:
                        # print(f"newWord: {newWord}, level: {currDist}")
                        q.append((newWord, currDist + 1))
                        wordSet.remove(newWord)
                
        return 0
                        
