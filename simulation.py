from random import random as rand

class Simulation:
    def __init__(self, p, n, m):
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
                if not self.visited[X][Y]:
                    self.visited[X][Y] = True
                    new.append((X, Y))
        
        self.in_queue = new
    
    def neighbours(self, x, y):
        return [] # Example
    
    def get_size(self):
        return (self.n, self.m) #or rewrite it by yourself
    
class Downside(Simulation):
    def neighbours(self, x, y):
        D = [(0, 1), (1, 0), (-1, 0)]
        adj = []
        for dx, dy in D:
            if dx + x >= 0 and dx + x < self.get_size()[0] and dy + y >= 0 and dy + y < self.get_size()[1]:
                if self.graph[y + dy][x + dx]:
                    adj.append((x + dx, y + dy))
        return adj
