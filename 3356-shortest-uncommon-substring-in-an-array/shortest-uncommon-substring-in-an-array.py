class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        """
        cab ab -> b d

        start with single chars in lexicographic order and see if it exists in other string

        then check for length 2 substrings and check every other string
        ....
        basically check every substring in lexicographic order and see if it exists
        """
        substring_to_string = defaultdict(set)
        for index, string in enumerate(arr): # N
            for i in range(len(string)): # L 
                substring = ''
                for j in range(i, len(string)): # L
                    substring += string[j]
                    substring_to_string[substring].add(index)
                
        # Time complexity: O(N * (L^3 + L^2 log L))
        valid = [substring for substring, index_set in substring_to_string.items() if len(index_set) == 1]
        answer = [''] * len(arr)
        count = 0
        for substring in sorted(valid, key = lambda x : (len(x), x)):
            for index in substring_to_string[substring]:
                if answer[index] == '': 
                    answer[index] = substring
                    count += 1
                    if count == len(arr):
                        return answer

        return answer


