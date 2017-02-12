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

def get_average_data(simul):
    num = 100 # magic constant, number of runs
    reaches = 0
    sum_steps = 0
    for i in range(num):
        reaches, sum_steps += reaches_bottom(simul)
    return (reaches / num, sum_steps / num)

def get_data_range(n, m, simul):
    step = 0.01 # another magic constant
    data = []
    for p in range(0, 1, step):
        data.append(get_average_data(simul(p, n, m)))
    return data
