    imporkt simulation


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

    def get_average_data(p, n, m, state):
        
