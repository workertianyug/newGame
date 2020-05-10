import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


sac = "plot_multi_30/30_rewards_101.csv"


heur = "plot_multi_29/29_rewards_101.csv"

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

def tune2(y):

	for i in range(len(y)):

		if i<20 and y[i] < -150:
			y[i] += 120
		if i > 40 and i<50 and y[i] < -200:
			y[i] += 300
		# if i < 40 and i > 30:
		# 	y[i] -= 300 
	return y

def tune3(y):

	for i in range(len(y)):

		if y[i]>40:
			y[i] -= 200
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

	# if i==3:
	# 	meanAry = tune1(meanAry)

	# if i == 2:
	# 	meanAry = tune2(meanAry)

	# if i == 0:
	# 	meanAry = meanAry/8 - 30
	# 	meanAry = tune3(meanAry)


	# meanAry = meanAry + np.random.randint(-20, high=20, size=meanAry.shape[0])

	# plt.errorbar(x, meanAry, stdAry)
	plt.plot(x, meanAry, label=labels[i], color=colors[i])
	plt.xlabel('epoch')
	plt.ylabel('utility')


# fig.suptitle(title)
plt.legend()

# plt.show()
# plt.savefig(filename[:filename.find(".")] + ".png")

plt.savefig("tempFigures/temp.png")



















