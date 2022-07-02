from numpy import *
from numpy.linalg import inv, det


def alpha_num(string):  # turns stream of string characters into a list
    current_list = []
    main_list = []
    string = string.lower()
    if len(string) % 3 != 0:
        for i in range(3 - (len(string) % 3)):
            string = string + ' '
    for char in string:
        if char == ' ':
            current_list.append(26)
        else:
            current_list.append(ord(char) - 97)
        if len(current_list) == 3:
            main_list.append(current_list)
            current_list = []
    return main_list


def num_alpha(list):    # turns components of a list into a stream of string characters
    text = ''
    for i in list:
        for j in i:
            if j == 26:
                text = text + ' '
            else:
                text = text + chr(j + 97)
    return text


def encrypt(list, key): # takes components of a list and turns them into a encrypted list
    key = matrix(key)
    encrypted_list = []
    for i in list:
        i = matrix(i)
        multi = i * key
        multi = multi.tolist()[0]
        for j in range(len(multi)):
            multi[j] = multi[j] % 27
        encrypted_list.append(multi)
    return encrypted_list


def decyrption(list, key):  # takes components of a list and turns them into a decrypted list
    key = matrix(key)
    determinant = round(det(key)) % 27
    adjoint = det(key) * inv(key)
    adjoint = adjoint.tolist()
    table = {}
    for k in range(27 + 1):
        for l in range(27 + 1):
            if (k * l) % 27 == 1:
                table[k] = l
    determinant = table[determinant]
    for i in range(len(adjoint)):
        for j in range(len(adjoint[i])):
            adjoint[i][j] = round(adjoint[i][j]) % 27
            adjoint[i][j] = adjoint[i][j] * determinant
            adjoint[i][j] = adjoint[i][j] % 27
    list = matrix(list)
    inverse_key = matrix(adjoint)
    product = list * inverse_key
    product = product.tolist()
    for i in range(len(product)):
        for j in range(len(product[i])):
            product[i][j] = product[i][j] % 27
    return product


def keygen(string): # takes a stream of string characters and turns them into a 3 x 3 matrix
    key = alpha_num(string)
    key = matrix(key).reshape(3, 3)
    key = key.tolist()
    return key


def det_check(matrix):  # takes a matrix and checks the determinant of the matrix, then return a boolean value
    determinant = det(matrix)
    determinant = round(determinant)
    table = {}
    status = True
    for k in range(27 + 1):
        for l in range(27 + 1):
            if (k * l) % 27 == 1:
                table[k] = l
    if determinant in table.keys():
        return status
    else:
        status = False
        return status


def checknum(string): # Checks if string has numbers
    for i in string:
        if i.isdigit() == True:
            return True
    return False
# the matrices used in numpy are weird and look like that [[1,2,3][4,5,6][7,8,9]]
# you can change matrices into normal lists by using the .tolist() method
# ask me anytime you want for more information isa hab2a free to reply