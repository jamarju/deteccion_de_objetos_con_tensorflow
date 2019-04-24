import argparse
import numpy as np
import pandas as pd
from pathlib import Path
from tqdm import tqdm

parser = argparse.ArgumentParser(
    description='Filtra filas del csv no existentes en dir')
parser.add_argument('dir', type=Path, help='Dir')
parser.add_argument('mycsvin', type=Path, help='My CSV in')
parser.add_argument('mycsvout', type=Path, help='My CSV out')
args = parser.parse_args()

fl = [ f.name for f in sorted(args.dir.glob('*.jpg')) ]
df = pd.read_csv(args.mycsvin, index_col=0)
dfout = df.loc[fl]

dfout.to_csv(args.mycsvout, index_label='fname')

