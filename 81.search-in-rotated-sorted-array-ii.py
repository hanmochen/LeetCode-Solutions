#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        low = 0
        high = len(nums) - 1
        while low <= high:
            while low < high and nums[low] == nums[high]:#这样的目的是为了能准确判断mid位置，所以算法的最坏时间复杂度为O(n)
                low += 1                  
            mid = (low+high)//2
            if target == nums[mid]:
                return True         
            elif nums[mid] >= nums[low]: #高区
                if nums[low] <= target < nums[mid]:  
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:  #低区
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
