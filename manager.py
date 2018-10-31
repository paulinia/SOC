from math import sqrt

def reaches_bottom(simul):
    while not simul.has_ended():
        simul.step()
    
    for i in range(simul.c):
        if simul.was_on_pos(i, simul.c - 1):
            return 1.0
        
    return 0.0

def get_average_data(simul, p, r, c):
    num = 400 # magic constant, number of runs
    reaches = 0
    for i in range(num):
        res = reaches_bottom(simul(p, r, c))
        reaches = reaches + res
    sigma = sqrt((reaches * ((1 - reaches / num) ** 2) + (num - reaches) * ((reaches / num) ** 2)) / num)
    return (p, reaches / num, 1.96 * sigma / sqrt(num))

def get_data(r, c, simul):
    step = 0.01 # another magic constant, dp
    data = []
    p = 0
    while p <= 1:
        data.append(get_average_data(simul, p, r, c))
        p += step
    return data
