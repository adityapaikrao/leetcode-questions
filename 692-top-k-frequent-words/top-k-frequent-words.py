class CustomWord:
    def __init__(self, word: str):
        self.word = word
    
    def __lt__(self, other: str):
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        n = len(words)
        buckets = [[] for _ in range(n + 1)]
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        
        for word, count in freq.items():
            buckets[count].append(word)
        
        top_k = []
        for i in range(n, -1, -1):
            buckets[i].sort()
            needed = k - len(top_k)
            if needed < 0: break
            top_k.extend(buckets[i][:needed])
        
        return top_k

            
                