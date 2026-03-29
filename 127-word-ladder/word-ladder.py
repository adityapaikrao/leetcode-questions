class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        
        if endWord not in word_set:
            return 0
        
        seq_len = 0
        q = deque([beginWord])
        word_set.discard(beginWord)

        while q:
            seq_len += 1
            for _ in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return seq_len
                for i in range(len(curr_word)):
                    for ch in range(26):
                        new_word = curr_word[:i] + chr(ord('a') + ch) + curr_word[i+1:]
                        if new_word in word_set:
                            word_set.discard(new_word) 
                            q.append(new_word)
        return 0