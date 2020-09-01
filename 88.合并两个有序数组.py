#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos1, pos2 = 1,1
        while( pos1<=m and pos2<=n):
            if nums1[m-pos1] >= nums2[n-pos2]:
                nums1[m+n+1-pos1-pos2] = nums1[m-pos1]
                pos1 += 1
            else:
                nums1[m+n+1-pos1-pos2] = nums2[n-pos2]
                pos2 += 1
        if pos1 > m:
            for i in range(n+1-pos2):
                nums1[i] = nums2[i]
                
    
# @lc code=end

