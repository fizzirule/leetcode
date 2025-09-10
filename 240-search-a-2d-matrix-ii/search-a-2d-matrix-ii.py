class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        columns = len(matrix[0])

        startrow = 0
        startcol = columns - 1

        while startrow < rows and startcol >= 0:
            if (matrix[startrow][startcol] == target):
                return True
            elif (matrix[startrow][startcol] < target):
                startrow += 1
            else:
                startcol -= 1
        return False
        