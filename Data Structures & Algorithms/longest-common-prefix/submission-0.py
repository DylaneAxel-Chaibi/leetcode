class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str = ""
        l = [len(s) for s in strs]
        minL = min(l)
        for i in range(minL) :
            a = strs[0][i]
            for s in strs :
                if a != s[i] :
                    return str
                
            str = str + a
        return str


