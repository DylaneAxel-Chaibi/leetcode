class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs :
            a = "".join(sorted(s))
            result[a].append(s);
        return list(result.values())
