import download
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

	# em image
	eData = download.fetch_image(zStart, zStop, padX, padY, padZ)
	# synapse image
	sData = download.fetch_synapse(zStart, zStop, padX, padY, padZ)

	# split into training & testing sets
	es = np.array_split(eData, sample_split)
	ss = np.array_split(sData, sample_split)
	eDataTrain = es[0]
	sDataTrain = ss[0]
	eDataTest = es[1]
	sDataTest = ss[1]

	# extract feature
	xTrain = vesicle_feats(eDataTrain)
	xTest = vesicle_feats(eDataTest)

	yTrain = sDataTrain

	# train classifier
	clf = RandomForestClassifier(n_estimators = 2)
	clf.fit(xTrain, sDataTrain)
	clf_probs = clf.predict_proba(xTest)
	y_score = clf.decision_funciton(xTest)

	# Compute Percision-Recall and plot curve
	# percision = dict()
	# recall = dict()
	# average_precision = dict()
	# for i in range(n_classes):
    	# precision[i], recall[i], _ = precision_recall_curve(y_test[:, i],
        #                                                 	y_score[:, i])
    	# average_precision[i] = average_precision_score(y_test[:, i], y_score[:, i])

    # Plot Precision-Recall curve
	# plt.clf()
	# plt.plot(recall[0], precision[0], label='Precision-Recall curve')
	# plt.xlabel('Recall')
	# plt.ylabel('Precision')
	# plt.ylim([0.0, 1.05])
	# plt.xlim([0.0, 1.0])
	# plt.title('Precision-Recall example: AUC={0:0.2f}'.format(average_precision[0]))
	# plt.legend(loc="lower left")
	# plt.show()

	sys.exit();

if __name__ == '__main__':
    main()
