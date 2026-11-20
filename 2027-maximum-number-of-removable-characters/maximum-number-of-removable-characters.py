class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        """
            i
        a b c a c b
        
            j
        a b

        at each removable i: check if still subsequence after removing
            - if p[j:] substring of s[i + 1:] 
            -
        find until when we can increase i 
        """
        n, m = len(s), len(p)
        
        def isSubsequence(p: str, curr: str, k: int) -> bool:
            if len(p) > len(curr):
                return False
            j = 0
            removed = set(removable[:k])
            for i, char in enumerate(s):
                if i in removed: continue
                if char == p[j]:
                    j += 1
                if j == len(p): return True
            return False
            
        low = 0
        high = len(removable)
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            # print(mid)
            if not isSubsequence(p, s, mid): 
                high = mid - 1
            else:
                answer = mid
                low = mid + 1
    
        return answer
        

        