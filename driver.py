# import download
import sys
import scipy.io as sio
import vesiclerf_feats
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score

import matplotlib.pyplot as plt


def main():
	zStart = 1000
	zStop = 1025
	padX = 50
	padY = 50
	padZ = 2
	# high number currently for testing
	# should become 2 for max data size later
	sample_split = 100

	# fetch standalone data
	data = sio.loadmat('standalone-data.mat')
	eData = data['em']
	sData = data['synapseTruth']
	# mData 

	# fetch data from the server
	# em image
	# eData = download.fetch_image(zStart, zStop, padX, padY, padZ)
	# synapse image
	# sData = download.fetch_synapse(zStart, zStop, padX, padY, padZ)

	# split into training & testing sets
	es = np.array_split(eData, sample_split)
	ss = np.array_split(sData, sample_split)
	eDataTrain = es[0]
	sDataTrain = ss[0]
	eDataTest = es[1]
	sDataTest = ss[1]

	# extract feature
	xTrain = vesiclerf_feats.vesiclerf_feats(eDataTrain)
	xTest = vesiclerf_feats.vesiclerf_feats(eDataTest)

	# create labels
	# pad = [50, 50, 2]
	# pixValid = find_valid_pixels[mData]
	# yTrain = create_labels_pixel(np.ravel(np.reshape(sDataTrain, (sDataTrain.size, 1))), pixValid, pad)

	yTrain = np.ravel(np.reshape(sDataTrain, (sDataTrain.size, 1)))
	yTrain[yTrain != 0] = 1
	yTest = np.ravel(np.reshape(sDataTest, (sDataTest.size, 1)))
	yTest[yTest != 0] = 1


	# train classifier
	clf = RandomForestClassifier(n_estimators = 10)
	clf.fit(xTrain, yTrain)
	yResult = clf.predict(xTest)
	clf_probs = clf.predict_proba(xTest)[:, 1]

	# Compute Percision-Recall and plot curve
	precision, recall, thresholds = precision_recall_curve(yTest, clf_probs)
	average_precision = average_precision_score(yTest, clf_probs)

    # Plot Precision-Recall curve
	plt.clf()
	plt.plot(recall, precision, label='Precision-Recall curve')
	print "recall"
	print recall
	print "precision"
	print precision
	plt.xlabel('Recall')
	plt.ylabel('Precision')
	plt.ylim([0.0, 1.05])
	plt.xlim([0.0, 1.0])
	plt.title('Precision-Recall example: AUC={0:0.2f}'.format(average_precision))
	plt.legend(loc="lower left")
	plt.show()

	sys.exit();

if __name__ == '__main__':
    main()
