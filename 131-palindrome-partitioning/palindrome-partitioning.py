class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        all_partitions = []
        curr_partition = []

        # memoized palindrome checks
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True # length 1 palindromes
            if i < n - 1:
                is_palindrome[i][i+1] = (s[i] == s[i+1]) # length 2 palindromes
        
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_palindrome[i+1][j-1]:
                    is_palindrome[i][j] = True

        def get_partitions(start_index: int) -> None:
            # reached end
            if start_index == n:
                all_partitions.append(curr_partition[:])
                return

            for i in range(start_index, n):
                if is_palindrome[start_index][i]:
                    curr_partition.append(s[start_index: i + 1])
                    get_partitions(i + 1)
                    curr_partition.pop()
            return 
        
        get_partitions(0)

        return all_partitions