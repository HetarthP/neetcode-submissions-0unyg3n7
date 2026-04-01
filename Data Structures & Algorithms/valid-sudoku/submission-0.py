class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        #Validate rows

        for i in range(9):
            s=set()
            for j in range(9):
                check= board[i][j]
                if check in s:
                    return False 
                elif check != '.':
                    s.add(check) 

        
        #Validate columns 

        for i in range(9):
            s=set()
            for j in range(9):
                check= board[j][i]
                if check in s:
                    return False 
                elif check != '.':
                    s.add(check)
        

        #Validate boxes 


        for i in range(0,9,3):
            for j in range (0,9,3):
                s=set()
                for row in range(i, i+3):
                    for column in range(j,j+3):
                        check= board[row][column]
                        if check in s:
                            return False
                        elif check !='.':
                            s.add(check)


        return True