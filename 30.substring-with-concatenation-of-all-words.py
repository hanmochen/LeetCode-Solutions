#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not (words and s) : return []
        indices = []
        wordLength = len(words[0])
        listLength = len(words)
        wordsHashTable = [hash(word) for word in words]
        textHashTable = [hash(s[i:i+wordLength]) for i in range(len(s)-wordLength+1)]

        for i in range(len(s)-wordLength*listLength+1):
            if textHashTable[i] in wordsHashTable:
                j = i
                tempHashTable = [hash(word) for word in words]
                while j<len(textHashTable) and textHashTable[j] in tempHashTable:
                    tempHashTable.remove(textHashTable[j])
                    j += wordLength
                if not tempHashTable: indices.append(i)
        
        return indices

