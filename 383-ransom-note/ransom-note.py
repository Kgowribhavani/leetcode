class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap={}
        for i in magazine:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for i in ransomNote:
            if i in hashmap and hashmap[i]==1:
                del hashmap[i]
            elif i in hashmap:
                hashmap[i]-=1
            else:
                return False
        return True
