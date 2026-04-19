import numpy as np 
from fractions import Fraction
from math import gcd

class DiscreteMarkovChain:
    def __init__(self,P:np.ndarray,states: list=None):
        P = np.array ( P, dtype=float)
        assert np.allclose(P.sum(axis=1),1) "Each row must sum to 1 "
        assert (P>=0).all() "Transition probabilities must be non-negative "
        self.P=P
        self.n=P.shape[0]
        self.states= states if states else list(range(self.n))

    def _reachable(self,i:int) : ## Comme si on travaille avec une file 
        visited = set()
        queue=[i]
        while queue:
            s=queue.pop()
            if s in visited:
                continue
            visited.add(s)
            for j in range(self.n):
                if self.P[s,j]>0 and j not in visited : 
                    queue.append(j)
                    return visited
    def communicates (i:int , j:int ) :
        return j in self._reachable(i) and i in self._reachable(j)
    def communication_classes(self):
        remaining = set (range(self.n))
        classes = []
        while remaining : 
            i= next(iter(remaining))
            class= {j for j in remaining if self.communicates(i,j)}
            classes.append(class)
            remaining-= class
        return classes 
    def is_closed (class : set) :
        for i in class : 
            for j in range (self.n):
                if self.P[i,j]>0 and j not in class : 
                    return False 
            return True   
    def classify_states(self):
        classes= self.communication_classes()
        result= {}
        for class in classes :
            closed = self.is_closed()
            nature = "recurrent" if closed else "transient"
            for s in class :
            period = self.period(s) 
            result[self.states(s)]={"nature"=nature, "class":{self.states[c] for c in class}, "period":period, "type": "absorbing" if (nature=="recurrent" and len(class)=1) else nature}
        return result 
    def period ( i;int):
        Pk=np.eye(self.n) ## cree la matrice identite 
        g=0
        for k in range(1,200):
            Pk= Pk @ self.P 
            if Pk[i,i]> 1e-12:
                g = gcd (g,k)
            if g==1 : 
                break
            return g if g>0 else 0 
    


    
                
                