class Solution:
   

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        oc = image[sr][sc]
        visited = set()
        
        def fill(image, r,c):
            if not (0<=r<n and 0<=c<m and (r,c) not in visited and image[r][c] == oc):
                return image
            
            visited.add((r,c))
            image[r][c] = newColor
            
            options = [(1,0), (0,1), (-1,0), (0,-1)]
            for option in options:
                image = fill(image,r+option[0], c+option[1])
            return image
        
        return fill(image,sr, sc)
        
        
        

            