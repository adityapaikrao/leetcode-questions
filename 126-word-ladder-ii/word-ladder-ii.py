class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        hit -> cog

        [hit], hit -> [hit, hot], hot -> dot -> dog -> cog
                                      -> lot -> log -> cog
        
        ["hot","dot","dog","lot","log","cog"]
        - keep track of already visited 

        red -> ted -> tad -> tax
                   -> tex -> tax
            -> rex -> 
                   
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        word_set.discard(beginWord)

        frontier = deque([beginWord]) #  curr_word
        parents = defaultdict(list) # node -> List of parents
        found = False

        while frontier and not found:
            new_words = set()
            for _ in range(len(frontier)):
                curr_word = frontier.popleft()
                
                if curr_word == endWord:
                    found = True
                    continue

                for i, ch in enumerate(curr_word):
                    curr_list = list(curr_word)
                    for idx in range(26):
                        new_char = chr(ord('a') + idx)
                        if new_char == ch: 
                            continue

                        curr_list[i] = new_char
                        new_word = "".join(curr_list)
                        if new_word in word_set:
                            parents[new_word].append(curr_word)
                            if new_word not in new_words:
                                frontier.append(new_word)
                                new_words.add(new_word)
            
            word_set -= new_words
        
        if not found:
            return []
        paths = [endWord]
        all_paths = []
        print(parents)
        def build_paths(word: str):
            if word == beginWord:
                # print(paths)
                all_paths.append(paths[::-1])
                return
            
            for parent in parents[word]:
                paths.append(parent)
                build_paths(parent)
                paths.pop()
            
            return
        
        build_paths(endWord)
        
        return all_paths
                
