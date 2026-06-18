class Codec:
    def __init__(self, base_url: str = "http://tinyurl.com/"):
        self.url_map = {}
        self.id = 0
        self.base = base_url
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.id += 1
        self.url_map[self.id] = longUrl
        return str(self.id)


        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        url_id = shortUrl.split("/")[-1]
        return self.url_map[int(url_id)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))