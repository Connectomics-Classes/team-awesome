import sys
import ndio
import ndio.remote.OCP as OCP
import ndio.remote.OCPMeta as NDLIMS



def fetch_data(zStart, zEnd, padX, padY, padZ):
  oo = OCP()
  nn = NDLIMS()

  # see list of tokens
  # tokens = oo.get_public_tokens()

  # image
  eData = oo.get_cutout('kasthuri11cc', 'image', 4400 - padX, 5424 + padX, 5440 - padY, 6464 + padY, 1100 - padZ, 1200 + padZ, resolution = 1)
  print str(eData)
  # synapse
  sData = oo.get_cutout('ac3ac4', 'ac4_synapse_truth', resolution = 1)

  # membranes
  mData = oo.get_cutout('cv_kasthuri11_membrane_2014', 'image', resolution = 1)

  # vesicles
  vData = oo.get_cutout('cv_kasthuri11_membrane_2014', 'annotation', resolution = 1)


def versiclerf_train(outputFile):
  return
