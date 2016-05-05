#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 7
# Taras Sotnikov

import sys
import numpy as np

#Kadane algorithm 1D
def max_subarray(A):
    max_so_far = max_ending_here = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

#Maximum subarray sum. Complexity O(n^3)
def findMaxSum (matrix):
    maxSum = 0
    N = len(matrix)
    M = len(matrix[0])

    for i in xrange(M):
        temp = [0]*N;

        for j in xrange(i,M):
            for k in xrange(N):
                temp[k] += matrix[k][j]

            maxSum = max(maxSum, max_subarray(temp))

    return maxSum

#True if sum of any row or column is > 0
def check_matrix_sums(matrix):
    N = len(matrix)
    M = len(matrix[0])

    for row in matrix:
        if sum(row) > 0:
            return True

    for col in zip(*matrix):
        if sum(col) > 0:
            return True

    return False

#True if max element is > 0
def check_matrix_max(matrix):
    if matrix.max() > 0:
        return True
    else:
        return False

def parse_line(line):
    row = []
    for char in line:
        if char == ".":
            row.append(0)
        elif char.islower():
            row.append(-1*ord(char) + 96)
        else:
            row.append(ord(char) - 64)

    return row

n_cases = int(sys.stdin.readline())
for i in range(n_cases):
    dimensions = sys.stdin.readline().split()
    N = int(dimensions[0])
    M = int(dimensions[1])
    matrix = [None]*N
    for j in range(N):
        line = sys.stdin.readline().strip()
        matrix[j] = parse_line(line)    

    mtx = np.array(matrix)

    if not check_matrix_max(mtx):
        result = "0"
    elif check_matrix_sums(mtx):
        result = "INFINITY"
    else:
        N_aux = M_aux = 0
        if (N % 2) != 0:
            n_aux = 1
        if (M % 2) != 0:
            m_aux = 1

        aux_up_left = mtx[N-N/2-n_aux:N,M-M/2-m_aux:M]
        aux_up_center = mtx[N-N/2-n_aux:N,:]
        aux_up_right = mtx[N-N/2-n_aux:N,0:M-M/2]

        aux_center_left = mtx[:,M-M/2-m_aux:M]
        aux_center_right = mtx[:,0:M-M/2]

        aux_down_left = mtx[0:N-N/2,M-M/2-m_aux:M]
        aux_down_center = mtx[0:N-N/2,:]
        aux_down_right = mtx[0:N-N/2,0:M-M/2]
        
        aux_up = np.concatenate((aux_up_left,aux_up_center,aux_up_right), axis=1)
        aux_center = np.concatenate((aux_center_left,mtx,aux_center_right), axis=1)
        aux_down = np.concatenate((aux_down_left,aux_down_center,aux_down_right), axis=1)

        ext_matrix = np.vstack((aux_up,aux_center,aux_down))

        result = str(findMaxSum(ext_matrix))

    print "Case #%d: %s" % (i+1, result)