# -*- coding: utf-8 -*-


class ClimbStairs(object):

    """
    假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

    动态规划
      最优子结构是第i步可以从第i-1和i-2直接或得，且无后效性，符合重叠子问题的定义
      状态：f(i)表示到达第i步爬楼梯的方法数
      状态转移方程：f(i) = f(i-1) + f(i-2)
    """

    def climb(self, stairs):

        result = [1, 1]

        if stairs >= 2:
            for i in xrange(2, stairs + 1):
                result.append(result[i-1] + result[i-2])

        return result[stairs]


if __name__ == '__main__':
    print ClimbStairs().climb(12)
