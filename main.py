import manager
import simulation
import matplotlib.pyplot as plt

data = [manager.get_data(x, x, simulation.Downside) for x in range(500, 501, 1)];
print("\t\t\t".join([str(i) for i in range(500, 501, 1)]))
transform = [[str(dat[i][0]) + "\t" + str(dat[i][1]) + "\t" + str(dat[i][2]) for dat in data] for i in range(len(data[0]))]
print("\n".join(["\t".join(T) for T in transform]))
