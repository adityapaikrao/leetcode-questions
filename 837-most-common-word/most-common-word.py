class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned = set(banned)
        hmap = defaultdict(int) # word -> freq
        i = 0 

        while i < len(paragraph):
            # skip spaces or non chars
            while i < len(paragraph) and not paragraph[i].isalpha():
                i += 1
            
            # read word
            j = i
            while j < len(paragraph) and paragraph[j].isalpha():
                j += 1
            word = paragraph[i: j].lower()
            if word not in banned: hmap[word] += 1
            i = j
        
        return max(hmap, key=hmap.get)