from random import random as rand

class Simulation:
    def __init__(self, p, r, c):
        self.r = r
        self.c = c
        self.graph = [[rand() < p for i in range(r)] for j in range(c)]
        self.visited = [[False for i in range(r)] for j in range(c)]
        self.in_queue = []
        
        for i in range(r):
            if self.graph[i][0]:
                self.in_queue.append((i, 0))
                self.visited[i][0] = True
        
    def was_on_pos(self, x, y):
        return self.visited[x][y]
    
    def has_ended(self):
        return len(self.in_queue) == 0
    
    def step(self):
        new = []
        for x, y in self.in_queue:
            adj = self.neighbors(x, y)
            for X, Y in adj:
                if not self.visited[X][Y]:
                    self.visited[X][Y] = True
                    new.append((X, Y))
        
        self.in_queue = new
    
    def neighbors(self, x, y):
        return [] #Example
    
    def get_size(self):
        return (self.r, self.c) #or rewrite it by yourself
    
class Downside(Simulation):
    def neighbors(self, x, y):
        D = [(0, 1), (1, 0), (-1, 0)]
        adj = []
        for dx, dy in D:
            if dx + x >= 0 and dx + x < self.get_size()[1] and dy + y >= 0 and dy + y < self.get_size()[0]:
                if self.graph[x + dx][y + dy]:
                    adj.append((x + dx, y + dy))
        return adj
