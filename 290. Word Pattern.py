class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = dict()
        if len(pattern) != len(s.split()):
            return False
        for i, j in zip(pattern, s.split()):
            if i in pattern_map:
                if pattern_map[i] != j:
                    return False
            else:
                pattern_map[i] = j
        if len(pattern_map.values()) != len(set(pattern_map.values())):
            return False
        return True




print(Solution().wordPattern("abba", "dog cat cat dog"))
print(Solution().wordPattern("aaa", "aa aa aa aa"))