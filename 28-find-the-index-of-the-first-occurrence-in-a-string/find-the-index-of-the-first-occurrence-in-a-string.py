class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l=len(needle)
        for i in range(len(haystack)):
            if needle[0]==haystack[i]:
                if needle==haystack[i:l+i]:
                    return i
        return -1        