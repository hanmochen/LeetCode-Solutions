#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        else:
            rootNode = TreeNode(postorder[-1])
            rootIndex = inorder.index(postorder[-1])
            rootNode.left = self.buildTree(inorder[:rootIndex], postorder[:rootIndex])
            rootNode.right = self.buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
            return rootNode
# @lc code=end

