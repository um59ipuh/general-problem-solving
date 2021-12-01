import sys

class Solution:

    def __init__(self):
        pass

    # -------------------------- 56 · Two Sum --------------------------------------------------------------
    # brute force two sum S(T) = O(n^2), S(s) = O(n)
    def BTtwoSum(self, numbers, target):
        # write your code here
        result = [-1, -1]
        length = len(numbers)
        for i in range(length - 1):
            for j in range(i+1, length):
                # print("i : {}, j : {}".format(i, j))
                if (numbers[i] + numbers[j]) == target:
                    result = [i, j]
        return result

    def twoSum(self, numbers, target):
        length = len(numbers)
        result = [-1, -1]
        mapper = {}
        # map all nums with index
        for i in range(length):
            item = numbers[i]
            if item in mapper:
                mapper[item].append(i)
            else:
                mapper[item] = [i]

        # traverse the mapper with target value
        for key, value in mapper.items():
            target_value = target - key
            first_index = value[0]
            if target_value in mapper:
                target_index_len = len(mapper[target_value])
                second_index = mapper[target_value][0]
                if target_index_len > 1:
                    second_index = mapper[target_value][1]
                    return sorted([first_index, second_index])
                elif target_index_len == 1 and first_index is not second_index:
                    return sorted([first_index, second_index])
                else:
                    return [-1, -1]
        return result

    # -------------------------- 56 · Two Sum --------------------------------------------------------------


if __name__ == '__main__':
    sol = Solution()
    res = sol.twoSum([1,2,7,8,11,15], 4)
    print(res)
