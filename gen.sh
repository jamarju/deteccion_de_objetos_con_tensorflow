#!/bin/bash

. vars.sh

# Criba similares (OJO, LAS BORRA)
python filtra_similares.py -d train mytrain-cajas-originales.csv mytrain-cribado.csv

# Agranda cajas
python agranda_cajas.py mytrain-cribado.csv mytrain.csv 100
python agranda_cajas.py myvalid-cajas-originales.csv myvalid.csv 100

# -> CSV intermedio
python mycsv2tfcsv.py train mytrain.csv tftrain.csv
python mycsv2tfcsv.py valid myvalid.csv tfvalid.csv

# -> TF record
python generate_tfrecord.py --csv_input=tftrain.csv --image_dir=train --output_path=train.record
python generate_tfrecord.py --csv_input=tfvalid.csv --image_dir=valid --output_path=valid.record
