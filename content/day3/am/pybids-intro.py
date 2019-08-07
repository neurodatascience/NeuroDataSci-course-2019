from bids import BIDSLayout

bids_dataset = '/home/emdupre/Desktop/ds000007'  # Change to your dataset location !

# first, we want to make sure we have a valid BIDS dataset !
# let's navigate to :
# https://bids-standard.github.io/bids-validator/

layout = BIDSLayout(bids_dataset)

# Let's learn a little about the data we have
layout.description
layout.get_modalities()
layout.get_tasks()
