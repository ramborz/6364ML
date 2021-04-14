
import os
import numpy as np
import pandas as pd
import time

cwd = os.getcwd() 
print("enter file name")
flie = str(input())
#flie = "i1.txt"
cwd = os.path.join(cwd, flie)
print(cwd)


file = open(cwd, "r")
size = file.readline()
size = int(size)
gamma = file.readline()
gamma = float(gamma)
noises = file.readline()
noises= noises.rstrip('               \n').split(', ')
noise = []
for i in noises:
    noise.append(float(i))

grid = []
file.readline()
for i in range (size):
    line = []
    row = file.readline()
    
    row = row.rstrip('                  \n').split(',')
    row = np.chararray.replace(row,"X","0")

    
    for j in row:
        if j =="X": 
           line.append(None)
           continue
        line.append(float(j))
    grid.append(line)
   

print(size)
print(gamma)
print(noises)
print (grid)



move = (
        (1,0), #right
        (-1,0), #left
        (0,1),  #up
        (0,-1)) #down



def pole(policy, grid):
    #Policy Evaluation
        V_old = np.zeros(size)
        while True:
            V_new = np.zeros(size)
            delta = 0
            for s in range (len(noise)):
                v_fn = 0
                action_probs = noise[s]
                for a in range(size):
                    next_state = grid[s][a]
                    v_fn += action_probs * (np.max(np.max(grid) + gamma * V_old[a]))
                delta = max(delta, abs(v_fn - V_old[s]))
                V_new[s] = v_fn
            V_old = V_new
            if(delta < size):
                break
        return V_old



def polit (iter):

        
    def one_step_lookahead(s, value_fn):
         actions = np.zeros(size)
         for a in range(len(move)):
                    next_state = grid[s][a]
                    actions[a]= noise[a]* (np.max(grid) + gamma * value_fn[a])
                    return actions

    for ite in range (iter):   
        policy = np.ones(size)
        actions_values = np.zeros(size)
        ns  = [[]*size]*size
        while True:
                value_fn = pole(policy, grid)
                policy_stable = True
                for s in range(len(ns)):
                    actions_values = one_step_lookahead(s, value_fn)
                    best_action = np.argmax(actions_values)
                    chosen_action = np.argmax(policy[s])
                    if(best_action != chosen_action):
                        policy_stable = False
                    policy[s] =best_action
                if(policy_stable):
                    return  value_fn



def valit (iter):
    out = grid
    for ite in range (iter):
           for i in range(size):
               for j in range(size):
                    out[i][ j] = valu(i, j, out)
    return out


def valu(x,y,out):
         
            if (x ==0 and y==0): 
                 return np.max(
                    gamma * np.sum(
                    out[x][y] * noise[0])+(out[x+1][y]+ out[x][y+1])* noise[1]
                    )

            if y == size-1 and x == size-1:
                return np.max(
                gamma * np.sum(
                    out[x][y] * noise[0])+(out[x-1][y]+ out[x][y-1]) * noise[2]
                )
            
            if x ==0 and y == size-1:
                return np.max(
                gamma * np.sum(
                    out[x][y] * noise[0])+(out[x+1][y])* noise[1]+ + ( out[x][y-1]) * noise[2]
                 )

            if y == size-1 & x == 0:
                return np.max(
                gamma * np.sum(
                   out[x][y] * noise[0])+(out[x+1][y])* noise[1]+ + (out[x][y-1]) * noise[2]
                )
            if x == size-1:
                return np.max(
                gamma * np.sum(
                    out[x][y] * noise[0])+(out[x][y+1])* noise[1]+(out[x-1][y]+ out[x][y-1]) * noise[2]
                )
            if x ==0:
                return np.max(
                    gamma * np.sum(
                    out[x][y] * noise[0])+(out[x+1][y]+ out[x][y+1])* noise[1]+ out[x][y-1] * noise[2]
                    )
            if y == size-1:
                return np.max(
                gamma * np.sum(
                    out[x][y] * noise[0])+(out[x+1][y])* noise[1]+(out[x-1][y]+ out[x][y-1]) * noise[2]
                 )
            else:
                return np.max(
                    gamma * np.sum(
                    out[x][y] * noise[0])+(out[x+1][y]+ out[x][y+1])* noise[1]+ + (out[x-1][y]+ out[x][y-1]) * noise[2]
                ) 

print("==========================================================")
print("input time of iteration")
iter = int(input())
#iter=3
print("==========================================================")
print("value cost                       ")
start_time = time.time()
out = valit(iter )
print("--- %s seconds ---" % (time.time() - start_time))
print(out)
print("==========================================================")
print("==========================================================")
print("policy cost")
start_time = time.time()
cos=polit(iter)
print("--- %s seconds ---" % (time.time() - start_time))
print(cos)
print("==========================================================")


