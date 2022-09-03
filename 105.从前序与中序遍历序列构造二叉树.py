#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        rootNode = TreeNode(preorder[0])
        if len(preorder) == 1:
            return rootNode
        else:
            rootIndex = inorder.index(preorder[0])
            rootNode.left = self.buildTree(preorder[1:rootIndex+1], inorder[:rootIndex])
            rootNode.right = self.buildTree(preorder[rootIndex+1:], inorder[rootIndex+1:])
            return rootNode
# @lc code=end

