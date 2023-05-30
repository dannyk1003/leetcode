class MyHashMap:

    def __init__(self):
        self.myHash = []
        

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.myHash.append([key, value])
        return self.myHash

    def get(self, key: int) -> int:
        for i in self.myHash:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in self.myHash:
            if i[0] == key:
                self.myHash.remove(i)
                break
        return self.myHash


obj = MyHashMap()
print(obj.put(1, 1))
print(obj.put(2,2))
print(obj.get(1))
print(obj.get(3))
print(obj.put(2,1))
print(obj.get(2))
print(obj.remove(2))
print(obj.get(2))