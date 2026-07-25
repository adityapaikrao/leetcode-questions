class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        """
        11000101 10000010 00000001
          k
                            i   
                    
        1 1 1 1 1 1 1 0
        nbytes = 0 + 1 + 1 = 2
        """
        while i < len(data):
            # first octet that denotes the n-bytes
            k = 7
            curr = data[i]
            num_bytes = 0
            while k >= 0 and curr & (1 << k):
                num_bytes += 1
                k -= 1
            if num_bytes == 0:
                i += 1
                continue
            
            if num_bytes == 1 or num_bytes > 4 or (i + num_bytes) > len(data): 
                return False
            
            for j in range(i + 1, i + num_bytes):
                if (data[j] & 0b11000000 != 0b10000000):
                    return False
            i = i + num_bytes
        
        return True