#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 13:46:41 2018

@author: kernel
"""
from copy import deepcopy


def backtracking_lookahead(X, D, C):
    
    history_D = [[] for i in range(option)]
   

    i = 0

    while (i >= 0 and i <= option -1):

        history_D[i] = deepcopy(D)
        X[i] = selectval_fc(D, i, history_D[i])
        print("X[{0}] = {1}".format(i, X[i]))

        if X[i] == None:
            
            X[i] = 0
            i = i - 1
            for j in range(i+1, option):
                D[j] = deepcopy(history_D[i][j])

            history_D[i] = deepcopy(D) 
            print("recover domain:", D)
        else:
            print("update domain:", D)
            if i <= option-1:
                i = i + 1
                #if i <= option-1:
                 #   print("up",i)
                  #  history_D[i] = deepcopy(D)
                   # print("h[",i,"]", history_D)
            
        print("X", X)

    
    if i == -1:
        return None
    else:
        return X
    
    

def selectval_fc(D, i, temp_D):
    while(D[i] != []):
        vi = D[i][0]
        D[i].remove(vi)
        print("delete {0} from D[{1}]".format(vi, i))
        
        empty_f = False
        
        for j in range(i+1, option):
            for u in list(D[j]):
                is_consistent = fit_consistent(i, j, vi, u)
                if not is_consistent:
                    print("not consistent",i,j,vi,u)
                   
                    D[j].remove(u)
                    # print("not consistent", i,j,vi,u)
                else:
                    print("is consistent",i,j,vi,u)

            if D[j] == []:
                # print(i, j, " j is []")
                empty_f = True

        
        if empty_f == True:
            for j in range(i+1, option):
                D[j] = deepcopy(temp_D[j])
        else:
            return vi
        
    return None
        


    


def fit_consistent(i, j, vi, u):
    
    is_consistent = False

#    print(".x[",i,"]", "x[",j,"]",vi,u)
    if j in C[i]:
#        has relation
#        update domain
        if ((i == 0 and j == 3) or (i == 3 and j == 0)):
            for a in D[6]:
                # print("now ",a,vi,u, matrix[0][0], a)
                if vi + u == matrix[0][0] - a:
                    is_consistent = True
                    break

        elif ((i == 0 and j == 6) or (i == 6 and j == 0)):
            for a in D[3]:
                if vi + u == matrix[0][0] - a:
                    is_consistent = True
                    break
        elif ((i == 3 and j == 6) or (i == 6 and j == 3)):
            if vi + u == matrix[0][0] - X[0]:
                is_consistent = True
            
        elif ((i == 0 and j == 4) or (i == 4 and j == 0)) :
            if vi + u == matrix[0][1]:
                is_consistent = True
            
        elif ((i == 0 and j == 5) or (i == 5 and j == 0)):
            for a in D[7]:
                if vi + u == matrix[0][2] - a:
                    is_consistent = True
                    break
        elif ((i == 0 and j == 7) or (i == 7 and j == 0)):
            for a in D[5]:
                if vi + u == matrix[0][2] - a:
                    is_consistent = True
                    break
        elif ((i == 5 and j == 7) or (i == 7 and j == 5)):
            if vi + u == matrix[0][2] - X[0]:
                is_consistent = True
        
        elif ((i == 1 and j == 3) or (i == 3 and j == 1)):
            if vi + u == matrix[1][0]:
                is_consistent = True
            
        elif ((i == 1 and j == 4) or (i == 4 and j == 1)):
            for a in D[6]:
                for b in D[7]:
                    if vi + u == matrix[1][1] - a - b:
                        is_consistent = True
                        break

        elif ((i == 1 and j == 6) or (i == 6 and j == 1)):
            for a in D[4]:
                for b in D[7]:
                    if vi + u == matrix[1][1] - a - b:
                        is_consistent = True
                        break
        elif ((i == 1 and j == 7) or (i == 7 and j == 1)):
            for a in D[4]:
                for b in D[6]:
                    if vi + u == matrix[1][1] - a - b:
                        is_consistent = True
                        break
        elif ((i == 4 and j == 6) or (i == 6 and j == 4)):
            for a in D[7]:
                if vi + u == matrix[1][1] - X[1] - a:
                    is_consistent = True
                    break

        elif ((i == 4 and j == 7) or (i == 7 and j == 4)):
            for a in D[6]:
                if vi + u == matrix[1][1] - X[1] - a:
                    is_consistent = True
                    break
        elif ((i == 6 and j == 7) or (i == 7 and j == 6)):
            if vi + u == matrix[1][1] - X[1] - X[4]:
                is_consistent = True
            
        
        elif ((i == 1 and j == 5) or (i == 5 and j == 1)):
            if vi + u == matrix[1][2]:
                is_consistent = True
            
            
            
        elif ((i == 2 and j == 3) or (i == 3 and j == 2)):
            for a in D[7]:
                if vi + u == matrix[2][0] - a:
                    is_consistent = True
                    break
        elif ((i == 2 and j == 7) or (i == 7 and j == 2)):
            for a in D[3]:
                if vi + u == matrix[2][0] - a:
                    is_consistent = True
                    break
        elif ((i == 3 and j == 7) or (i == 7 and j == 3)):
            if vi + u == matrix[2][0] - X[2]:
                is_consistent = True
            
        elif ((i == 2 and j == 4) or (i == 4 and j == 2)):
            if vi + u == matrix[2][1]:
                is_consistent = True
        
        elif ((i == 2 and j == 5) or (i == 5 and j == 2)):
            for a in D[6]:
                if vi + u == matrix[2][2] - a:
                    is_consistent = True
                    break
        elif ((i == 2 and j == 6) or (i == 6 and j == 2)):
            for a in D[5]:
                if vi + u == matrix[2][2] - a:
                    is_consistent = True
                    break
        elif ((i == 5 and j == 6) or (i == 6 and j == 5)):
            if vi + u == matrix[2][2] - X[2]:
                is_consistent = True
    else:
        is_consistent = True
    
# add

    return is_consistent


def init_domain(matrix):
   
    D = [[] for i in range(option)]
    
    for i in range(matrix_size):
        x = int(i/matrix_dim)
        y = i%matrix_dim
        num = matrix[x][y]

        
        if i == 0:
            init_partial_domain(D[0], num)
            init_partial_domain(D[3], num)
            init_partial_domain(D[6], num)
        elif i == 1:
            init_partial_domain(D[0], num)
            init_partial_domain(D[4], num)
        elif i == 2:
            init_partial_domain(D[0], num)
            init_partial_domain(D[5], num)
            init_partial_domain(D[7], num)
        elif i == 3:
            init_partial_domain(D[1], num)
            init_partial_domain(D[3], num)
        elif i == 4:
            init_partial_domain(D[1], num)
            init_partial_domain(D[4], num)
            init_partial_domain(D[6], num)
            init_partial_domain(D[7], num)
        elif i == 5:
            init_partial_domain(D[1], num)
            init_partial_domain(D[5], num)
        elif i == 6:
            init_partial_domain(D[2], num)
            init_partial_domain(D[3], num)
            init_partial_domain(D[7], num)
        elif i == 7:
            init_partial_domain(D[2], num)
            init_partial_domain(D[4], num)
        elif i == 8:
            init_partial_domain(D[2], num)
            init_partial_domain(D[5], num)
            init_partial_domain(D[6], num)
        else:
            print()  
    return D

def init_partial_domain(Di, num):
    
    temp_domain = [i for i in range(num+1)]
    if Di != []:
        for d in list(Di):
            if d not in temp_domain:
                Di.remove(d)
                
    else:
        for i in range(num, -1, -1):
            Di.append(i)


def init_constrant():
   
    C = [[] for i in range(option)]
    for i in range(option):
        if i in range(0, 3):
            init_partial_constrant(C[i], 3)
            init_partial_constrant(C[i], 4)
            init_partial_constrant(C[i], 5)
            init_partial_constrant(C[i], 6)
            init_partial_constrant(C[i], 7)
        elif i in range(3, 6):
            init_partial_constrant(C[i], 0)
            init_partial_constrant(C[i], 1)
            init_partial_constrant(C[i], 2)
            init_partial_constrant(C[i], 6)
            init_partial_constrant(C[i], 7)
        elif i == 6:
            init_partial_constrant(C[i], 0)
            init_partial_constrant(C[i], 1)
            init_partial_constrant(C[i], 2)
            init_partial_constrant(C[i], 3)
            init_partial_constrant(C[i], 4)
            init_partial_constrant(C[i], 5)
            init_partial_constrant(C[i], 7)
        elif i == 7:
            init_partial_constrant(C[i], 0)
            init_partial_constrant(C[i], 1)
            init_partial_constrant(C[i], 2)
            init_partial_constrant(C[i], 3)
            init_partial_constrant(C[i], 4)
            init_partial_constrant(C[i], 5)
            init_partial_constrant(C[i], 6)
        else:
            print()
    return C

def init_partial_constrant(Ci, Xi):
    Ci.append(Xi)
    
            

if __name__ == "__main__":
    matrix =  [[4, 4, 4 ], [1, 4, 1 ], [1, 1, 1 ]]
    matrix =  [[31, 25, 40 ], [30, 47, 37 ], [31, 23, 36 ]]
    #matrix =  [[57, 43, 54 ], [24, 49, 36 ], [18, 19, 45 ]]

    matrix_dim = len(matrix)
    option = 2*matrix_dim+2
    matrix_size = matrix_dim*matrix_dim
    
    print("M", matrix)
    
    X = [0 for i in range(option)]
    print("X", X)
    D = init_domain(matrix)
    print("D", D)
    C = init_constrant()
    print("C", C)
#    P = [i for i in range(option)]
#    print("P", P)
    solution = backtracking_lookahead(X, D, C)
    print(">>> solution", solution)
    
    