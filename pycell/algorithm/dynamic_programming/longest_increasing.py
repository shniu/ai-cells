# -*- coding: utf-8 -*-


class LongestIncreasingContinuousSubsequence(object):
    """
    给定一个整数数组（下标从 0 到 n-1， n 表示整个数组的规模），请找出该数组中的最长上升连续子序列。
    （最长上升连续子序列可以定义为从右到左或从左到右的序列。）

    给定 [5, 4, 2, 1, 3], 其最长上升连续子序列（LICS）为 [5, 4, 2, 1], 返回 4.

    动态规划
      状态：f(k)表示到第k个数字的最长子序列的长度
      状态转方程  f(k) = f(k-1)+1 A[k]>A[k-1] 否则 f(k) = max(f(i)) i=1...k
    """

    def lics(self, sequence):
        def _lics(seq):
            longest_cnt, tmp = 0, 0

            for i in xrange(len(seq)):
                if seq[i] > seq[i-1] or tmp == 0:
                    tmp += 1
                    longest_cnt = max(longest_cnt, tmp)
                else:
                    tmp = 1

            return longest_cnt

        return max(_lics(sequence), _lics(sequence[::-1]))


if __name__ == '__main__':
    print LongestIncreasingContinuousSubsequence().lics([5, 4, 2, 1, 3])
