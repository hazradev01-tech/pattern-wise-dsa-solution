class Solution(object):

  def setZeroes(self, matrix):
    """:type matrix: List[List[int]]

    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    row = [0] * m
    col = [0] * n

    # Step 1: Mark rows and columns that need to be zeroed
    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 0:
          row[i] = -1
          col[j] = -1

    # Step 2: Set elements to zero based on marks
    for i in range(m):
      for j in range(n):
        if row[i] == -1 or col[j] == -1:
          matrix[i][j] = 0