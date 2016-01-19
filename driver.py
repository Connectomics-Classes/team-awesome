import download
import vesicle_feats
import numpy as np
from sklearn.ensemble import RandomForestClassifier 

zStart = 1000
zStop = 1025
padX = 50
padY = 50
padZ = 2
#high number currently for testing
#should become 2 for max data size later
sample_split = 100

#em image
eData = download.fetch_image(zStart, zStop, padX, padY, padZ)
#synapse image
sData = download.fetch_synapse(zStart, zStop, padX, padY, padZ)

#split into training & testing sets
es = np.array_split(eData, sample_split)
ss = np.array_split(sData, sample_split)
eDataTrain = es[0]
sDataTrain = ss[0]
eDataTest = es[1]
sDataTest = ss[1]

#extract feature
features = vesicle_feats(eDataTrain)

RFC = RandomForestClassifier(n_estimators = 2)
RFC.fit(features, sDataTrain)
