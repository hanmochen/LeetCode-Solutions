# LeetCodeNotes

[TOC]

## 1.[Two Sum](https://leetcode.com/problems/two-sum)



### Problem Description

> Given an array of integers, return indices of the two numbers such that they add up to a specific target.
> You may assume that each input would have exactly one solution, and you may not use the same element twice.
> Example:
>
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

- `enumerate` 的使用
- `dict` 的使用

## 2.[Add Two Numbers](https://leetcode.com/problems/add-two-numbers)

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

## 3.[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

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
**Optimized Sliding Window** 
从前往后遍历，假定已知目前最大长度，和目前活动的滑动窗口，对于下一个字符，有两种情况：
- 未出现过： 加入滑动窗口中，比较窗口大小和最大长度，更新字典和最大长度
- 已经出现过：
  - 若上一次出现的位置在滑动窗口内，窗口左边界设为上一次出现的位置，当前位置加入滑动窗口，更新字典和最大长度
  - 若上一次出现的位置不在窗口中，当前位置加入滑动窗口，更新字典和最大长度

一个误区：
**滑动窗口是目前正在活动（active）的窗口，而不是目前最大长度的窗口。**

时间复杂度：$O(n)$

## 4.[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)

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

TODO： 进一步优化

## 5.[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)

### Problem Description
> Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
> Example 1:
> > Input: "babad"
> > Output: "bab"
> > Note: "aba" is also a valid answer.
> Example 2:
> > Input: "cbbd"
> > Output: "bb"

### Solution
Other's Code
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #预处理
        s1='#'+'#'.join(s)+'#'
        RL=[0]*len(s1)
        MaxRight=0
        pos=0
        MaxLen=0
        maxPos=0
        for i in range(len(s1)):
            if i<MaxRight:
                RL[i]=min(RL[2*pos-i], MaxRight-i)
            else:
                RL[i]=1
            #尝试扩展，注意处理边界
            while i-RL[i]>=0 and i+RL[i]<len(s1) and s1[i-RL[i]]==s1[i+RL[i]]:
                RL[i]+=1
            #更新MaxRight,pos
            if RL[i]+i-1>MaxRight:
                MaxRight=RL[i]+i-1
                pos=i
            #更新最长回文串的长度
            if RL[i]>MaxLen:
                MaxLen = RL[i]
                maxPos = i

        MaxLen = MaxLen - 1
        return s[int((maxPos-MaxLen)/2):int((maxPos+MaxLen)/2)]
```

My Code
```python
#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #preprocessing
        s1='#'+'#'.join(s)+'#'
        radius=[1]*len(s1)
        rightBound,centerPosition,maxLength,maxPosition=1,0,1,0

        for i in range(len(s1)):
            if(i+maxLength>len(s1)):break 
            iMirrored = 2*centerPosition - i
            if(radius[iMirrored]>=rightBound-i):
                radius[i] = rightBound-i
                while(i-radius[i]>=0 and i+radius[i]< len(s1) and s1[i+radius[i]] == s1[i-radius[i]]):
                    radius[i] += 1
                centerPosition = i
                rightBound = i + radius[i]
            else: radius[i]=radius[iMirrored]
            
            if(radius[i]>maxLength):
                maxLength = radius[i]
                maxPosition = i
        
        maxLength -= 1
        return s[int((maxPosition-maxLength)/2):int((maxPosition+maxLength)/2)]

