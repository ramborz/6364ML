import os
import numpy as np
import pandas as pd
from operator import itemgetter
from queue import PriorityQueue
import time



cwd = os.getcwd() 

print("enter size of map 100 200 500 1000 2000")
size = int(input())
print("enter version of map 1 2 3 4")
ver = int(input())
name = 'graphs\\graph'+str(size)+'_0.'+str(ver)

print("enter the start point")
start = int(input())
print("enter target point")
end = int(input())





'''name = 'graphs\\graph100_0.1'''
cwd = os.path.join(cwd, name )
E = os.path.join(cwd, "e.txt")
V = os.path.join(cwd, "v.txt")
edge = pd.read_csv(E)
vetx = pd.read_csv(V)

print (E)

print (V)



def LCP(str,end,road,hpq):
    next=hpq.pop()
    print(next)
    road.append(next)

    if(str==end):
        return road
    if(path[str]==[]):
        back=road.pop[-1];
        return LCP(back,end,road,hpq)
    tmp = len(path[str])
    for i in range (0,tmp):
        addcost = path[str][i]
        addcost.cost += next.cost
        hpq.append (addcost)
    print(hpq)
    hpq.sort(key=getKey)
    next=hpq.pop()
    print(next)
    road.append(next)
    return LCP(next.next,end,road,hpq)

def dijkstra (start,end):
    dist=[None]*size
    perv=[None] * size
    for i in range (0,size):
        dist[i]= size*14.1    
    dist[start]=0
   
    Q={}
    for i in range (0,size):
        Q[i]=(i,dist[i])
    vised = []
    while (len(Q)>0):
        tmp = list(Q.values())
        tmp.sort(key= getdist)
        temp = tmp.pop(0)
        u = Q.pop(temp[0])
        neigbers = path[u[0]]
        vised.append(u[0])
        if u[0]==end:
             
            return dist[end]

        for i in range (len(neigbers)):
            

            if (neigbers[i].next) in vised:
                 continue
           
            alt=u[1]+neigbers[i].cost

            neb = dist[neigbers[i].next]
            if(alt<neb):
                dist[neigbers[i].next] = alt
                perv[neigbers[i].next] = u[0]
                Q[neigbers[i].next]=(neigbers[i].next,alt)
                
              
  
    return None


def gettup(item):
    return item[1]
def getdist(item):
    return item[1]
def UCSS(start,goal):
    node=start
    cost = 0
    frontier=[]
    frontier+=path[node]
    frontier.sort(key=getKey)
    explored=[]
    while(len(frontier)>0):
        node = frontier.pop();
        if (node==goal):
            print("goal")
            return sol
        explored.append(node)
        for i in range (len(path[node.it])):
            if(path[node.it][i].next not in explored):
                child = path[node.it][i]
                cost+=path[node.it][i].cost
                frontier.append(child)
                
def UCS( start, goal):
    visited = set()
    uqueue = PriorityQueue()
    uqueue.put((0, start))
    while uqueue:
        cost, node = uqueue.get()
        if node not in visited: 
            visited.add(node)
            if node == goal:
                return cost
            if(node in path.keys()):
                for i in  range (len(path[node])):
                    if path[node][i].next not in visited:
                        total_cost = cost + path[node][i].cost
                        uqueue.put((total_cost, path[node][i].next))
        return None
   




def A8(start, goal):
    visited = set()
    queue = PriorityQueue()
    gh=(((int(nodeat[end])%10 - int(nodeat[start])%10)**2+ (int(nodeat[end])//10 - int(nodeat[start])//10)**2)**(0.5))*14.1
    queue.put((gh, start, 0))
    while queue:
        fh, node, cost = queue.get()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return cost
            if(node in path.keys()):
                for i in  range (len(path[node])):
                    if path[node][i].next not in visited:
                        total_cost = cost + path[node][i].cost 
                        gh=(((int(nodeat[end])%10 - int(nodeat[path[node][i].next])%10)**2+ (int(nodeat[end])//10 - int(nodeat[path[node][i].next])//10)**2)**0.5)*14.1
                        queue.put((total_cost+gh, path[node][i].next,total_cost))
    return None
    

class vex:
    def __init__(self, it, next, cost):
        self.it = it
        self.next = next
        self.cost = cost
        self.path = []
    def __repr__(self):
        return '{}: {} {} {}'.format(self.__class__.__name__,
                                  self.it,
                                  self.next,
                                  self.cost
                                  )

def getKey(vex):
    return vex.cost  

nodeat = vetx.iloc[2:, 0:2].values
conn = edge.iloc[:,:].values
path = {}
ptr=0;

i = 0


while(ptr in range (0,len(edge))):

    neigber=[]
    while (conn[ptr][0]==i):
        tmp = vex(conn[ptr][0],conn[ptr][1],conn[ptr][2])
        neigber.append(tmp)
        '''print(tmp)'''
        ptr+=1
        if(ptr==len(edge)):
            break
    '''print(neigber)'''
    neigber.sort(key=getKey)
    '''print(neigber)'''
    path[i]=neigber
    i+=1
while (i <size):
        neigber=[]
        path[i]=(neigber)
        i+=1



    

hpq=[]


'''LCP(start,end,road,hpq)'''
print("A star cost                       ")
start_time = time.time()
cost=A8(start,end)
print("--- %s seconds ---" % (time.time() - start_time))
print(cost)
print("dijkstra cost")
start_time = time.time()
cos=dijkstra(start,end)
print("--- %s seconds ---" % (time.time() - start_time))

print(cos)

















