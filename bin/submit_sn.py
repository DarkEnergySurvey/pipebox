#!/usr/bin/env python

from pipebox import pipebox_utils, pipeline

# initialize and get options
sn = pipeline.SuperNova()
args = sn.args

if args.auto:
    # run auto-submit 
    sn.auto(args)
else:
    # create JIRA ticket per nite found (default)
    sn.ticket(args)
    # write submit files and submit if necessary
    # columns should only be values that change per submit (groupby)
    sn.make_templates(columns=['expnums','nite','field','band','firstexp','single','fringe','seqnum',
                               'ccdlist'],groupby=['nite','field','band'])
