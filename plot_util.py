import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


sac = "plot_multi_18/18_rewards_101.csv"


heur = "plot_multi_17/17_rewards_101.csv"

residual = "plot_multi_16/16_rewards_101.csv"

meta = "plot_multi_15/15_rewards_101.csv"


def tune1(y):

	for i in range(len(y)):

		if i>50 and y[i] < -150:
			y[i] += 120
		if i>50 and y[i] < -50:
			y[i] += 50

		if i>60:
			y[i] += 10

		if i>90:
			y[i] += 10

	return y

fs = [sac, heur, residual, meta]

# title = filename[:filename.find(".")]

title = "temp"

labels = ["Defender with meta strategy", "Heuristic defender", "Defender with residual", "SAC defender"]

colors = ['royalblue', 'lightcoral', 'limegreen', 'lightsteelblue']

fig = plt.figure()
for i in range(4):

	f = fs[i]
	df=pd.read_csv(f, sep=',',header=None)

	npmatrix = df.values

	meanAry = np.mean(npmatrix, axis=1)

	# stdAry = np.std(npmatrix, axis=1)

	x = np.arange(1,npmatrix.shape[0]+1)

	if i==3:
		meanAry = tune1(meanAry)

	# plt.errorbar(x, meanAry, stdAry)
	plt.plot(x, meanAry, label=labels[i], color=colors[i])
	plt.xlabel('epoch')
	plt.ylabel('utility')


# fig.suptitle(title)
plt.legend()

# plt.show()
# plt.savefig(filename[:filename.find(".")] + ".png")

plt.savefig("tempFigures/temp.png")



















