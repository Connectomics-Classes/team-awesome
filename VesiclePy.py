import sys
import ndio
import ndio.remote.OCP as OCP
import ndio.remote.OCPMeta as NDLIMS
import numpy as np
from sklearn.ensemble import RandomForestClassifier

eDataTrain = None
mDataTrain = None
sDataTrain = None
vDataTrain = None

def get_ac4_data(zStart, zEnd, padX, padY, padZ):
	oo = OCP()
	nn = NDLIMS()

	# see list of tokens
	# tokens = oo.get_public_tokens()

	# image
	eDataTrain = oo.get_cutout('kasthuri11cc', 'image', 4400 - padX, 5424 + padX, 5440 - padY, 6464 + padY, 1100 - padZ, 1200 + padZ, resolution = 1)

	# synapse
	sDataTrain = oo.get_cutout('ac3ac4', 'ac4_synapse_truth', 4400 - padX, 5424 + padX, 5440 - padY, 6464 + padY, 1100 - padZ, 1200 + padZ, resolution = 1)

	# membranes
	mDataTrain = oo.get_cutout('cv_kasthuri11_membrane_2014', 'image', 4400 - padX, 5424 + padX, 5440 - padY, 6464 + padY, 1100 - padZ, 1200 + padZ, resolution = 1)

	# vesicles
	vDataTrain = oo.get_cutout('cv_kasthuri11_membrane_2014', 'annotation', 4400 - padX, 5424 + padX, 5440 - padY, 6464 + padY, 1100 - padZ, 1200 + padZ, resolution = 1)


def versiclerf_train(outputFile):
	# find valid pixels
	mThresh = 0.75
	mm = (mDataTrain.data > mThresh)
	# mm = imdilate(mm, strel('disk', 5))
	# mm = bwareopen(mm, 1000, 4)
	pixValid = np.where(mm > 0)

	# extract features
	Xtrain = versiclerf_feats(eDataTrain.data, pixValid, vDataTrain)

	# classifier training
	Ytrain = create_labels_pixel(sDataTrain.data, pixValid, [50, 50, 2]);
	trTarget = np.where(Ytrain > 0);
	trClutter = np.where(Ytrain == 0);

	idxT =  np.random.permutation(range(len(trTarget)))
	idxC = np.random.permutation(range(len(trClutter)))

	print "Ready to classify"
	nPoints = min(100000, len(trTarget))

	# trainLabel = [Ytrain(trTarget(idxT(1:nPoints))); ...
    #	Ytrain(trClutter(idxC(1:nPoints)))];

    # trainFeat = [Xtrain(trTarget(idxT(1:nPoints)),:); ...
    #	Xtrain(trClutter(idxC(1:nPoints)),:)];

    #classifier = classRF_train(doube(trainFeat), double(trainLabel),...
    #	200, floor(sqrt(size(trainFeat, 2))));

	print "training complete"

	save(outputFile, 'classifier')

def main():

	sys.exit();

if __name__ == '__main__':
    main()






