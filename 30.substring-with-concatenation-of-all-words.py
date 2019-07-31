#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not (words and s): return []
        wordLength = len(words[0])
        listLength = len(words)

        # building dictionary for word count
        wordCountDictionary = {}
        for word in words:
            if word in wordCountDictionary:
                wordCountDictionary[word] += 1
            else:
                wordCountDictionary[word] = 1
        
        ans = []
        
        for firstIndex in range(wordLength):
            left = firstIndex
            substringDictionary = {}
            count = listLength
            for j in range(firstIndex, len(s)-wordLength+1, wordLength):
                tempWord = s[j:j+wordLength]
                if tempWord in wordCountDictionary:
                    if tempWord in substringDictionary:
                        substringDictionary[tempWord] += 1
                        while substringDictionary[tempWord] > wordCountDictionary[tempWord]:
                            substringDictionary[s[left:left+wordLength]] -= 1
                            left += wordLength
                            count += 1
                    else:
                        substringDictionary[tempWord] = 1
                    count -= 1
                    
                    if not count: ans.append(left)
                else:
                    left = j + wordLength
                    substringDictionary = {}
                    count = listLength

        return ans

