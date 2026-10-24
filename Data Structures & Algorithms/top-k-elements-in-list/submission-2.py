class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    
        seen = dict()
        #So now I have a dict with key number and value its apperances
        for num in nums:
            seen[num] = seen.get(num,0) + 1

        sorted_app= sorted(seen.values(),reverse = True)
        res = set()
        for i in range(k):
            for key in seen:
                if seen[key] == sorted_app[i]:
                    res.add(key)
        
        return list(res)