****# LeetCodeNotes

## Problem 1 Two Sum
> Given an array of integers, return indices of the two numbers such that they add up to a specific target.
> You may assume that each input would have exactly one solution, and you may not use the same element twice.
> Example:
> > Given nums = [2, 7, 11, 15], target = 9,
> > Because nums[0] + nums[1] = 2 + 7 = 9,
> > return [0, 1].


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


Tips:
- enumerate 的使用
- dict 的使用

## Problem 2 
> You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
> You may assume the two numbers do not contain any leading zero, except the number 0 itself.
> Example:

>> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
>> Output: 7 -> 0 -> 8
>> Explanation: 342 + 465 = 807.

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

Tips: 
- 保证 l1 为较长的一个
- 利用 l1 存储，节省空间

## Problem 3 Longest Substring Without Repeating Characters

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