```
### Tips

Manacher 算法
仅适用于奇回文问题('aba') 
1. 改造原字符串以适应偶回文（加入原字符串中不存在的字符如'#'）记为 S[i]
2. 辅助数组 P, P[i]表示以S[i]为中心的最长回文半径（包含中心字符）, P[i]-1 对应原字符串中最长回文长度
3. 问题：已知 P[0:i] 求 P[i]，设置辅助变量 mx: 目前遍历到的回文子串能到达的最右端的位置；id: mx 对应的回文串中心的位置 即mx=P[id]+id (S[mx]不在当前回文子串中）。根据 i 的位置，可以分为两种情况：
   1. i=mx 没有对称性可以利用，从中间向两边逐步扩展，更新 mx 和 id
   2. id<i<mx 可以利用 i_mirror = 2*id - i 和 P[i_mirror] 的值，又分为两种情况。
      -  P[i_mirror] 较小，P[[i_mirror]+i<=mx: P[i]=P[i_mirror] 
      -  P[i_mirror] 较大，P[[i_mirror]+i>mx：只能保证 P[i]>= mx-i 从mx-i 开始向两边扩展，更新 mx 和 id
    Wait! 最后一种情况和第一种可以合并为 P[[i_mirror]+i>mx 的情况
4. 时间复杂度$O(n)$ 空间复杂度 $O(n)$
  
> 一个问题：两个不同位置的回文串到达相同的 mx,选取较大的 id 还是较小的 id?
猜测：无所谓？
> 空间的改进：仅保留 id 和 mx 对应的回文子串内的P数组？
如果在这种情况下，上一个问题，自然是选取越近的 id 越好

References:
1. [Manacher's algorithm: 最长回文子串算法 - eGust - 博客园](https://www.cnblogs.com/egust/p/4580299.html)
2. [最长回文子串问题—Manacher算法 - code666 - 博客园](https://www.cnblogs.com/code666/p/7298300.html)
3. [Manacher's Algorithm 马拉车算法 - Grandyang - 博客园](https://www.cnblogs.com/grandyang/p/4475985.html)
  

## 6.[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion)

### Problem Description
> The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
>> P   A   H   N
>> A P L S I I G
>> Y   I   R
> 
> And then read line by line: "PAHNAPLSIIGYIR"
> Write the code that will take a string and make this conversion given a number of rows:
> string convert(string s, int numRows);
> 
>> Example 1:
>> Input: s = "PAYPALISHIRING", numRows = 3
>> Output: "PAHNAPLSIIGYIR"
> 
>> Example 2:
>> Input: s = "PAYPALISHIRING", numRows = 4
>> Output: "PINALSIGYAHRPI"
>> Explanation:
>> P     I    N
>> A   L S  I G
>> Y A   H R
>> P     I

### Solution
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1): return s
        period = 2*(numRows - 1)
        length = len(s)-1
        result = ""
        rounds = int (length/period)
        remains = length % period 

        for i in range(rounds+1):
            result += s[i*period]

        if(remains<numRows-1):
            for j in range(1,remains+1):
                for i in range(rounds):
                    result += s[j+i*period]
                    result += s[(i+1)*period-j]

                result += s[j+rounds*period]
            
            for j in range(remains+1,numRows-1):
                for i in range(rounds):
                    result += s[j+i*period]
                    result += s[(i+1)*period-j]
                    
            for i in range(rounds):
                result += s[numRows-1+i*period]

        else:
            for j in range(1,period-remains):
                for i in range(rounds):
                    result += s[j+i*period]
                    result += s[(i+1)*period-j]

                result += s[j+rounds*period]
            
            for j in range(period-remains,numRows-1):
                for i in range(rounds):
                    result += s[j+i*period]
                    result += s[(i+1)*period-j]  

                result += s[j+rounds*period]
                result += s[rounds*period+period-j]

            for i in range(rounds):
                result += s[numRows-1+i*period]
                
            result += s[numRows-1+rounds*period]
        return result

```

### Tips

- 以 2n-2 为周期
- 最后一个周期单独处理
  - 余数大于 n-1
  - 余数小于 n-1
- 最后一行单独处理
- 另一个思路：用特殊符号如`#`补齐到完整的周期 然后从结果中删去

## 7.[Reverse Integer](https://leetcode.com/problems/reverse-integer)

### Problem Description
> Given a 32-bit signed integer, reverse digits of an integer.
> 
>> Example 1:
>> Input: 123
>> Output: 321
> 
>> Example 2:
>> Input: -123
>> Output: -321
> 
>> Example 3:
>> Input: 120
>> Output: 21
> 
> Note:
> Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: $[−2^{31},  2^{31} − 1]$. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


### Solution
```python
class Solution:
    def reverse(self, x: int) -> int:
        flag = (x>=0)
        INT32_MAX = 2**31-1
        INT32_MIN = - 2**31
        x = abs(x)
        res = 0
        if x==0 : return res
        while(x!=0):
            res *= 10
            tmp = x %10
            res += tmp
            x = int(x/10)

        if not flag: res = -res
        if res >= INT32_MAX or res <= INT32_MIN: res = 0
        
        return res
```

### Tips

- Boring

## 8.[String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi)

### Problem Description

> Implement atoi which converts a string to an integer.

