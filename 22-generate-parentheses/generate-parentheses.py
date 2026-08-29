class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_combs = []
        curr_comb = []

        def get_combs(num_opens: int, num_closes: int) -> None:
            # Base Cases
            if num_opens == num_closes == n:
                all_combs.append("".join(curr_comb))
                return
            if num_opens > n or num_closes > n:
                return
            
            # Recursive Cases
            if num_opens == num_closes:
                # can only opne from here
                curr_comb.append("(")
                get_combs(num_opens + 1, num_closes)
                curr_comb.pop()
                return
            
            if num_opens == n:
                curr_comb.append(")")
                get_combs(num_opens, num_closes + 1)
                curr_comb.pop()
                return
            
            # try either option
            curr_comb.append(")")
            get_combs(num_opens, num_closes + 1)
            curr_comb.pop()
        
            curr_comb.append("(")
            get_combs(num_opens + 1, num_closes)
            curr_comb.pop()

            return
        
        get_combs(0, 0)
        return all_combs
            