# -*- coding: utf-8 -*-


class BackPackExt(object):

    """
    背包的扩展问题
    """

    @classmethod
    def back_pack_variant1(cls, m, A, V):
        """
        给出n个物品的体积A[i]和其价值V[i]，将他们装入一个大小为m的背包，最多能装入的总价值有多大？
        """
        objects_len = len(A)

        result = [0] * (m + 1)

        for i in xrange(0, objects_len):

            for j in xrange(m, A[i] - 1, -1):
                temp = result[j - A[i]] + V[i]
                result[j] = max(result[j], temp)

        return result[m]

    @classmethod
    def back_pack_variant2(cls, nums, target):
        """
        给出一个都是正整数的数组 nums，其中没有重复的数。从中找出所有的和为 target 的组合个数

          这是一个背包问题，状态定义：f[i] 表示所有和为i的组合个数；
          状态转移方程：f[i] = sum(f[i-nums[j]]) j=1...len(nums)且nums[j]<=i
        """
        result = [0] * (target + 1)
        result[0] = 1

        for i in xrange(1, target + 1):
            for j in xrange(0, len(nums)):
                if nums[j] <= i:
                    result[i] += result[i - nums[j]]

        print result
        return result[target]


if __name__ == "__main__":
    # print Solution().back_pack(100, [77, 22, 29, 50, 99], [92, 22, 87, 46, 90])
    print BackPackExt.back_pack_variant2([4, 1, 2, 8, 11], 10)

