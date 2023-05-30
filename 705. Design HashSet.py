class MyHashSet:

    def __init__(self):
        self.HashSet = []

    def add(self, key: int) -> None:
        if key not in self.HashSet:
            self.HashSet.append(key)
        return self.HashSet

    def remove(self, key: int) -> None:
        if key in self.HashSet:
            self.HashSet.remove(key)
        return self.HashSet

    def contains(self, key: int) -> bool:
        if key in self.HashSet:
            return  True
        return False


obj = MyHashSet()
print(obj.add(1))
print(obj.add(2))
print(obj.contains(1))
print(obj.contains(3))
print(obj.add(2))
print(obj.contains(2))
print(obj.remove(2))
print(obj.contains(2))