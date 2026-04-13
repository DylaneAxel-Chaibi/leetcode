class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums :
            hashmap[num] += 1
        return max(hashmap, key=hashmap.get)
