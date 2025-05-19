class Solution:
    
    # Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat):
        n = len(mat)
        
        # 🔄 Step 1: Transpose the matrix (mat[i][j] ⇄ mat[j][i])
        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        # 🔃 Step 2: Reverse har column to get anti-clockwise 90 degree rotation
        for col in range(n):
            top = 0
            bottom = n - 1
            while top < bottom:
                mat[top][col], mat[bottom][col] = mat[bottom][col], mat[top][col]
                top += 1
                bottom -= 1
        
        return mat
