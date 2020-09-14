#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack,res = [root],[]
        while(stack):
            if stack[-1].left:
                stack.append(stack[-1].left)
            else:
                res.append(stack[-1].val)
                pos = stack.pop()
                if stack: stack[-1].left = None
                if pos.right: stack.append(pos.right)
        return res        
# @lc code=end

