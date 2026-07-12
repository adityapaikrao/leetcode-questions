class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def isEnd(self):
        return self.is_end
    def setEnd(self):
        self.is_end = True
    
    def addChar(self, char):
        if char not in self.children:
            self.children[char] = Node()
        return
    def hasChar(self, char):
        return char in self.children


class Trie:
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word):
        node = self.root
        for char in word:
            if not node.hasChar(char):
                node.addChar(char)
            node = node.children[char]
        node.setEnd()
    
    def hasPrefix(self, word) -> Tuple[bool, Node]:
        node = self.root
        prev = None
        for char in word:
            if not node.hasChar(char):
                return False, prev
            prev = None
            node = node.children[char]
        return True, node

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # create Trie
        trie = Trie()
        for terms in products:
            trie.addWord(terms)
        
        results = []
        for i in range(len(searchWord)):
            curr_list = []
            has_prefix, prefix_node = trie.hasPrefix(searchWord[:i + 1])
            if not has_prefix:
                break
            # DO BFS/DFS from here
            frontier = [(prefix_node, searchWord[:i + 1])]
            # print(searchWord[:i + 1], has_prefix, prefix_node.children.keys())
            while frontier:
                curr, string = frontier.pop()
                if curr.isEnd():
                    curr_list.append(string)
                for next_char, child_node in curr.children.items():
                    frontier.append((child_node, string + next_char))
            # 
            heapq.heapify(curr_list)
            results.append(heapq.nsmallest(3, curr_list))
        
        while len(results) != len(searchWord):
            results.append([])
        
        return results
                    
                

