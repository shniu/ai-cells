# -*- coding: utf-8 -*-


class BackPack(object):
    """
    背包问题

    在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]
    样例
        如果有4个物品[2, 3, 5, 7]

        如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。

        如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。

        函数需要返回最多能装满的空间大小。
    """

    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def back_pack(self, m, A):

        object_len = len(A)

        maxmium_capacity = [[0 for j in xrange(0, m)] for i in xrange(0, object_len)]

        for j in xrange(0, m):
            if A[0] <= j + 1:
                maxmium_capacity[0][j] = A[0]

        for i in xrange(1, object_len):

            for j in xrange(0, m):

                weight_i = A[i]
                if j + 1 >= weight_i:
                    put_in_weight = maxmium_capacity[i - 1][j - weight_i] + weight_i
                    if put_in_weight <= m:
                        maxmium_capacity[i][j] = max(maxmium_capacity[i - 1][j],
                                                     maxmium_capacity[i - 1][j - weight_i] + weight_i)
                        continue

                maxmium_capacity[i][j] = maxmium_capacity[i - 1][j]

        return maxmium_capacity[object_len - 1][m - 1]

    def back_pack_opt1(self, m, A):
        """ 优化空间，使用更少的空间 """

        object_len = len(A)

        maxmium_capacity = [[0 for j in xrange(0, m + 1)] for i in xrange(0, 2)]

        for j in xrange(0, m + 1):
            if A[0] <= j + 1:
                maxmium_capacity[0][j] = A[0]

        for i in xrange(1, object_len):

            for j in xrange(0, m + 1):

                weight_i = A[i]
                if j >= weight_i:
                    put_in_weight = maxmium_capacity[0][j - weight_i] + weight_i
                    if put_in_weight <= j:
                        maxmium_capacity[1][j] = max(maxmium_capacity[0][j], put_in_weight)
                        continue

                maxmium_capacity[1][j] = maxmium_capacity[0][j]

            maxmium_capacity[0] = [i for i in maxmium_capacity[1]]

        return maxmium_capacity[1][m]

    def back_pack_opt2(self, m, A):
        """ 同时优化空间和时间复杂度 """
        object_len = len(A)
        result = [0] * (m + 1)

        for i in xrange(0, object_len):
            for j in xrange(m, A[i] - 1, -1):
                temp = result[j - A[i]] + A[i]
                result[j] = max(result[j], temp)

        return result[m]


if __name__ == "__main__":
    import time

    start = time.time()
    # print BackPack().backPack(5000, [828,125,740,724,983,321,773,678,841,842,875,377,674,144,340,467,625,916,463,922,255,662,692,123,778,766,254,559,480,483,904,60,305,966,872,935,626,691,832,998,508,657,215,162,858,179,869,674,452,158,520,138,847,452,764,995,600,568,92,496,533,404,186,345,304,420,181,73,547,281,374,376,454,438,553,929,140,298,451,674,91,531,685,862,446,262,477,573,627,624,814,103,294,388])
    # print BackPack().back_pack_opt1(5000, [828,125,740,724,983,321,773,678,841,842,875,377,674,144,340,467,625,916,463,922,255,662,692,123,778,766,254,559,480,483,904,60,305,966,872,935,626,691,832,998,508,657,215,162,858,179,869,674,452,158,520,138,847,452,764,995,600,568,92,496,533,404,186,345,304,420,181,73,547,281,374,376,454,438,553,929,140,298,451,674,91,531,685,862,446,262,477,573,627,624,814,103,294,388])
    print BackPack().back_pack_opt1(80000,
                                    [81, 112, 609, 341, 164, 601, 97, 709, 944, 828, 627, 730, 460, 523, 643, 901, 602,
                                     508, 401, 442, 738, 443, 555, 471, 97, 644, 184, 964, 418, 492, 920, 897, 99, 711,
                                     916, 178, 189, 202, 72, 692, 86, 716, 588, 297, 512, 605, 209, 100, 107, 938, 246,
                                     251, 921, 767, 825, 133, 465, 224, 807, 455, 179, 436, 201, 842, 325, 694, 132,
                                     891, 973, 107, 284, 203, 272, 538, 137, 248, 329, 234, 175, 108, 745, 708, 453,
                                     101, 823, 937, 639, 485, 524, 660, 873, 367, 153, 191, 756, 162, 50, 267, 166, 996,
                                     552, 675, 383, 615, 985, 339, 868, 393, 178, 932])
    middle = time.time()
    print middle - start
    print BackPack().back_pack_opt2(80000,
                                    [81, 112, 609, 341, 164, 601, 97, 709, 944, 828, 627, 730, 460, 523, 643, 901, 602,
                                     508, 401, 442, 738, 443, 555, 471, 97, 644, 184, 964, 418, 492, 920, 897, 99, 711,
                                     916, 178, 189, 202, 72, 692, 86, 716, 588, 297, 512, 605, 209, 100, 107, 938, 246,
                                     251, 921, 767, 825, 133, 465, 224, 807, 455, 179, 436, 201, 842, 325, 694, 132,
                                     891, 973, 107, 284, 203, 272, 538, 137, 248, 329, 234, 175, 108, 745, 708, 453,
                                     101, 823, 937, 639, 485, 524, 660, 873, 367, 153, 191, 756, 162, 50, 267, 166, 996,
                                     552, 675, 383, 615, 985, 339, 868, 393, 178, 932])
    end = time.time()
    print end - middle
