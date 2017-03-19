import simulation

simulations_per_data = 50

def reaches_bottom(simul):
    steps = 0
    while not simul.has_ended():
        steps += 1
        simul.step()
    
    for i in range(simul.n):
        if simul.water_on_pos(simul.m - 1, i):
            return (1, steps)
    
    return (0, steps)

def get_average_data(simul, p, n, m):
    num = 1000 # magic constant, number of runs
    reaches = 0
    sum_steps = 0
    for i in range(num):
        res = reaches_bottom(simul(p, n, m))
        reaches, sum_steps = reaches + res[0], sum_steps + res[1]
    return (reaches / num, sum_steps / num)

def get_data(n, m, simul):
    print("{}x{}".format(n, m))
    step = 0.01 # another magic constant
    data = []
    p = 0
    while p <= 1:
        data.append(get_average_data(simul, p, n, m))
        p += step
    return data
