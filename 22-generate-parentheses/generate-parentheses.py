class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_combs = []
        curr_comb = []

        def backtrack(num_opens: int, num_closes: int) -> None:
            if num_opens == num_closes == n:
                all_combs.append("".join(curr_comb))
                return
            if num_opens > n or num_closes > n:
                return
            
            # can only open from here
            if num_opens == num_closes:
                curr_comb.append("(")
                backtrack(num_opens + 1, num_closes)
                curr_comb.pop()
                return
            # can only close from here
            if num_opens == n:
                curr_comb.append(")")
                backtrack(num_opens, num_closes + 1)
                curr_comb.pop()
                return
            
            curr_comb.append("(")
            backtrack(num_opens + 1, num_closes)
            curr_comb.pop()


            curr_comb.append(")")
            backtrack(num_opens, num_closes + 1)
            curr_comb.pop()

            return
        
        backtrack(0, 0)
        return all_combs

            
