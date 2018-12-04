from __future__ import division
import numpy as np

def pageRank(Graph, s = 0.2, maxerr = .001):
    nodes = Graph.shape[0]
    # Normalizing
    Graph=(Graph.T/np.sum(Graph,axis=1)).T
    # prob=np.random.rand(nodes,1)
    prob=np.array([1/nodes]*nodes)
    I=np.identity(nodes)

    # Compute pagerank r until we converge
    count=1
    while(1):
    	print count
    	Graph=Graph*(1-s)
    	Graph=(s*I +Graph).T
    	prob_new=np.matmul(Graph,prob)
    	if(sum(abs(prob_new-prob))<maxerr):
    		break
    	prob=prob_new
    	count+=1
        
    # return pagerank
    return prob_new

if __name__=='__main__':
    G = np.array([[0,0,0,0,1,0,0],
                  [1,0,0,0,0,0,0],
                  [0,0,0,0,0,1,0],
                  [0,0,0,0,1,0,1],
                  [1,0,0,1,0,0,0],
                  [0,0,0,0,1,0,0],
                  [0,1,0,0,1,0,0]])
    print pageRank(G,s=0.2)
