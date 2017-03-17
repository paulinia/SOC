import manager
import simulation

#first try
data = manager.get_data(50, 50, simulation.Downside);
print("\n".join([str(dat[0]) for dat in data]))
