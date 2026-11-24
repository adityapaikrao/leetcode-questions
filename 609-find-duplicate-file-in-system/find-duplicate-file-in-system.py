class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        """
        - build content -> path map
        - return groups of duplicate files
        """
        def parse_content(files: list[str]) -> str:
            file_contents = [] # (file, content)
            for file_name in files:
                idx = file_name.find("(")
                file_contents.append([file_name[:idx], file_name[idx + 1: -1]])
            return file_contents

        content_map = defaultdict(set) # content -> set(file)
        for path in paths:
            direc = path.split()
            file_contents = parse_content(direc[1:])
            for content in file_contents:
                content_map[content[1]].add(direc[0] + f'/{content[0]}')
        
        dup_files = []
        for content in content_map:
            if len(content_map[content]) > 1:
                dup_files.append(list(content_map[content]))
        return dup_files