# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# [[1, [] [3]], 4]
"""
0, [[1, [] [3]], 4]
stack = []

"""

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[0, nestedList]]
    
    def next(self) -> int:
        idx, nestedInt = self.stack[-1]
        self.stack[-1][0] = idx + 1
        return nestedInt[idx].getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            index, last = self.stack[-1]
            # print(index, last)
            if index == len(last):
                self.stack.pop()
                continue
            if last[index].isInteger():
                return True
            else:
                self.stack[-1][0] += 1
                self.stack.append([0, last[index].getList()])
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())