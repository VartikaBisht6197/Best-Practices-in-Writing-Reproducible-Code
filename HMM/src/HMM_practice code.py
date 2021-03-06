import unittest
import pandas as pd
import os
import sys
from pathlib import Path
import numpy as np

# Path to the script (can be script name)
pathname = os.path.dirname(sys.argv[0])
# Absolute path to the script
src_dir = os.path.abspath(pathname)
# The directory to the main HMM file
HMM_dir = Path(src_dir).parent

# Emission Matrix
EmissionMatrix = pd.read_csv(os.path.join(HMM_dir, 'data', 'raw', 'EmissionMatrix.txt'), sep=' ', header=None)
EmissionMatrix = EmissionMatrix.to_numpy()

# Hidden State legends Matrix
HiddenMatrix = {0: 'I', 1: 'D', 2: 'M', 3: 'Mi'}

# Prior Matrix
StartingProbability = np.add(np.array(EmissionMatrix[0]), np.array(EmissionMatrix[1]))

# Transition Matrix
TransitionMatrix = []
for i in range(4):
    TransitionMatrixRow = []
    for j in range(4):
        Prob_i2j = StartingProbability[i] * StartingProbability[j]
        TransitionMatrixRow.append(Prob_i2j)
    TransitionMatrix.append(TransitionMatrixRow)



def MultiEle(A, B):
    '''
    Element wise multiplication
    Given two lists A and B, it multiplies respective elements of the list
    and returns a list AB (Specifically for [I D M MI] probability multiplication).
    As all the multiplication is needed while calculating the [I D M MI] probability
    so the number of elements in each list is 4
    :param A: the seconf list of elements
    :param B: the first list of elements
    :return: element wise multiplied list
    '''
    if len(A) == 0 or len(B) == 0:
        raise("Emty list provided. Something wrong with the input string")
    AB = []
    #
    for a in range(4):
        AB.append(A[a] * B[a])
    return AB


def FillMat(V_Mat, str1, str2):
    '''
    Fills in the Observation Matrix. It take VMat after FillInsDel as an input and returns the Filled Matrix
    :param V_Mat: matrix after FillInsDel
    :param str1: first string (base sequence)
    :param str2: second string (base sequence)
    :return: Filled matrix
    '''
    for let1 in range(1, len(str1)):
        for let2 in range(1, len(str2)):
            if str1[let1] == str2[let2]:
                simi = 0
            else:
                simi = 1
            V_Mat[let1][let2][0] = EmissionMatrix[simi][0] * max(MultiEle(V_Mat[let1][let2 - 1], TransitionMatrix[0]))
            V_Mat[let1][let2][1] = EmissionMatrix[simi][1] * max(MultiEle(V_Mat[let1 - 1][let2], TransitionMatrix[1]))
            V_Mat[let1][let2][2] = EmissionMatrix[simi][2] * max(
                MultiEle(V_Mat[let1 - 1][let2 - 1], TransitionMatrix[2]))
            V_Mat[let1][let2][3] = EmissionMatrix[simi][3] * max(
                MultiEle(V_Mat[let1 - 1][let2 - 1], TransitionMatrix[3]))
    return V_Mat


def FillInsDel(VMat, l1, l2):
    '''
    Fills the first row for Insertion and first column for deletion
    :param VMat: iniitial matrix ( empty )
    :param l1: length of first base sequence
    :param l2: length of second base sequence
    :return: matrix
    '''
    v_mat_count = 1
    for let in l2[1:]:
        if l1[0] == let:
            VMat[0][v_mat_count][0] = max(MultiEle(EmissionMatrix[0], VMat[0][v_mat_count - 1]))
        else:
            VMat[0][v_mat_count][0] = max(MultiEle(EmissionMatrix[1], VMat[0][v_mat_count - 1]))
        v_mat_count = v_mat_count + 1
    v_mat_count = 1
    for let in l1[1:]:
        if l2[0] == let:
            VMat[v_mat_count][0][1] = max(MultiEle(EmissionMatrix[0], VMat[v_mat_count - 1][0]))
        else:
            VMat[v_mat_count][0][1] = max(MultiEle(EmissionMatrix[1], VMat[v_mat_count - 1][0]))
        v_mat_count = v_mat_count + 1
    return VMat


def Viterbi(VMat, m, n):
    '''
    Given VMat filled as an Input, it returns the most probable path
    :param VMat: initial matrix
    :param m: length of string 1
    :param n: length of string 2
    :return: best path
    '''
    path = []
    max_at_each = [[[0 for z in range(2)] for y in range(n)] for x in range(m)]
    for i in range(m):
        for j in range(n):
            max_at_each[i][j][0] = max(VMat[i][j])
            max_at_each[i][j][1] = HiddenMatrix[VMat[i][j].index(max(VMat[i][j]))]
    g = m - 1
    h = n - 1
    while g > 0 and h > 0:
        check = [max_at_each[g - 1][h][0], max_at_each[g][h - 1][0], max_at_each[g - 1][h - 1][0]]
        if check.index(max(check)) == 0:
            path.append([g, h, max_at_each[g][h][1]])
            g = g - 1
        if check.index(max(check)) == 1:
            path.append([g, h, max_at_each[g][h][1]])
            h = h - 1
        if check.index(max(check)) == 2:
            path.append([g, h, max_at_each[g][h][1]])
            g = g - 1
            h = h - 1
    path.append([g, h, max_at_each[g][h][1]])
    if g == 0:
        for w in range(h - 1, -1, -1):
            path.append([g, h, max_at_each[g][h][1]])
    if h == 0:
        for u in range(g - 1, -1, -1):
            path.append([g, h, max_at_each[g][h][1]])
    return path


str1_path = os.path.join(HMM_dir, 'data', 'raw', 'string1.txt')
with open(str1_path, 'r') as file:
    str1 = file.read()

str2_path = os.path.join(HMM_dir, 'data', 'raw', 'string2.txt')
with open(str2_path, 'r') as file:
    str2 = file.read()

# Observation Matrix according to str1 and str2
VMat = [[[0 for z in range(4)] for y in range(len(str2))] for x in range(len(str1))]

# Fill in the (0,0) position using the prior matrix
if str1[0] == str2[0]:
    VMat[0][0] = MultiEle(EmissionMatrix[0], StartingProbability)
else:
    VMat[0][0] = MultiEle(EmissionMatrix[1], StartingProbability)

# Fill the Matrix
FillInsDel(VMat, str1, str2)
FillMat(VMat, str1, str2)

# Print the path
# TODO : add pictorial representation for the path formed.
original_stdout = sys.stdout
with open(os.path.join(HMM_dir, 'results', 'output', "HMM_output.txt"), "w")  as f:
    sys.stdout = f  # Change the standard output to the file we created.
    print(Viterbi(VMat, len(str1), len(str2)))
    sys.stdout = original_stdout
