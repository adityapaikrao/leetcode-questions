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

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]] # (nestedList, index) index is the index of elem         currently considered in this list
    
    def next(self) -> int:
        # self.hasNext()
        last, index = self.stack[-1]
        self.stack[-1][1] += 1
        return last[index].getInteger()

    
    def hasNext(self) -> bool:
        while self.stack:
            last, index = self.stack[-1]
            if index == len(last):
                self.stack.pop()
            else:
                first_elem = last[index]
                if first_elem.isInteger():
                    return True
                self.stack[-1][1] += 1
                self.stack.append([first_elem.getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())