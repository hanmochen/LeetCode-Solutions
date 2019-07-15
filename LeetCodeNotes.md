# LeetCodeNotes

[TOC]

## Problem 1 Two Sum

### Problem Description
> Given an array of integers, return indices of the two numbers such that they add up to a specific target.
> You may assume that each input would have exactly one solution, and you may not use the same element twice.
> Example:
> > Given nums = [2, 7, 11, 15], target = 9,
> > Because nums[0] + nums[1] = 2 + 7 = 9,
> > return [0, 1].

### Solution
First version
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
```

Using `enumerate`

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,item in enumerate(nums):
            target1 = target - item
            for i in range(index+1,len(nums)):
                if nums[i] == target1:
                    return [index,i]
```

Using Dict

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for index,item in enumerate(nums):
            target1 = target - item
            if found.get(target1) is not None:
                return [found.get(target1), index]
            found[item] = index
        return False       
```

### Tips

- enumerate 的使用
- dict 的使用

## Problem 2 
### Problem Description
> You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
> You may assume the two numbers do not contain any leading zero, except the number 0 itself.
> Example:

>> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
>> Output: 7 -> 0 -> 8
>> Explanation: 342 + 465 = 807.

### Solution 
First Version
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = l1
        temp = 0

        while ((l1.next is not None) or (l2.next is not None)):
            num = l1.val + l2.val + temp
            l1.val = num % 10
            temp = (num>=10)
            if(l1.next is None or l2.next is None):
                if(l1.next is None):
                    l1.next = l2.next
                    l2.next = None
                
                while(l1.next is not None):
                    l1 = l1.next
                    num = l1.val + temp
                    l1.val = num %10
                    temp = (num>=10)
                
                num = l1.val + temp
                l1.val = num % 10
                temp = (num>=10)
                if(temp == 1):
                    l1.next = l2
                    l2.val = 1

                return l
                 
            else:
                l1 = l1.next
                l2 = l2.next
                
        num = l1.val + l2.val + temp
        l1.val = num % 10
        temp = (num>=10)
        if(temp == 1):
            l1.next = l2
            l2.val = 1

        return l
```

Improved 
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = l1
        temp = 0
        while ((l1.next is not None) or (l2.next is not None) ):
            num = l1.val + l2.val + temp
            l1.val = num % 10
            temp = num//10
            if(l1.next is None): # Make Sure l1 is longer than l2
                l1.next = l2.next
                l2.next = None
            
            l1 = l1.next
            if(l2.next is None):
                l2.val = 0
            else: l2 = l2.next  
        
        num = l1.val + l2.val + temp
        l1.val = num % 10
        temp = num//10
        if temp:
            l1.next = l2
            l2.val =1
    
        return l
```

### Tips 
- 保证 l1 为较长的一个
- 利用 l1 存储，节省空间

## Problem 3 Longest Substring Without Repeating Characters

### Problem Description
> Given a string, find the length of the longest substring without repeating characters.
> Example 1:

>> Input: "abcabcbb"
>> Output: 3 
>> Explanation: The answer is "abc", with the length of 3. 

> Example 2:

>> Input: "bbbbb"
>> Output: 1
>> Explanation: The answer is "b", with the length of 1.

> Example 3:

>> Input: "pwwkew"
>> Output: 3
>> Explanation: The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence

### Solution 
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) <= 1): 
            return len(s)
        pos, maxLen = -1, 0
        dic = {}
        for ind,char in enumerate(s):
            if (char in dic) :
                if (pos <= dic[char]):
                    pos = dic[char]
            maxLen = max(maxLen,ind - pos)
            dic[char]=ind
        return maxLen
```
### Tips
- Optimized Sliding Window 

## Problem 4

### Problem Description

> There are two sorted arrays nums1 and nums2 of size m and n respectively.
> Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
> You may assume nums1 and nums2 cannot be both empty.
> Example 1:
>> nums1 = [1, 3]
>> nums2 = [2]
>> The median is 2.
> Example 2:
> nums1 = [1, 2
> nums2 = [3, 4]
>> The median is (2 + 3)/2 = 2.5


### Solution
Given Solution
```python
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = int(half_len - i)
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
```

My Solution
```python
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:

        m,n = len(A),len(B)
        if(m >n):
            A,B = B,A
            m,n = len(A),len(B)
        
        if(n==0): raise ValueError
            
        high = m
        low = 0
        i = int(m+1/2)
        j = int((m+n+1)/2)-i

        while(self.atIndex(A,i-1)>self.atIndex(B,j) or self.atIndex(B,j-1)>self.atIndex(A,i)):
            if(self.atIndex(A,i-1)>self.atIndex(B,j)):
                high = i
                i = int((high+low)/2)
                j = int((m+n+1)/2)-i
            
            else:
                low = i
                i = int((high+low+1)/2)
                j = int((m+n+1)/2)-i
            

        if((m+n)%2 == 0):
            return (max(self.atIndex(A,i-1),self.atIndex(B,j-1))+min(self.atIndex(A,i),self.atIndex(B,j)))/2.0
        return max(self.atIndex(A,i-1),self.atIndex(B,j-1))

    def atIndex(self,A:List[int],index:int)-> int:
        if(index < 0): return float("-inf")
        if(index >= len(A)): return float("inf")
        return A[index]
```
### Tips

如何寻找中位数？

> 找到一个位置，使得排序后左右两边的数个数相等。
> 思路转变：寻找数值 -> 寻找位置

位置满足的条件
1. 左右集合的数个数相等
2. 左边集合的最大值小于等于右边集合的最小值

对于两个有序的集合 A，B，原问题转化为寻找位置对$(i,j)$ 满足

1. 长度条件：$i+j = [\frac {m+n+1} 2]$ 
2. 大小条件：$max(A[i-1],B[j-1])\leqslant \min(A[i],B[j])$ 等价于 $B[j−1]\leqslant A[i], A[i−1]\leqslant B[j]$

代入条件 1， 问题转化为寻找位置$i\in\{0,1,2,\cdots,m\}$, $\text{s.t.} j = [\frac {m+n+1} 2]-i$,$B[j-1]\leqslant A[i],A[i-1]\leqslant B[j]$

由于目标连续，可以采用二分查找，时间复杂度为$O(log(m))$

特殊情况的处理：
- $ m>n $  可能出现 $j$ 为负数的情况，此时将 A,B 互换即可，同时也可以降低时间复杂度为$O(\log(\min(m,n)))$
- $i=0,m, j = 0,n$ 的情况，规定$A[-1]=B[-1] -\infty,A[m]=B[n]= \infty$ 即可

## Problem 5

### Problem Description

### Solution

### Tips


## Problem 6

### Problem Description

### Solution

### Tips


## Problem 7

### Problem Description

### Solution

### Tips

## Problem 8

### Problem Description

### Solution

### Tips

## Problem 9

### Problem Description

### Solution

### Tips


## Problem X

### Problem Description

### Solution

### Tips
