import sys
import ndio
import ndio.remote.OCP as OCP
import ndio.remote.OCPMeta as NDLIMS

oo = OCP()
nn = NDLIMS()

#functions return numpy.ndarray

def fetch_image(zStart, zStop, padX, padY, padZ):
  # see list of tokens
  # tokens = oo.get_public_tokens()

  # image
  return oo.get_cutout('kasthuri11cc', 'image', 4400 - padX, 5424 + padX, 5440 - padY, 6464 + padY, 1100 - padZ, 1200 + padZ, resolution = 1)

def fetch_synapse(zStart, zStop, padX, padY, padZ):
  # synapse
  return oo.get_cutout('kasthuri2015_ramon_v1', 'synapses', 4400 - padX, 5424 + padX, 5440 - padY, 6464 + padY, 1100 - padZ, 1200 + padZ, resolution = 1)

  # # membranes
  # mData = oo.get_cutout('cv_kasthuri11_membrane_2014', 'image', resolution = 1)

  # # vesicles
  # vData = oo.get_cutout('cv_kasthuri11_membrane_2014', 'annotation', resolution = 1)
