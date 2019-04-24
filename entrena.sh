#!/bin/bash

. vars.sh

mkdir -p model/$MODEL
python $OD/model_main.py --model_dir model/$MODEL --pipeline_config_path=configs/$CONFIG
