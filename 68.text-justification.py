#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
class Solution:
    def fullJustify(self, words, maxWidth):
        lines = []
        cur = []
        cur_length = 0
        for word in words:
            if len(word) + cur_length <= maxWidth:
                cur_length += len(word) + 1
                cur.append(word)
            else:
                spaces_needed = maxWidth - sum([len(w) for w in cur])
                if len(cur) == 1:
                    lines.append(cur[0]+' '*spaces_needed)
                else:
                    space_per_word = spaces_needed // (len(cur) - 1)
                    num_extra = spaces_needed % (len(cur) - 1)
                    sentence = ''
                    for j, w in enumerate(cur):
                        sentence += w
                        if j != len(cur) - 1:
                            sentence += ' ' * space_per_word
                            if num_extra > 0:
                                sentence += ' '
                                num_extra -= 1
                    lines.append(sentence)
                cur = [word]
                cur_length = len(word) + 1
        spaces_needed = maxWidth - sum([len(word) for word in cur]) - len(cur) + 1
        lines.append(' '.join(cur) + ' ' * spaces_needed)
        return lines

        

