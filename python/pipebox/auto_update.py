from pipebox import pipequery

# Create db connection
pipeline = pipequery.PipeQuery('db-desoper')

# Find unitnames that have been successfully processed and update auto_queue
pipeline.update_auto_queue()
