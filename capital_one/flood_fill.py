def floodFill(image, sr, sc, newColor):
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return image
    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1:
                dfs(r-1, c)
            if r + 1 < R:
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < C:
                dfs(r, c + 1)

    dfs(sr, sc)
    return image

if __name__ == '__main__':

    # You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

    # To perform a flood fill:

    # Begin with the starting pixel and change its color to color.
    # Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
    # Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
    # The process stops when there are no more adjacent pixels of the original color to update.
    # Return the modified image after performing the flood fill.

    print(floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))

    # Example 1:

    # Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

    # Output: [[2,2,2],[2,2,0],[2,0,1]]

    # Explanation:

    # From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

    # Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

    # Example 2:

    # Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

    # Output: [[0,0,0],[0,0,0]]

    # Explanation: