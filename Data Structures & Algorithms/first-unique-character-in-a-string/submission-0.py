class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for i in range(len(s)) :
            if s[i] not in mp :
                mp[s[i]] = i
            else :
                mp[s[i]] = len(s)
        for c in mp :
            if mp[c] != len(s) :
                return mp[c]
        return -1
        