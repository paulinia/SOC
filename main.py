import manager
import simulation
import matplotlib.pyplot as plt

#first try
data = [manager.get_data(x, x, simulation.Downside) for x in range(10, 20, 5)];
print("\t".join([str(i) for i in range(10, 20, 5)]))
transform = [[str(dat[i][0]) for dat in data] for i in range(len(data[0]))]
print("\n".join(["\t".join(T) for T in transform]))


plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
