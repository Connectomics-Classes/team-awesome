import sys
import ndio
import ndio.remote.OCP as OCP
import ndio.remote.OCPMeta as NDLIMS



def fetch_data():
oo = OCP()
nn = NDLIMS()

# see list of tokens
# tokens = oo.get_public_tokens()

token = 'cv_kasthuri11_vesicle_2014'
channel = 'annotation'

nn.get_metadata(token)


vesicle_annos = oo.get_cutout(token, channel, 694, 1794, 1750, 2640, 1004, 1154, resolution=1)
vesicle_image = oo.get_cutout('kasthuri11cc', 'image', 694, 1794, 1750, 2640, 1004, 1154, resolution=1)
synapse_annos = oo.get_cutout('kasthuri2015_ramon_v1', 'synapses', 694, 1794, 1750, 2640, 1004, 1154, resolution=1)

def versiclerf_train(outputFile):

