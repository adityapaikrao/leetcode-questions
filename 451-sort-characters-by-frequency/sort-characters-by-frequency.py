class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        new_string = []
        for char in sorted(list(freq), key = lambda x : freq[x], reverse=True):
            new_string.append(char * freq[char])
        
        return "".join(new_string)
    
        
