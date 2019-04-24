import argparse
import cv2
import numpy as np
import pandas as pd
from pathlib import Path
from tqdm import tqdm

parser = argparse.ArgumentParser(
    description='My CSV to Tensorflow CSV')
parser.add_argument('dir', type=Path, help='Directorio con frames (jpg)')
parser.add_argument('mycsvin', type=Path, help='My CSV (in)')
parser.add_argument('mycsvout', type=Path, help='My CSV (out)')
parser.add_argument('threshold', type=int, nargs='?', default=30, help='MSE thresh between images (def 30)')
parser.add_argument('-d', '--delete', action='store_true', help='Delete rejects')
args = parser.parse_args()

fl = sorted(args.dir.glob('*.jpg'))
last_img = None

df = pd.read_csv(args.mycsvin, index_col=0)
#df.sort_index(inplace=True)
rows = []
keep = total = 0

t = tqdm(fl)

for f in t:
    img = cv2.imread(str(f))

    if last_img is None or img.shape != last_img.shape or ((img - last_img)**2).mean() > args.threshold:
        rows.append(f.name)
        keep += 1
        last_img = img
    else:
        f.unlink()
    
    total += 1
    t.set_description(f'keep/total = {keep}/{total}')

dfout = df.loc[rows]
dfout.to_csv(args.mycsvout, index_label='fname')
