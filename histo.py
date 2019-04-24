import argparse
import numpy as np
import pandas as pd
from collections import defaultdict
from pathlib import Path
from tqdm import tqdm

parser = argparse.ArgumentParser(
    description='Muestra histograma del training set')
parser.add_argument('mycsvin', type=Path, help='My CSV')
#parser.add_argument('mycsvout', type=Path, help='My equalized CSV')
parser.add_argument('bins', type=int, nargs='?', default=10, help='Number of bins (def 10)')
#parser.add_argument('mspb', type=int, nargs='?', default=20, help='Max samples per bin (def 20)')
args = parser.parse_args()

df = pd.read_csv(args.mycsvin)

labels = set( col.rstrip('_x') for col in df.columns[3::4])
print(labels)

bins = defaultdict(lambda: np.zeros((args.bins, args.bins), dtype=np.int32))

for idx, row in tqdm(df.iterrows(), total=len(df)):
    imgw, imgh = row['w'], row['h']
    for label in labels:
        if not np.isnan(row[label + '_x']):
            x, y, w, h = ( row[label + '_' + suffix] for suffix in ('x', 'y', 'w', 'h') )
            cx = x + w / 2
            cy = y + h / 2
            xbin = int(cx * args.bins / imgw)
            ybin = int(cy * args.bins / imgh)
            bins[label][ybin][xbin] += 1

for label in labels:
    print(label)
    print(bins[label])

