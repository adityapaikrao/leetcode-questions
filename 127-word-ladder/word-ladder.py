from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        q = deque([beginWord])
        word_set.discard(beginWord)
        seq_len = 1

        while q:
            size = len(q)
            for _ in range(size):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return seq_len
                
                for i, char in enumerate(curr_word):
                    for pos in range(26):
                        new_char = chr(ord('a') + pos)
                        if new_char == char: continue

                        next_word = curr_word[:i] + new_char + curr_word[i + 1:]
                        if next_word in word_set:
                            word_set.remove(next_word)
                            q.append(next_word)
            seq_len += 1

        return 0


