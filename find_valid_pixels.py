from skimage import morphology
from skimage.morphology import selem
from skimage.morphology import binary

def find_valid_pixels(mDataTrain):
	# find valid pixels
	mThresh = 0.75
	mm = mDataTrain > mThresh
	strel = selem.disk(5)
	mm = binary.binary_dilation(mm, strel)
	mm = morphology.remove_small_objects(mm, 1000, 4)
	pixValid = mm[mm > 0]
	return pixValid








