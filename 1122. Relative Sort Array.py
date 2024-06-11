class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr1_dict = {}
        other = []
        for i in arr1:
            if i in arr2:
                if i not in arr1_dict:
                    arr1_dict[i] = 1
                else:
                    arr1_dict[i] += 1
            else:
                other.append(i)
        result = []
        for i in arr2:
            if i in arr1_dict:
                result += [i] * arr1_dict[i]
        return result + sorted(other)
        