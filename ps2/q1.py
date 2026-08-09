class Cache:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Cache, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.data = {}
       
 
def main():
    for i in range(5):
        cache = Cache()
        cache.data[i] = f"Value {i}"
        print(f"Cache instance ID: {id(cache)}")
        print(f"Cache data: {cache.data}")
        
main()