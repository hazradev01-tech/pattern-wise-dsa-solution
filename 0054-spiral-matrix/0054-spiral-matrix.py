class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
           return[]
        result=[]
        top,left=0,0 #initialize for traversal
        bottom,right=len(matrix)-1,len(matrix[0])-1
        #travesal the matrix in a spiral order
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1
            #move top bottom along with the right coloumn
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1
            #move right to left across the bottom row(if still valid)
            if top<=bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom-=1
                #move botttom to top along the left column(if possible)
                if left<=right:
                    for i in range(bottom,top-1,-1):
                        result.append(matrix[i][left])
                    left+=1
        return result
        