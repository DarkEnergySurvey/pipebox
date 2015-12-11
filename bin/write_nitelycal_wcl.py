#!/usr/bin/env python

from pipebox import copy_pipeline as pipeline, pipebox_utils

# initialize and get options
nitelycal = pipeline.NitelyCal()   
args = nitelycal.args

if args.auto:
    # run auto-submit
    nitelycal.auto(args)
else:    
    if args.combine:
        # create ticket based on date range
        nitelycal.ticket(args,groupby='niterange')
    else:
        # create tickets based on each nite
        nitelycal.ticket(args)
    # write submit files for each nite and submit if necessary
    nitelycal.make_templates() 

