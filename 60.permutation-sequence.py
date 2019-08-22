#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1]*(n-1)
        for i in range(n-2):
            factorials[i+1]=factorials[i]*(i+2)
        charSet = [str(i) for i in range(1,n+1)]
        k -= 1
        res=''
        while(k!=0):
            factorial = factorials.pop()
            res += charSet.pop( k // factorial)
            k %= factorial
        for char in charSet:
            res += char
        return res
