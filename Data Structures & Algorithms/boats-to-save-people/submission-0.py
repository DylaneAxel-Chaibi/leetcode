class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r :
            remain = limit - people[r]
            if people[l] <= remain :
                l += 1
            boats += 1
            r -= 1
        return boats
            
            
            