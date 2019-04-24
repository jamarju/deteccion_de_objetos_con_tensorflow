import argparse
import numpy as np
import pandas as pd
from pathlib import Path
from tqdm import tqdm

parser = argparse.ArgumentParser(
    description='My CSV to Tensorflow CSV')
parser.add_argument('dir', type=Path, help='Directorio con frames (jpg)')
parser.add_argument('mycsv', type=Path, help='My CSV')
parser.add_argument('tfcsv', type=Path, help='Tensorflow CSV')
args = parser.parse_args()

tfcols = [ 'filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax' ]

mydf = pd.read_csv(args.mycsv, index_col=0)
for col in mydf.columns:
    pd.to_numeric(mydf[col])

labels = set( col.rstrip('_x') for col in mydf.columns[2::4] )
print(labels)

fl = sorted(args.dir.glob('*.jpg'))

tfdf = pd.DataFrame(columns=tfcols)

rows = []

for idx, p in enumerate(tqdm(fl)):
    fname = p.name
    w, h = int(mydf.at[fname, 'w']), int(mydf.at[fname, 'h'])
    for label in labels:
        cx, cy, cw, ch = (label + '_' + suffix for suffix in ('x', 'y', 'w', 'h'))
        if cx in mydf.columns:
            assert cy in mydf.columns and cw in mydf.columns and ch in mydf.columns
            lx, ly = mydf.at[fname, cx], mydf.at[fname, cy]
            lw, lh = mydf.at[fname, cw], mydf.at[fname, ch]
            if not np.isnan(lx) and not np.isnan(ly) and not np.isnan(lw) and not np.isnan(lh):
                lx, ly, lw, lh = int(lx), int(ly), int(lw), int(lh)
                # Clamp to avoid 'maximum box coordinate value is larger than 1.100000' TF error
                xmin = lx
                ymin = ly
                xmax = lx + lw
                ymax = ly + lh
                if xmin < 0: xmin = 0
                if ymin < 0: ymin = 0
                if xmax >= w: xmax = w-1
                if ymax >= h: ymax = h-1
                rows.append({
                    'filename': fname,
                    'width': w,
                    'height': h,
                    'class': label,
                    'xmin': xmin,
                    'ymin': ymin,
                    'xmax': xmax,
                    'ymax': ymax
                    })

tfdf = tfdf.append(rows, ignore_index=True)
tfdf.to_csv(args.tfcsv, index=False)

