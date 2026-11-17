class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        """
        cab ab -> b d

        start with single chars in lexicographic order and see if it exists in other string

        then check for length 2 substrings and check every other string
        ....
        basically check every substring in lexicographic order and see if it exists
        """
        substrings = {} # string -> sibstrings
        substring_to_string = defaultdict(set)
        for index, string in enumerate(arr):
            substrings[index] = []
            for i in range(len(string)):
                substring = ''
                for j in range(i, len(string)):
                    substring += string[j]
                    substrings[index].append(substring)
                    substring_to_string[substring].add(index)
                
            substrings[index].sort(key = lambda x : (len(x), x))
        
        # print(substrings)
        answer = []
        for index in range(len(arr)):
            found = False
            for substring in substrings[index]:
                if len(substring_to_string[substring]) == 1:
                    answer.append(substring)
                    found = True
                    break
            if not found: answer.append('')
        return answer


