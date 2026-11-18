# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        candidates = words[:]
        def get_similarity(a: str, b: str) -> int:
            return sum(1 for x, y in zip(a, b) if x == y)

        while True:
            best_guess = ''
            best_bucket = float('inf')

            for guess in candidates:
                buckets = defaultdict(int)
                for word in candidates:
                    buckets[get_similarity(guess, word)] += 1

                worst_bucket = max(buckets.values())
                if worst_bucket < best_bucket:
                    best_bucket = worst_bucket
                    best_guess = guess
            
            matches = master.guess(best_guess)
            if matches == 6: 
                return 
            
            candidates = [word for word in candidates if get_similarity(best_guess, word) == matches]



            