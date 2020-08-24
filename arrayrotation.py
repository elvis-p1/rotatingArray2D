from numpy import array

# The program takes a 3 by 3 2-D Array and rotates it by n steps
# 
# e.g. [[1,2,3] 
#       [4,5,6]
#       [7,8,9]]
# 
# rotates two steps left into
#       [[3,6,9]
#        [2,5,8]
#        [1,4,7]] 

# Rotate 2-D array arr n steps in the left direction
def rotateLeft(arr, n):
    result = arr
    for h in range(n):

        temp_down1 = result[0][0] # Top left element to move down
        temp_down2 = result[1][0] # Mid left element to move down
        temp_up1 = result[2][2] # Bottom right element to move upwards
        temp_up2 = result[1][2] # Mid right element to move upwards

        for i in range(len(result)): # Iterate through array in the 2d array
            for j in range(len(result[i])): # Iterate through each array
                if i == 0: # Top array
                    if j != 2: # Shifting left one at a time
                        result[i][j] = result[i][j+1]
                    else: # The last element at the top gets the value from the lower column
                        result[i][j] = temp_up2
                if i == 1: # Middle array, the middle element is unchanged
                    if j == 0:
                        result[i][j] = temp_down1
                    elif j == 2:
                        result[i][j] = temp_up1
                if i == 2: # Bottom array
                    if j == 2:
                        pass
                    else:
                        if j == 0:
                            temp_right = result[i][j+1]
                            result[i][j+1] = result[i][j] # set the next element to this
                            result[i][j] = temp_down2 # set element to variable from above column
                        if j == 1:
                            result[i][j+1] = temp_right # Shifting right
                        
    
    return result

def printArray(arr):
    print(str(arr[0]) + "\n" + str(arr[1]) + "\n" + str(arr[2]) + "\n")

def main():
    blank_array = [["" for i in range(3)] for i in range(3)]
    flag = False # check to break 
    user_input = input("Enter 9 numbers (single digits) to be made into a 2d array ")
    for i in range(len(user_input)):
        for j in range(len(blank_array)):
            for k in range(len(blank_array[j])):
                if blank_array[j][k] == "":
                    blank_array[j][k] = int(user_input[i])
                    flag = True
                    break
            if flag:
                flag = False
                break

    user_input_rotate = int(input("Enter the number of rotations left to be done on the array "))
    
    
    print("Your starting array:")
    printArray(blank_array)
    print("Your rotated array after rotating left by {0} steps:".format(str(user_input_rotate)))
    rotated_array = rotateLeft(blank_array, user_input_rotate)
    printArray(rotated_array)

ex = array([[1,3,4],[2,2,2],[5,9,0]])

# print("Example array:")
# printArray(ex)
# out = rotateLeft(ex, 1)
# print("After one step rotation left:")
# printArray(out)

print("example: input 123456789 creates an array of\n")
printArray([[1,2,3],[4,5,6],[7,8,9]])

while True:
    main()
