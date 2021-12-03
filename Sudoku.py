grid=[ [8, 0, 0, 0, 5, 4, 0, 0, 1],
       [2, 0, 0, 0, 7, 0, 0, 6, 0],
       [3, 1, 7, 0, 0, 0, 0, 5, 0],
       [1, 0, 0, 0, 0, 2, 7, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 3, 9, 0, 0, 0, 0, 2],
       [0, 2, 0, 0, 0, 0, 3, 8, 9],
       [0, 3, 0, 0, 8, 0, 0, 0, 6],
       [5, 0, 0, 2, 9, 0, 0, 0, 7]
]

# (0,3) (0,4) (0,5) (0,7) (1,2) (1,3)......
# emptyCeilR=[0,0,0,0,1,1......]
# emptyCeilC=[3,4,5,7,2,3......]

emptyCeilR=[]
emptyCeilC=[]
i=0
while i<9:
  j=0
  while j<9:
     if grid[i][j]==0:
        emptyCeilR.append(i)
        emptyCeilC.append(j)
     j+=1
  i+=1


def validRow (grid,r,num):
    j=0
    while j<9:
        if grid[r][j]==num: return False
        j+=1
    return True


def validColumn (grid,c,num):
    j=0
    while j<9:
        if grid[j][c]==num: return False
        j+=1
    return True


def validBox(grid,r,c,num):
    r=r-r%3
    c=c-c%3
    i=r
    while i<=r+2:
        j=c
        while j<=c+2:
            if grid[i][j]==num: return False
            j+=1
        i+=1
    return True


# final print the grid 

def printSolution (grid) :
   for i in grid:
      for j in i:
        print(j,end=" ")
      print("\n") 
      
      
# Backtraking

def Sudouko (grid,arrR,arrC,indx):    
    
    if indx==len(arrR) :
        printSolution(grid)
        return True
    r=arrR[indx]
    c=arrC[indx]
    i=1
    while i<=9 :
        if validRow(grid,r,i) and validColumn(grid,c,i) and validBox(grid,r,c,i):
            grid[r][c]=i
            if Sudouko(grid, arrR, arrC, indx+1):
                return True
            else: grid[r][c]=0
        i+=1
    return False 

       
print(Sudouko(grid, emptyCeilR, emptyCeilC, 0))       

    
    
    
    
        
       