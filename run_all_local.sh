#!/bin/bash

# Run the commands in the background and redirect outputs using conda run
nohup conda run -n diss --no-capture-output python train.py --model transformer > output_transformer.log 2>&1 &
nohup conda run -n diss --no-capture-output python train.py --model mamba > output_mamba.log 2>&1 &
nohup conda run -n diss --no-capture-output python train.py --model rnn > output_rnn.log 2>&1 &

# Print message indicating that the scripts have been started
echo "Training scripts have been started in the background. Outputs are being logged to output_transformer.log, output_mamba.log, and output_rnn.log."
