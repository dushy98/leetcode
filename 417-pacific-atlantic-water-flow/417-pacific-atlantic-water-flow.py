class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def pac(i,j):
            if rp[i][j]:
                return True
            k=False
            h=heights[i][j]
            heights[i][j]=100001
            if heights[i-1][j]<=h:
                k=k or pac(i-1,j)
                
            if heights[i][j-1]<=h:
                k=k or pac(i,j-1)
                
            if i<m-1 and heights[i+1][j]<=h:
                k=k or pac(i+1,j)
                
            if j<n-1 and heights[i][j+1]<=h:
                k=k or pac(i,j+1)
                
            heights[i][j]=h
            rp[i][j]=k
            return k
        
        def ant(i,j):
            if ra[i][j]:
                return True
            k=False
            h=heights[i][j]
            heights[i][j]=100001
            if i>0 and heights[i-1][j]<=h:
                k=k or ant(i-1,j)
                
            if j>0 and heights[i][j-1]<=h:
                k=k or ant(i,j-1)
                
            if heights[i+1][j]<=h:
                k=k or ant(i+1,j)
                
            if heights[i][j+1]<=h:
                k=k or ant(i,j+1)
                
            heights[i][j]=h
            ra[i][j]=k
            return k
        
        m=len(heights)
        n=len(heights[0])
        rp=[[False for i in range(n)] for j in range(m)]
        ra=[[False for i in range(n)] for j in range(m)]
        
        for i in range(m):
            rp[i][0]=True
            ra[i][-1]=True
        for i in range(n):
            rp[0][i]=True
            ra[-1][i]=True
        
        for i in range(m):
            for j in range(n):
                pac(i,j)
                ant(i,j)
        res=[]
        for i in range(m):
            for j in range(n):
                if rp[i][j] and ra[i][j]:
                    res.append([i,j])
        return res        