### Solution
```python
class Solution:
    def myAtoi(self, str: str) -> int:
        l = len(str)
        INT_MAX = 2**31-1
        INT_MIN = - 2**31
        if(l == 0): return 0
        
        pos = 0 
        flag = True
        res = 0
        while(pos < l and str[pos]==" "): 
            pos += 1
        
        if(pos>=l): return 0

        if(not( str[pos]=="+" or str[pos] == "-" or (str[pos]>= "0" and str[pos] <= "9"))): return 0
        
        if( str[pos]=="+" or str[pos] == "-"): 
            flag = (str[pos]== "+")
            pos += 1
        

        while (pos < l and str[pos]>="0" and str[pos] <= "9" ):
            if(res>INT_MAX or res < INT_MIN):
                if flag: return INT_MAX
                else: return INT_MIN
            
            res *= 10
            res += int(str[pos]) - int("0")
            pos += 1

        if(res>INT_MAX or res < INT_MIN):
                if flag: return INT_MAX
                else: return INT_MIN
        
        if flag: return res
        else: return -res
```

### Tips

> It's not algorithm,it's a if-else practice :(

## 9.[Palindrome Number](https://leetcode.com/problems/palindrome-number)

### Problem Description
> Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.


### Solution

```python
from math import log10 as log
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0): return False
        if(x==0): return True
        numOfDigits = int(log(x))
        rangeTen = 10**numOfDigits
        while(x>0):            
            if(x%10 !=  int(x/rangeTen)): return False
            x = int((x%rangeTen) /10)
            rangeTen /= 100
        
        return True
```

```python
def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
```

### Tips

- 刚开始考虑类似迭代的思路，每次去除最高位和最低位，但对于 10101 类型出错
- 需要引入 range /= 100，同时也不需要每次取 log

## 10.[Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching)

### Problem Description
Given an input string (`s`) and a pattern (`p`), implement regular expression matching with support for `'.'` and `'*'`.

```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```

The matching should cover the **entire** input string (not partial).

**Note:**

- `s` could be empty and contains only lowercase letters `a-z`.
- `p` could be empty and contains only lowercase letters `a-z`, and characters like `.` or `*`.

### Solution



```python
#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        
        lengthOfText,lengthOfPattern = len(text),len(pattern)
        dp = [[False]* (lengthOfPattern + 1) for _ in range(lengthOfText+1)] 
        dp[-1][-1] = True #End of Match

        for i in range(lengthOfText,-1,-1):
            for j in range(lengthOfPattern-1,-1,-1):
                if(j == lengthOfPattern-1):
                    dp[i][j] = ( (i == lengthOfText-1) and (self.isMatchOfSingleCharacter(text[i],pattern[j])) )
                else:
                    if(pattern[j+1] == '*'):
                        if(i == lengthOfText ): # End of Text
                            dp[i][j] = dp[i][j+2]
                        else:
                            dp[i][j] = (dp[i][j+2] or (self.isMatchOfSingleCharacter(text[i],pattern[j]) and dp[i+1][j]))
                    else:
                        if(i == lengthOfText): dp[i][j] = False
                        else:
                            dp[i][j] = dp[i+1][j+1] and (self.isMatchOfSingleCharacter(text[i],pattern[j]) )
                        
        return dp[0][0]
        
    def isMatchOfSingleCharacter(self,textCharacter,patternCharacter)->bool:
            return patternCharacter == '.' or patternCharacter == textCharacter
```



### Tips



最容易想到的是递归的方法

如果 `pattern` 第二位为 `*`  此时有两种情况

- 检查 `text` 和 `pattern[2:]` 是否匹配，即 `*` 使前面字符出现 0 次
- 如果 `pattern` 和 `text` 的第一位匹配，检查 `text[1:]` 和 `pattern` 是否匹配

否则： 如果 `pattern` 和 `text` 的第一位匹配，检查 `text[1:]` 和 `pattern[1:]` 是否匹配

复杂度分析：

- 显然跟 `pattern` 中 `*` 的个数有关，设长度分别为 $T,P$ ，最坏情况下有$P/2$ 个 `*`  设复杂度为$f(T,P)$

  - $P=0$ 时为 $O(1)$, $T=0$时为 $O(P)$ $P=2$ 时为 $O(T)$
  - $P$ 每增加 2: $f(T,P+2) = f(T,P)+f(T-1,P+2)$  
  - 问题转化为
    - $f(0,0)=1,f(0,n) = n ,f(m,0)= 1$
    - $f(m,n)=f(m,n-1)+f(m-1,n)$

  - $f(m,n) = \binom{n+m+1}{n}- \binom{n+m-1}{m}  = O(e^{m+n})$ 

- 复杂度为 $O(e^{T+\frac P 2})​$



**动态规划**

用 $dp[i][j]$ 记录 `text[i:]` 和 `pattern[j:]` 匹配的结果，从而避免重复的运算，从而有

- 如果 `pattern[j+1] == '*'` ,  `dp[i][j]= dp[i][j+2] ` or `dp[i+1][j] and  text[i]==pattern[j]`
- 否则 `dp[i][j]= text[i]==pattern[j] and dp[i+1][j+1]`  



**A stupid Bug**

`[[1] * m for _ in range(n)]`跟 `n*[m*[1]]` 的区别

> `n*[m*[1]]` 中先创建了一个 $m\times 1$ 的数组，然后把这个数组的引用拷贝了 n 份，因此在修改任一元素时都会改动 $n$ 份。

**References**

1. [Regular Expression Matching - LeetCode Articles](https://leetcode.com/articles/regular-expression-matching/)



## 11.[Container With Most Water](https://leetcode.com/problems/container-with-most-water)

### Problem Description

Given *n* non-negative integers *a1*, *a2*, ..., *an* , where each represents a point at coordinate (*i*, *ai*). *n* vertical lines are drawn such that the two endpoints of line *i* is at (*i*, *ai*) and (*i*, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

**Note:** You may not slant the container and *n* is at least 2.

 

![img](assets/question_11.jpg)

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

**Example:**

```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```



### Solution

```python
#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        rightBoundIndex = len(height)-1
        leftBoundIndex = 0
        maxArea = min(height[leftBoundIndex],height[rightBoundIndex])*(rightBoundIndex-leftBoundIndex)

        while leftBoundIndex < rightBoundIndex:
            if height[leftBoundIndex] < height[rightBoundIndex]:# If left is higher than right, then move the left bound
                leftBoundIndex += 1         
            else: rightBoundIndex -= 1
            
            maxArea = max(maxArea,min(height[leftBoundIndex],height[rightBoundIndex])*(rightBoundIndex-leftBoundIndex))

        return maxArea
            
```

### Tips

**Two Pointer**

- 问题在于如何更新左右边界

  - 方向：从两边开始往中间走
  - 由于宽度减少，想要面积更大，必须要增加高度
  - 如果短边不变，长边改变（无论增加还是减少），高度不会增加
  - 因此每次从较短的一边开始变化




## 12. Integer to Roman

### Problem Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as `II` in Roman numeral, just two one's added together. Twelve is written as, `XII`, which is simply `X` + `II`. The number twenty seven is written as `XXVII`, which is `XX` + `V` + `II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

**Example 1:**

```
Input: 3
Output: "III"
```

**Example 2:**

```
Input: 4
Output: "IV"
```

**Example 3:**

```
Input: 9
Output: "IX"
```

**Example 4:**

```
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

**Example 5:**

```
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```



### Solution

First Edition

```python
#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
class Solution:
    def intToRoman(self, num: int) -> str:
        romanNumber = ""
        while(num>=1000):
            num -= 1000
            romanNumber += "M"
        romanNumber += self.oneDigitIntToRoman(int(num/100),"C","D","M")
        num = num%100
        romanNumber += self.oneDigitIntToRoman(int(num/10),"X","L","C")
        num = num%10
        romanNumber += self.oneDigitIntToRoman(num,"I","V","X")
        return romanNumber
        

    def oneDigitIntToRoman(self,num:int,oneRoman:str,fiveRoman:str,tenRoman:str)->str:
        oneDigitRoman=""
        if(num in {4,9}):
            oneDigitRoman += oneRoman
            if(num>4):
                oneDigitRoman += tenRoman
            else: oneDigitRoman += fiveRoman
        else:
            if(num>4):
                oneDigitRoman += fiveRoman
                num -= 5
            while(num):
                num -= 1
                oneDigitRoman += oneRoman
        return oneDigitRoman
```



Improved a little from 52ms to 48ms

```python
#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
class Solution:
    def intToRoman(self, num: int) -> str:
        romanNumber = ""
        while(num>=1000):
            num -= 1000
            romanNumber += "M"
        romanNumber += self.oneDigitIntToRoman(num//100,"C","D","M")
        num = num%100
        romanNumber += self.oneDigitIntToRoman(num//10,"X","L","C")
        num = num%10
        romanNumber += self.oneDigitIntToRoman(num,"I","V","X")
        return romanNumber
        

    def oneDigitIntToRoman(self,num:int,oneRoman:str,fiveRoman:str,tenRoman:str)->str:

        if(num in {4,9}):
            oneDigitRoman = oneRoman
            if(num>4):
                oneDigitRoman += tenRoman
            else: oneDigitRoman += fiveRoman
        else:
            oneDigitRoman = (num//5)*fiveRoman + (num%5) * oneRoman

        return oneDigitRoman

```



A cool version

```python

class Solution:
    def intToRoman(self, num: int) -> str:
        rom = { 1000:'M', 900:'CM', 500:'D',400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL',
               10:'X', 9:'IX', 5:'V', 4: 'IV',1:'I'}
        
        output = ''
        
        for r in rom.keys():
            while r <= num:
                num -= r
                output += rom[r]
        return output
```



### Tips

- 各位数字之间独立，只是表示字母不同
- 字符串与整数的乘法运算



## 13.Roman to Integer



### Problem Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as `II` in Roman numeral, just two one's added together. Twelve is written as, `XII`, which is simply `X` + `II`. The number twenty seven is written as `XXVII`, which is `XX` + `V` + `II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

**Example 1:**

```
Input: "III"
Output: 3
```

**Example 2:**

```
Input: "IV"
Output: 4
```

**Example 3:**

```
Input: "IX"
Output: 9
```

**Example 4:**

```
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 5:**

```python
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

### Solution

```python
#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntDictionary = {'I':1, 'V':5, 'X':10, 'L':50 , 'C':100, 'D':500, 'M':1000}
        intNumber = romanToIntDictionary[s[-1]]
        for index in range(len(s)-1):
            if(romanToIntDictionary[s[index]]<romanToIntDictionary[s[index+1]]):
                intNumber -= romanToIntDictionary[s[index]]
            else: intNumber += romanToIntDictionary[s[index]]
        return intNumber
```



### Tips

- 从左往右走，若比右边一位小则减去左边一位，否则加。 **有趣的思路**



## 14. Longest Common Prefix

### Problem Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

```
Input: ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**

```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Note:**

All given inputs are in lowercase letters `a-z`.

### Solution

My first version

```python
#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(not strs):return ""
        commonPrefix = ""
        shortestLength = min([len(strs[i]) for i in range(len(strs))])
        for indexOfChar,currentChar in range(shortestLength):
            currentChar = strs[0][indexOfChar]
            for indexOfStr in range(1,len(strs)):
                if (strs[indexOfStr][indexOfChar]!= currentChar):
                    return commonPrefix
            commonPrefix += currentChar
        return commonPrefix
```

Improved & Cleaned a little

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(not strs):return ""
        commonPrefix = ""
        #shortestLength = min([len(strs[i]) for i in range(len(strs))])
        shortestString = min(strs,key=len)
        for indexOfChar,currentChar in enumerate(shortestString):
            for str in strs:
                if (str[indexOfChar]!= currentChar):
                    return commonPrefix
            commonPrefix += currentChar
        return commonPrefix
```



### Tips

- Use `min` and `enumrate`
- 特殊情况的处理：`strs = []`



## 15. 3Sum



### Problem Description

Given an array `nums` of *n* integers, are there elements *a*, *b*, *c* in `nums` such that *a* + *b* + *c* = 0? Find all unique triplets in the array which gives the sum of zero.

**Note:**

The solution set must not contain duplicate triplets.

**Example:**

```text
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```



### Solution

First Version

```python
#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(not nums): return []
        tripletSet = []
        sortedNumbers = sorted(nums)
        currentIndex = 0
        while currentIndex < len(sortedNumbers)-2 :
            currentNumber = sortedNumbers[currentIndex]
            leftBound = currentIndex + 1 
            rightBound = len(sortedNumbers)-1
            while(leftBound < rightBound):
                sum = currentNumber+sortedNumbers[leftBound]+sortedNumbers[rightBound]
                if(sum == 0):
                    tripletSet.append([currentNumber,sortedNumbers[leftBound],sortedNumbers[rightBound]])
                    while(sum==0 and leftBound<rightBound):
                        leftBound += 1
                        sum = currentNumber+sortedNumbers[leftBound]+sortedNumbers[rightBound]
                elif(sum > 0): rightBound -= 1
                else: leftBound += 1
            
            while(currentIndex<len(sortedNumbers)-2 and sortedNumbers[currentIndex]==currentNumber):
                currentIndex += 1
            

        return tripletSet   
                    
```

Add a line and greatly improved

```python
#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(not nums): return []
        tripletSet = []
        sortedNumbers = sorted(nums)
        currentIndex = 0
        while currentIndex < len(sortedNumbers)-2 :
            currentNumber = sortedNumbers[currentIndex]
            #ADD A LINE
            if(currentNumber>0): return tripletSet
            leftBound = currentIndex + 1 
            rightBound = len(sortedNumbers)-1
            while(leftBound < rightBound):
                sum = currentNumber+sortedNumbers[leftBound]+sortedNumbers[rightBound]
                if(sum == 0):
                    tripletSet.append([currentNumber,sortedNumbers[leftBound],sortedNumbers[rightBound]])
                    while(sum==0 and leftBound<rightBound):
                        leftBound += 1
                        sum = currentNumber+sortedNumbers[leftBound]+sortedNumbers[rightBound]
                elif(sum > 0): rightBound -= 1
                else: leftBound += 1
            
            while(currentIndex<len(sortedNumbers)-2 and sortedNumbers[currentIndex]==currentNumber):
                currentIndex += 1
            

        return tripletSet   
                    
```



Smarter ways of doing this

- Using `bisect`
- Using `counts`

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        counts={}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        nums=sorted(counts)
        for i,num in enumerate(nums):
            if counts[num]>=2:
                if num==0:
                    if counts[num]>=3:
                        ans.append([0,0,0])
                else:
                    if (-2*num) in nums:
                        ans.append([num,num,-2*num])
            if num<0:
                twosum=-num
                left=bisect.bisect_left(nums,(twosum-nums[-1]), i+1)
                for i in nums[left:bisect.bisect_right(nums,(twosum//2),left)]:
                    j=twosum-i
                    if j in counts and j!=i:
                        ans.append([num,i,j])
        return ans
```



### Tips

- 问题主要在`不重` `不漏`
- 算法复杂度为$O(n^2)$ 但仍有可改进的地方
  - 引入 `counts` 数组避免重复比较和移动（缺点：可能占用大量空间？）
  - 查找时可以使用二分查找，尽管在查找这一部分复杂度从$O(n)$ 降低为$O(log(n))$ 但整体复杂度仍然为$O(n^2)$
- `bisect`的使用



## 16. 3Sum Closest

### Problem Description

Given an array `nums` of *n* integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Example:**

```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```



### Solution 

```python
#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(not nums): return []
        tripletSet = []
        sortedNumbers = sorted(nums)
        currentIndex = 0
        while currentIndex < len(sortedNumbers)-2 :
            currentNumber = sortedNumbers[currentIndex]
            if(currentNumber>0): return tripletSet
            leftBound = currentIndex + 1 
            rightBound = len(sortedNumbers)-1
            while(leftBound < rightBound):
                if(sortedNumbers[leftBound]+currentNumber>0): break
                sum = currentNumber+sortedNumbers[leftBound]+sortedNumbers[rightBound]
                if(sum == 0):
                    tripletSet.append([currentNumber,sortedNumbers[leftBound],sortedNumbers[rightBound]])
                    while(sum==0 and leftBound<rightBound):
                        leftBound += 1
                        sum = currentNumber+sortedNumbers[leftBound]+sortedNumbers[rightBound]
                elif(sum > 0): rightBound -= 1
                else: leftBound += 1
            
            while(currentIndex<len(sortedNumbers)-2 and sortedNumbers[currentIndex]==currentNumber):
                currentIndex += 1
            

        return tripletSet
```



### Tips

- 相较于上一题问题变复杂了，但思路可以简化：不需要考虑重复的情况



## 17. Letter Combinations of a Phone Number

### Problem Description

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![img](assets/200px-Telephone-keypad2.svg.png)

**Example:**

```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

**Note:**

Although the above answer is in lexicographical order, your answer could be in any order you want.

### Solution

```python
#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(not digits): return []
        dicFromDigitsToLetters = {'2':['a','b','c'],
                                  '3':['d','e','f'],
                                  '4':['g','h','i'],
                                  '5':['j','k','l'],
                                  '6':['m','n','o'],
                                  '7':['p','q','r','s'],
                                  '8':['t','u','v'],
                                  '9':['w','x','y','z']}
        allLetterCombinations = dicFromDigitsToLetters[digits[0]]
        for index in range(1,len(digits)):
            allLetterCombinations = [(prefix+suffix) for (prefix,suffix) in itertools.product(allLetterCombinations,dicFromDigitsToLetters[digits[index]])]
        
        return allLetterCombinations
```



### Tips

- `itertools` 的使用
- 列表生成式



## 18. 4Sum



### Problem Description

Given an array `nums` of *n* integers and an integer `target`, are there elements *a*, *b*, *c*, and *d* in `nums` such that *a* + *b* + *c* + *d* = `target`? Find all unique quadruplets in the array which gives the sum of `target`.

**Note:**

The solution set must not contain duplicate quadruplets.

**Example:**

```
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

### Solution

```python
#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: return []
        sortedNumbers = sorted(nums)
        firstIndex = 0
        quadSet = []
        while firstIndex < len(nums) - 3:
            firstNumber = sortedNumbers[firstIndex]
            if firstNumber*4 > target: return quadSet
            secondIndex = firstIndex + 1
            while secondIndex < len(nums) - 2:
                secondNumber = sortedNumbers[secondIndex]
                if secondNumber*3 > target - firstNumber: break
                thirdIndex = secondIndex + 1
                fourthIndex = len(nums) - 1
                while(thirdIndex < fourthIndex):
                    sum = firstNumber + secondNumber + sortedNumbers[thirdIndex] + sortedNumbers[fourthIndex]
                    if (sum > target): fourthIndex -= 1
                    elif (sum < target): thirdIndex += 1
                    else: 
                        quadSet.append([firstNumber,secondNumber,sortedNumbers[thirdIndex],sortedNumbers[fourthIndex]])
                        while( thirdIndex < fourthIndex and firstNumber + secondNumber + sortedNumbers[thirdIndex] + sortedNumbers[fourthIndex] == target ):
                            thirdIndex += 1
                while(secondIndex < len(nums) - 2 and sortedNumbers[secondIndex] == secondNumber ):
                    secondIndex += 1
            while(firstIndex < len(nums)-3 and sortedNumbers[firstIndex] == firstNumber):
                firstIndex += 1

        return quadSet


```



### Tips



- 推广到 n-sum？



## 19. Remove Nth Node From End of List



### Problem Description

Given a linked list, remove the *n*-th node from the end of list and return its head.

**Example:**

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

**Note:**

Given *n* will always be valid.



### Solution 

```python
#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        currentPosition = head 
        forwardPosition = head
        for _ in range(n-1):
            # ADD JUDGEMENT
            forwardPosition = forwardPosition.next
        while(forwardPosition.next is not None):
            forwardPosition = forwardPosition.next
            lastPosition = currentPosition
            currentPosition = lastPosition.next
        
        if(currentPosition == head):
            return head.next
        else:
            lastPosition.next = currentPosition.next
            return head
```



### Tips 

- `TWO-POINTER`
- 特殊情况的处理
  - `n ` is invalid (not in this case)
  - remove the first node





## 20. Valid Parentheses



### Problem Description

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.



### Solution

```python
#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        expressionStack = []
        bracketDictionary = {"}":"{",
                             "]":"[",
                             ")":"("}
        if not s: return True
        for char in s:
            if char in bracketDictionary:
                if not expressionStack: return False
                if( bracketDictionary[char]!= expressionStack.pop()): return False
            else: expressionStack.append(char)
        
        return not expressionStack
                

```



### Tips

- `List ` 的 `pop` 方法
- 改进：可以考虑自己实现栈



```python
class Node:
    def __init__(self, data, link):
        self._data = data
        self._next = link

class Stack:
    def __init__(self):
        self._top = None
    
    def push(self, data):
        self._top = Node(data, self._top)
    
    def pop(self):
        node = self._top
        self._top = self._top._next
        return node._data
    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        bracketDict = {")":"(", "}":"{", "]":"["}
        for character in s:
            if character == "(" or character == "{" or character == "[":
                stack.push(character)
            elif character == ")" or character == "}" or character == "]":
                if stack._top is None:
                    return False
                else:
                    if stack._top._data != bracketDict[character]:
                        return False
                    else:
                        stack.pop()
        
        return stack._top is None
        
```



## 21. Merge Two Sorted Lists



### Problem Description

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

**Example:**

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```



### Solution 



```python
#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else :
            head = l2
            l2 = l2.next

        lastPosition = head
        position1 = l1
        position2 = l2
        
        while(position1 is not None and position2 is not None):
            if(position1.val < position2.val):
                lastPosition.next = position1
                position1 = position1.next
            else:
                lastPosition.next = position2
                position2 = position2.next
            lastPosition = lastPosition.next
            
        lastPosition.next = position2 if position1 is None else position1

        return head
        
```



### Tips

- 特殊情况的处理



## 22. Generate Parentheses



### Problem Description

Given *n* pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given *n* = 3, a solution set is:

```text
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```



### Solution



```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 2 : return [n*"()"]
        validSet = []
        for i in range(n):            
            validSet += ["("+str1+")"+str2 for str1 in self.generateParenthesis(i) for str2 in self.generateParenthesis(n-1-i)]
        return validSet
```



### Tips



- 最简单的想法是生成所有可能序列然后检验，复杂度$O(2^{2n}n)$ 
- 一个自然的方法是利用递归，即寻找 $S_n$ 与$S_k (k\leqslant n)$ 之间的关系， $S_n$ 为$n$ 对括号的所有有效表达式



>  **思路**：对于$S_n$, 可以看成一个路径问题，数轴上的点从原点出发，每次向左或向右移动一格，在整个过程中始终不能移动到原点左侧，$2n$ 次移动后回到原点，求所有可能路径。
>
> - 递推来源于分类。
>
> - 分类依据为第一次回到原点时间，可能为$2k,k=1,2,\cdots,n-1,n$
>
> 对于在$2k$步第一次回到原点的路径：
>
> - 后面 $2(n-k)$ 的路径由 $S_{n-k}$ 给出
> - 前面的路径呢？
>   - **不是$S_k$**  （有重复的） ，重复包含了在第 $2k$ 步之前已经回到过原点的路径
>   - 为了保证 $2k$ 步以前从未回到原点
>     - 第1步向右，第 2k 步向左
>     - 过程中始终保证与原点距离为正$(\geqslant 1)$
>     - 这也意味着把如果把第$1$ 步和$2k$ 步去掉，同时原点右移一格，所有可能的路径为 $S_{k-1}$
>
> **递推公式**
>
> $S_n= \sum\limits_{i=1}^n[$ `(` $+S_{i-1}+$ `)` $+S_{n-i}]$
>
> 



- 见到题目的第一感与卡特兰数有关



## 23. Merge k Sorted Lists



### Problem Description 

Merge *k* sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

**Example:**

```text
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```



### Solution



Using `PriorityQueue`

```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        head = point = ListNode(0)
        q = PriorityQueue()
        count = 0
        for l in lists:
            if l:
                q.put((l.val, count,l))
                count += 1
        while not q.empty():
            val,_,node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val,count,node))
                count += 1 
        return head.next
```



Using `heap`



```python
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        
        heap = []
        for node in lists:
            if node:
                heappush(heap, (node.val, id(node), node))
                
        head = current = ListNode(None) # dummy head
        
        while heap:
            node = heappop(heap)[2]
            if node.next:
                heappush(heap, (node.next.val, id(node.next), node.next))
            current.next = node
            current = node
        
        return head.next
```



### Tips

- 最简单的思路 ：k 个结点，每次找到最小的，加入，后移，复杂度$O(Nk)$ $N$ 为节点数，$k$ 为链表数 
- 改进的想法：每次找到最小值，不需要比较$k$ 次，只需比较$\log k$ 次
  - 利用堆的数据结构
  - 或者优先队列

- 需要注意的是，由于可能出现 `node.value` 相同的情况，这时会默认比较 `node` 而 `ListNode` 类并没有重载 `<` 运算符从而会报错。解决方法：每一个进入 `heap` 或 `PriorityQueue` 的 `tuple` 加入一个 `identifier` 在 `node` 之前，`identifier`可以使用 `id()` 或者 `count` 计数



**References**:

1. [queue — A synchronized queue class — Python 3.7.4 documentation](https://docs.python.org/3/library/queue.html?highlight=priority%20queue)
2. [heapq — Heap queue algorithm — Python 3.7.4 documentation](https://docs.python.org/3/library/heapq.html?highlight=priority%20queue)



## 24. Swap Nodes in Pairs



### Problem Description

Given a linked list, swap every two adjacent nodes and return its head.

You may **not** modify the values in the list's nodes, only nodes itself may be changed.

 

**Example:**

```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```



### Solution

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        position = dummy = ListNode(0)
        dummy.next = head
        while(position.next and position.next.next):
            temp = position.next
            position.next = temp.next
            temp.next = position.next.next
            position.next.next = temp
            position = position.next.next
        return dummy.next 
```



### Tips



## 25. Reverse Nodes in k-Group



### Problem Description

Given a linked list, reverse the nodes of a linked list *k* at a time and return its modified list.

*k* is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of *k* then left-out nodes in the end should remain as it is.



**Example:**

Given this linked list: `1->2->3->4->5`

For *k* = 2, you should return: `2->1->4->3->5`

For *k* = 3, you should return: `3->2->1->4->5`

**Note:**

- Only constant extra memory is allowed.
- You may not alter the values in the list's nodes, only nodes itself may be changed.



### Solution



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse_K(head: ListNode,tail: ListNode):
            previous = head.next
            point = previous.next
            head.next = tail
            previous.next = tail.next
            while(point is not tail):
                next = point.next
                point.next = previous
                previous = point
                point = next
            tail.next = previous

        if k == 1: return head
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        count = 0
        rPointer = pointer
        while(rPointer.next is not None):
            rPointer = rPointer.next
            count += 1
            if(count == k):
                count = 0
                next = pointer.next
                reverse_K(pointer,rPointer)
                rPointer = next
                pointer = rPointer
        
        return dummy.next
```





### Tips

- 先试探有没有`k` 个结点
- 每`k` 个结点做一次链表的反转



