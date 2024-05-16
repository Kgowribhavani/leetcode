class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        res=''
        k_res=''
        dict={}
        dup={}
        for i in range(len(s)):
            if s[i] in dict.keys():
                res+=dict[s[i]]
            else:
                dict[s[i]]=t[i]
                res+=dict[s[i]]
        for i in range(len(res)):
            if res[i] in dup.keys():
                k_res+=dup[res[i]]
            else:
                dup[res[i]]=s[i]
                k_res+=dup[res[i]]
        print(res)
        print(k_res)
        if res==t and k_res==s:
            return True
        
            