class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        i = 0

        while i < len(words):
            curr_len = len(words[i])
            j = i + 1
            num_spaces = 0
            while j < len(words) and curr_len + num_spaces + 1 + len(words[j]) <= maxWidth:
                curr_len += len(words[j])
                num_spaces += 1
                j += 1
            
            if j == len(words) or num_spaces == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
                lines.append(line)

            else:
                spaces_len = (maxWidth - curr_len) // num_spaces
                extra_spaces = (maxWidth - curr_len) % num_spaces
                line = []
                for k in range(i, j):
                    line.append(words[k])
                    if k < j - 1:
                        line.append(" " * spaces_len)
                        if extra_spaces:
                            line.append(" ")
                            extra_spaces -= 1
                lines.append("".join(line))
            i = j
        
        return lines