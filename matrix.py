import random

def addition(matrix_1, matrix_2):
    print("Sum")

    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        return "NA"
    #assuming that they are the same size
    new_matrix = []
    rows = len(matrix_1) #breadth
    columns = len(matrix_1[0]) #depth
    new_matrix = init_array(new_matrix, rows, columns) #array has random numbers   
    
    for y in range(columns):
        for x in range(rows):
            new_matrix[x][y] = matrix_1[x][y] + matrix_2[x][y]

    return new_matrix
    

def multiply(matrix_1, matrix_2): #for row in matrix_1 dot with matrix_2
    print("Multiply")

    if len(matrix_1) != len(matrix_2[0]):
        return "NA"
    
    new_matrix = []
    new_matrix = init_array(new_matrix, len(matrix_1[0]), len(matrix_2))

    #index of matrix_1 is the x coordinate
    #index of matrix_2 is the y coordinate

    for x in range(len(matrix_1[0])):
        row = getRow(matrix_1, x)
        for y in range(len(matrix_2)):
            column = matrix_2[y]
            total = 0
            for i in range(len(row)):
                total += row[i]*column[i]
            new_matrix[x][y] = total

    return new_matrix


def getRow(A, index):
    row = []
    for column in A:
        row.append(column[index])
    return row

def getColumn(A, index):
    return A[index]

def printMatrix(A):
    longest = ''
    
    for y in range(len(A[0])): 
        for x in range(len(A)):
            if len(str(A[x][y])) > len(longest):
                longest = str(A[x][y])
            
    for y in range(len(A[0])): 
        for x in range(len(A)):
            digit = ''
            spaces = len(longest) - len(str(A[x][y]))
            digit += ' '*spaces + str(A[x][y])
            print (digit, end=' ')
        print()

def init_array(A, rows, columns):
    for i in range(rows): #length of x (breadth)
        A.append([]) #we are appending columns vertically
    
    for row in A:
        for i in range(columns):
            #row.append(random.randint(0,rows*columns))
            row.append(random.randint(0,100))
            
            
    #print row by row
    

    return A #returns the array

matrix_1 = []

matrix_2 = []



#initialising array

print("Matrix 1")
rows_1 = input("Enter m:")
columns_1 = input("Enter n:")

proceed = True

if rows_1 == "-1" or columns_1 == "-1":
    proceed = False
    print("Bye!")
   
        
if proceed:        
    print("Matrix 2")
    while True:
        rows_2 = input("Enter m:")
        if (rows_2 != rows_1 and rows_2 != columns_1) or rows_2.isdigit() is False:
            print("Cannot! Try Again!")
        else:
            break
    
    while True:
        
        columns_2 = input("Enter n:")
        if (columns_2 != rows_1 and columns_2 != columns_1) or columns_2.isdigit() is False:
            print("Cannot! Try again!")
        else:
            break
    print()
                       
    # initialision
    print("Matrix 1:")
    printMatrix(init_array(matrix_1, int(rows_1), int(columns_1)))
    
    
    print("Matrix 2:")
    printMatrix(init_array(matrix_2, int(rows_2), int(columns_2)))
    
    
    printMatrix(addition(matrix_1, matrix_2))
    printMatrix(multiply(matrix_1, matrix_2))
