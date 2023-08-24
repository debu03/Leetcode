class Solution(object):
    def longestCommonPrefix(self, str):
        if len(str) == 0:
            return ""

        word1 = str[0]
        for i in range(len(word1)):
            for word2 in str[1:]:
                if i == len(word2) or word2[i] != word1[i]:
                    return word1[0:i]

        return word1
  