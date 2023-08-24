class Solution(object):
    def lengthOfLastWord(self, s):
        word=s.split() #delimiter at whitespaces thus divides into 2 arrays
        return len(word[-1]) #cathes only last word with -1 index and gets length
        