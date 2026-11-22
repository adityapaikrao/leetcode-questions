class CustomWord:
    def __init__(self, word: str):
        self.word = word
    
    def __lt__(self, other: str):
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = defaultdict(int)
        for i, word in enumerate(words):
            freq[word] += 1
        
        heap = [] # min heap 

        for word, count in freq.items():
            heapq.heappush(heap, (count, CustomWord(word)))
            if len(heap) > k:
                heapq.heappop(heap)
        
        heap.sort(reverse=True)
        return [entry[1].word for entry in heap]
                