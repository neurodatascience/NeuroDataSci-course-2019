from bids import BIDSLayout

bids_dataset = '/home/emdupre/Desktop/ds000007'  # Change to your dataset location !
layout = BIDSLayout(bids_dataset)

# Let's learn a little about the data we have
layout.description
layout.get_modalities()
layout.get_tasks()
