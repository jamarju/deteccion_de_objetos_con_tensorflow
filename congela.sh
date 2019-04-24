#!/bin/bash

. vars.sh

STEP=3000

python export_inference_graph.py \
	--trained_checkpoint_prefix=model/$MODEL/model.ckpt-$STEP \
	--pipeline_config_path=configs/$CONFIG \
	--output_directory=model/$MODEL/frozen
