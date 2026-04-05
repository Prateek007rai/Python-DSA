# word search in 2D matrix
# input: matrix - [['A','B','C'], ['D','E','F'], ['G','H','I']], word - "ABE"
# output: True
# Time Complexity: O(m*n*4^k), k- length of word
# Space Complexity: O(k)

# Adjacent cells - for word search

def word_search(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])

    # This dfs function will find the word in matrix 
    def dfs(r,c,i):
        if i == len(word):
            return True
        
        # check for boundaries
        if r < 0 or c<0 or r >= rows or c >= cols:
            return False
        
        # if not present in matrix
        if matrix[r][c] != word[i]:
            return False
        
        # if present
        # store in temp and mark as '#'
        temp = matrix[r][c]
        matrix[r][c] = '#'

        # check on all side for next char of word
        found = (
            dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1) 
        )

        matrix[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True

    return False    
print(word_search([['A','B','C'], ['D','E','F'], ['G','H','I']], "ABCFEHG"))