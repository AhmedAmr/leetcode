class Solution:
    def is_valid(self, image, r,c, fillColor):
            return 0<=r<self.n and 0<=c<self.m and image[r][c] == fillColor and not self.visited[r][c]

    def fill(self, image, sr, sc, newColor, fillColor):
            options = [(0,1), (1,0),(-1,0),(0,-1)]
        
            # fill the node where at
            if self.is_valid(image, sr,sc, fillColor):
                image[sr][sc] = newColor
                self.visited[sr][sc] = True
            else:
                return image 

            for option in options:
                image = self.fill(image, sr+option[0], sc+option[1], newColor, fillColor)
            return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.n = len(image)
        self.m = len(image[0])
        self.visited = [[False for _ in range(self.m)] for _ in range(self.n)]
        fillColor = image[sr][sc]
        
        return self.fill(image, sr, sc, newColor,fillColor)
        
        
        
        

            