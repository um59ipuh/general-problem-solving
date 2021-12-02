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
            for j in range(i + 1, length):
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

    """
        @param Gene1: a string
        @param Gene2: a string
        @return: return the similarity of two gene fragments
    """

    def GeneSimilarity(self, Gene1: str, Gene2: str) -> str:
        # write your code here

        if len(Gene1) == 0 or len(Gene2) == 0:
            return "0/0"

        length = len(Gene1)
        amions = "ACGT"

        g1_c_i = g2_c_i = 0
        total_o = equ_c = 0

        s = e = 0
        while s < length and e < length:
            if Gene1[e] not in amions:
                e += 1
            else:
                total_o += int(Gene1[s: e])
                e += 1
                s = e

        g1_d_v = g2_d_v = None;
        g1_c_v = g2_c_v = None

        while g1_c_i < length and g2_c_i < length:
            g1_s_i = g1_c_i
            g1_e_i = None
            if g1_d_v is None and g1_c_v is None:
                while Gene1[g1_c_i] not in amions:
                    g1_c_i += 1
                g1_e_i = g1_c_i
                g1_d_v = int(Gene1[g1_s_i: g1_e_i])
                g1_c_v = Gene1[g1_e_i]
            else:
                g1_s_i = g1_c_i
                g1_e_i = g1_s_i + len(str(g1_d_v)) + 1

            g2_s_i = g2_c_i;
            g2_e_i = None
            if g2_d_v is None and g2_c_v is None:
                while Gene2[g2_c_i] not in amions:
                    g2_c_i += 1
                g2_e_i = g2_c_i
                g2_d_v = int(Gene2[g2_s_i: g2_e_i])
                g2_c_v = Gene2[g2_e_i]
            else:
                g2_s_i = g2_c_i
                g2_e_i = g2_s_i + len(str(g2_d_v))

            if g1_c_v == g2_c_v:
                min_d = min(int(g1_d_v), int(g2_d_v))
                equ_c += min_d
                g1_d_v -= min_d
                g2_d_v -= min_d

                if g1_d_v == 0:
                    g1_c_i += 1
                    g1_d_v = g1_c_v = None

                if g2_d_v == 0:
                    g2_c_i += 1
                    g2_d_v = g2_c_v = None
            else:
                g1_c_i = g1_e_i + 1
                g2_c_i = g2_e_i + 1

        return "{}/{}".format(equ_c, total_o)


if __name__ == '__main__':
    sol = Solution()
    # res = sol.twoSum([1,2,7,8,11,15], 4)
    # print(res)

    Gene1 = "60T30A40T20A40G10C"  # "3T2G4A1C"
    Gene2 = "30T60A20G30T30G30C"
    res = sol.GeneSimilarity(Gene1, Gene2)
    print(res)
