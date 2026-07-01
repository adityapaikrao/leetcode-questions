class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v1 = [int(t) for t in v1]

        v2 = version2.split(".")
        v2 = [int(t) for t in v2]

        i = 0
        while i < len(v1) and i < len(v2):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i += 1
        
        # print(i,v1, v2)
        if i == len(v1) == len(v2):
            return 0
        
        while i < len(v1):
            # print("v1:",v1[i])
            if v1[i] != 0:
                return 1
            i += 1
        
        while i < len(v2):
            # print("v2:", v2[i])
            if v2[i] != 0:
                return -1
            i += 1 
        
        return 0
        