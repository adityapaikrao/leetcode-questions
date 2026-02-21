class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        2, 5, 2, 1, 2
                    []
                [2]                             []
            x     [2]                      [5].       []
              [2,2]        [2]                   [2].  []
        [2,2,1]. [2, 2] [2,1]  [2]
        
        - can create duplicates of same prev element being selected
        - choose to select or skip && never select
        """
        all_combs = []
        curr_comb = []
        candidates.sort()

        def get_combinations(index: int, curr_target: int) -> None:
            if curr_target == 0:
                all_combs.append(curr_comb[:])
                return 
            
            if index >= len(candidates):
                return

            # early exit: number > curr_target
            if candidates[index] > curr_target:
                return
            
            # choose candidate
            curr_comb.append(candidates[index])
            get_combinations(index + 1, curr_target - candidates[index])
            curr_comb.pop()

            # skip and never choose again
            i = index
            while i < len(candidates) and candidates[i] == candidates[index]:
                i += 1
            get_combinations(i, curr_target)
            return
        
        get_combinations(0, target)

        return all_combs