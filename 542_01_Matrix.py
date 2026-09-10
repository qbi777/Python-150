#LC 542 _ 01 Matrix (sources are all the 0-cells,spread outward)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols=len(mat),len(mat[0])
        dist=[[0]*cols for _ in range(rows)]
        queue=deque()
        visited=[[False]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    queue.append((r,c,0))
                    visited[r][c]=True
       directions=[(-1,0),(1,0),(0,-1),(0,1)]
       while queue:
            r,c,d=queue.popleft()
            dist[r][c]=d
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc]:
                    visited[nr][nc]=True
                    queue.append((nr,nc,d+1))
      return dist
