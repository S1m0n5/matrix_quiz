# Matrix quiz
# Really basic script that generates a matrix of the required size
# and asks the user to solve the determinant

#PS: Developed to run on CASIO-CG50

#Set this value to 1 for using on MicroPython version
RUNNING_ON_MICROPY = 1

from random import randint

def generate_mat(dim, max=3):
    #generate a random matrix 
    randint(-max, max)
    matrix = [[randint(-max, max) for x in range(dim)] for y in range(dim)]
    return matrix

def is_square(m): 
    #returns True if the matrix is square
    return all (len (row) == len (m) for row in m)

def take_det(mat):
    #returns the determinant of a matrix

    if any (len (row) != len (mat) for row in mat): 
        return None
    det=0

    if len(mat) == 1:
        det = mat[0][0]
    else:
        for n in range(len(mat)):
            det += (-1)**((n+1)+1) * mat[0][n] * take_det(reduced(mat, 0, n))
    return det

def reduced(mat, r, c):
    #returns the reduced matrix

    mat_rid = mat.copy()
    mat_rid.pop(r)
    mat_rid = [[mat_rid[x][y] for y in range(len(mat_rid[x])) if y!= c] for x in range(len(mat_rid))]
    return mat_rid

def pprint(mat):
    #Prettify printing
    for r in mat:
        print(str(r))


if __name__ == '__main__' or RUNNING_ON_MICROPY: #for casio-cg50 
    dim = int(input("Dim: "))

    correct_count = 0

    while True:

        r_mat = generate_mat(dim)
        correct_flag = False
        determinant = str(take_det(r_mat))

        while not correct_flag:
            print("\n")
            pprint(r_mat)
            answr = input("Det?: ((E)xit, (R)esult) ")

            if answr == determinant:
                correct_flag = True
                print("Correct")
                correct_count += 1
                break
                
            elif answr.upper() == 'R':
                print("Det: {}". format(determinant))
                break

            elif answr.isalpha():
                print("Solved correctly: {}".format(correct_count))
                quit()
            
            
            else:
                print("Try again")
                correct_flag = False

