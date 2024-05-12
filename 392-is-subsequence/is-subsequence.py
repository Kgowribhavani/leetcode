class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="":
            return True
        sub=-1
        b=''
        for i in range(len(s)):
            if s[i] in t[sub+1:] and sub+1!=len(t):
                a=s[i]
                sub=t.find(a,sub+1)
                b+=a
                if len(s)==len(b) and b==s:
                    return True

        