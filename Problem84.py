# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 09:48:19 2021

@author: Tobi
"""

import numpy as np
import numpy.linalg as LA

dice = range(1,7)
P_moves = {}
for i in dice:
    for j in dice:
        P_moves[i+j] = P_moves.get(i+j, 0) + 1
        


P = np.matrix(np.zeros(1600)).reshape(40, 40)

all_combs = sum(P_moves.values())
for i in range(40):
    for j in range(40):
        #a = P[i,j]
        P[i, j] = P_moves.get((j-i)%40, 0)/all_combs
        
# Go to Jail
P[:,10] += P[:,30]
P[:,30] = 0
# P[:,10].shape

# if three doubles are rolled in a row, person is sent to jail. prob for that is 1/216 (for 6-dice)
p_three_doubles = 1/len(dice)**3 # prob for three doubles
#P[:][P[:]>0] = P[:]
P = np.where(P>0,P-p_three_doubles,0) # substract these probabilities from every matrix element
P[:,10] += p_three_doubles # add this probability to the ones where one ends up in jail
P = P/P.sum(axis=1) # make every row a probability vector again (normalizing)
# --> das ist sehr wahrscheinlich falsch

# check
P.sum(axis=1) # --> good
P.sum(axis=0) # --> good

# Community chest
# advance to GO
P[:,0] += P[:,2]*1/16
P[:,0] += P[:,17]*1/16
P[:,0] += P[:,33]*1/16
# advance to jail
P[:,10] += P[:,2]*1/16
P[:,10] += P[:,17]*1/16
P[:,10] += P[:,33]*1/16
# adjust if the player stays on the square
P[:,2] = P[:,2]*14/16
P[:,17] = P[:,17]*14/16
P[:,33] = P[:,33]*14/16

# check
P.sum(axis=1) # -->  good


# Chance (10/16 cards):
# Advance to GO
P[:,0] += P[:,7]*1/16
P[:,0] += P[:,22]*1/16
P[:,0] += P[:,36]*1/16
# Go to JAIL
P[:,10] += P[:,7]*1/16
P[:,10] += P[:,22]*1/16
P[:,10] += P[:,36]*1/16
# Go to C1
P[:,11] += P[:,7]*1/16
P[:,11] += P[:,22]*1/16
P[:,11] += P[:,36]*1/16
# Go to E3
P[:,24] += P[:,7]*1/16
P[:,24] += P[:,22]*1/16
P[:,24] += P[:,36]*1/16
# Go to H2
P[:,39] += P[:,7]*1/16
P[:,39] += P[:,22]*1/16
P[:,39] += P[:,36]*1/16
# Go to R1
P[:,5] += P[:,7]*1/16
P[:,5] += P[:,22]*1/16
P[:,5] += P[:,36]*1/16
# Go to next R (railway company)
P[:,15] += P[:,7]*1/16
P[:,25] += P[:,22]*1/16
P[:,5] += P[:,36]*1/16
# Go to next R
P[:,15] += P[:,7]*1/16
P[:,25] += P[:,22]*1/16
P[:,5] += P[:,36]*1/16
# Go to next U (utility company)
P[:,12] += P[:,7]*1/16
P[:,28] += P[:,22]*1/16
P[:,12] += P[:,36]*1/16
# Go back 3 squares.
P[:,4] += P[:,7]*1/16
P[:,19] += P[:,22]*1/16
P[:,33] += P[:,36]*1/16
# adjust if the player stays on the square
P[:,7] = P[:,7]*6/16
P[:,22] = P[:,22]*6/16
P[:,36] = P[:,36]*6/16

# check
P.sum(axis=1) # -->  good
P.sum(axis=0) # -->  good

P_new = LA.matrix_power(P, 10000)

j = 0
dic = {}
for i in P_new[0,:]:
    dic[i] = j
    j+=1
    
s = sorted(dic.keys())
dic[s[-1]]
dic[s[-2]]
dic[s[-3]]
dic[s[-4]]

res = int(str(dic[s[-1]]) + str(dic[s[-2]]) + str(dic[s[-3]]))
print(res) # 101524