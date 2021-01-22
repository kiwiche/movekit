from matplotlib import pyplot as plt
import numpy as np
import movekit
from scipy.stats import gaussian_kde

# Enter absolute/complete path to CSV file-
path_to_file = "datasets/fish-5.csv"

# Read in CSV file using 'path_to_file' variable-
data = movekit.read_data(path_to_file)


x = np.linspace(0, 100, 1000)

hlist = [p1, p2, p1]
kdelist = [gaussian_kde(p[:, 0], bw_method=.4, weights=p[:, 1]) for p in hlist]

steps = 20

fig, ax = plt.subplots()
for i in range(len(kdelist) - 1):
    for s in range(steps + 1):
        plt.plot(x, kdelist[i](x) * s / steps + kdelist[i + 1](x) * (1 - s / steps), color='crimson')
        plt.ylim(0, 0.065)
        plt.savefig(f'kde_{i*(steps+1)+s:04d}.png')
        plt.cla() # needed to remove the plot because savefig doesn't clear it
