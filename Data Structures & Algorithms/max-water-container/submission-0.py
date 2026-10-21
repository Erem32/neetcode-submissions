class Solution:
    def maxArea(self, heights: List[int]) -> int:
        end = len(heights) -1
        start = 0
        maxV = 0
        while end != start:
            
            V = (end-start) * min(heights[start],heights[end])
            if heights[start]>heights[end]:
                end-=1
            else:
                start+=1
                
            #Calculating current Volume
            #Picking maximum volume between current and local
            maxV = max(maxV,V)
        
        return maxV