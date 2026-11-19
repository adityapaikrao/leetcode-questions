class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        """
        This is an example of text justification
        i
                j

        curr_len = words[i]
        space = 0
        while curr_len + spaces + 1 + words[j] < maxWidth:
            - add to curr words: curr_words = [This, is, an]
            - len += word 
            - space += 1 
        
        normal line i.e j != len(words):
            space_len = (max_width - curr_len) // space
            extra_space = (max_width - curr_len) % space
            for each word:
                line += word
                if not last word:
                    line += " " * space_len
                    if extra_space:
                        line += " "
                        extra_space -= 1
        last_line:
            line = " ".join(words)
            line += " " * (max_width - curr_len)

        maxwidth = 16

        - spaces = maxwidth - chars = 16 - 8 = 8
        - each space = 4 chars long
        example
        """
        i = 0
        lines = []
        while i < len(words):
            curr_len = len(words[i])
            j = i + 1
            curr_space = 0
            while j < len(words) and curr_len + curr_space + 1 + len(words[j]) <= maxWidth:
                curr_len += len(words[j])
                curr_space += 1
                j += 1
            
            line = ""
            if j != len(words) and curr_space > 0:
                space_len = (maxWidth - curr_len) // curr_space
                extra_space = (maxWidth - curr_len) % curr_space
                for k in range(i, j):
                    line += words[k]
                    if k < j - 1:
                        line += " " * space_len
                        if extra_space:
                            line += " "
                            extra_space -= 1
            else:
                line = " ".join(words[k] for k in range(i, j))
                extra_space = maxWidth - curr_len - curr_space
                line += " " * extra_space

            lines.append(line)
            i = j
        return lines
                    
