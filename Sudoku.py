grid=[ [4,1,6,0,0,0,7,5,0],
       [9,3,0,0,0,0,1,2,6],
       [0,0,0,5,6,1,3,0,4],
       [0,4,0,2,0,0,0,3,0],
       [2,7,3,0,5,6,4,8,1],
       [8,5,1,4,3,0,0,6,2],
       [5,8,4,1,2,3,6,0,9],
       [0,0,0,0,7,5,8,4,3],
       [0,6,0,0,4,9,0,1,0]  
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


# final print the grid 

def printSolution (grid) :
   for i in grid:
      for j in i:
        print(j,end=" ")
      print("\n") 
      
      
# Backtraking

def Sudouko (grid,arrR,arrC,indx):
    printSolution(grid)
    print("\n")
    if indx==len(arrR) :
        return True
    r=arrR[indx]
    c=arrC[indx]
    i=1
    while i<=9 :
        if validRow(grid,r,i) and validColumn (grid,c,i)  :
            grid[r][c]=i
            if Sudouko(grid, arrR, arrC, indx+1):
                return True
        i+=1
        print (i)
    return False 


       
print(Sudouko(grid, emptyCeilR, emptyCeilC, 0))       
        

    
    
    
    
        
       