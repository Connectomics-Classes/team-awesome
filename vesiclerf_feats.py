# Function to compute features for synapse detection.
#
# **Inputs**
#
# em: (uint8)
#   - Matrix containing the raw EM dataset of interest.
#
# idxToTest: (uint32)
#   - Vector containing a list of linear indices to use in feature extraction and downstream classification.
#
# vesicles: (string)
#   - Location of mat file containing a RAMONVolume named cube. The cube contains a binary mask indicating locations of putative neurotransmitter-containing vesicles.
#
# **Outputs**
#
# xt: (float)
#   - Matrix (NxD) containing features for N idxToTest datapoints and D features.
#

import numpy as np
from scipy import ndimage

def vesiclerf_feats(em):
  #return value
  xt = [] 
  num_features = 2

  # Kernels
  B0 = np.ones([5,5,1])/(5*5*1)
  B1 = np.ones([15,15,3])/(15*15*3)
  B2 = np.ones([25,25,5])/(25*25*5)

  ### Intensity Feats ###
  # find weighted average of features
  I0 = ndimage.convolve(em,B0,mode='constant')
  I2 = ndimage.convolve(em,B1,mode='constant')

  # reshape data
  # I0 = [np.reshape(I0,(I0.size,1)).tolist(), num_features]
  # I2 = [np.reshape(I2,(I2.size,1)).tolist(), num_features]
  # I0 = np.reshape(I0,(I0.size,1))
  I2 = np.reshape(I2,(I2.size,1))
  xt = I2
  #xt.append(I0)
  #xt.append(I2)

  return xt