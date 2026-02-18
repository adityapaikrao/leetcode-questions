class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        all_combs = []
        curr_comb = []

        char_map = {
            "1": [],                "2": ['a', 'b','c'],    "3": ['d','e','f'],
            "4": ['g','h','i'],     "5": ['j','k','l'],     "6": ['m','n','o'],
            "7": ['p','q','r','s'], "8": ['t','u','v'],     "9": ['w','x','y','z']
        }

        def get_combs(idx: int) -> None:
            # Base Case: reached end
            if idx >= len(digits):
                all_combs.append("".join(curr_comb[:]))
                return
            
            # Choose what char to use
            for char in char_map[digits[idx]]:
                curr_comb.append(char)
                get_combs(idx + 1)
                curr_comb.pop()
            
            return
        
        get_combs(0)

        return all_combs
        