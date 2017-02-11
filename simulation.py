from random import random as rand

class Simulation:
    def __init__(p, n, m):
        self.n = n
        self.m = m
        self.graph = [[rand() < p for i in range(n)] for j in range(m)]
        self.visited = [[False for i in range(n)] for j in range(m)]
        self.in_queue = []
        
        for i in range(n):
            if self.graph[0][i]:
                self.in_queue.append((0, i))
                self.visited[0][i] = True
        
    def water_on_pos(self, x, y):
        return self.visited[x][y]
    
    def has_ended(self):
        return len(self.in_queue) == 0
    
    def step(self):
        new = []
        for x, y in self.in_queue:
            adj = self.neighbours(x, y)
            for X, Y in adj:
                if !visited[X][Y]:
                    visited[X][Y] = True
                    new.append((X, Y))
        
        self.in_queue = new
            
    def neighbours(self, x, y):
        return [] # Example
    
    def get_size(self):
        return (self.n, self.m)
    
class Downside(Simulation):
    def neighbours(self, x, y):
        pass # TODO
