# -*- coding: utf-8 -*-


class MaxPathSum(object):

    """
    给出一棵二叉树，寻找一条路径使其路径和最大，路径可以在任一节点中开始和结束
    （路径和为两个节点之间所在路径上的节点权值之和）
    """

    def max_path_sum(self, root):
        m = [0]
        m[0] = -float("Inf")
        return self.post_order_traversal(root, m)

    @classmethod
    def post_order_traversal(cls, node, max_sum):
        if node is not None:
            cls.post_order_traversal(node.left, max_sum)
            cls.post_order_traversal(node.right, max_sum)

            # 叶子节点
            if node.left is None and node.right is None:
                pass
            elif node.left is not None:
                pass

