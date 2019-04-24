import argparse
import numpy as np
import pandas as pd
from pathlib import Path
from tqdm import tqdm

parser = argparse.ArgumentParser(
    description='My CSV to Tensorflow CSV')
parser.add_argument('mycsvin', type=Path, help='My CSV in')
parser.add_argument('mycsvout', type=Path, help='My CSV out')
parser.add_argument('size', type=int, help='Nuevo tamaño para las cajas')
args = parser.parse_args()

df = pd.read_csv(args.mycsvin)

labels = [ 'lazul', 'lverde', 'vazam', 'vamve' ]
#labels = set( col.rstrip('_x') for col in df.columns[2::4])


for idx, row in tqdm(df.iterrows(), total=len(df)):
    for label in labels:
        if not np.isnan(row[label + '_x']):
            x, y, w, h = ( row[label + '_' + suffix] for suffix in ('x', 'y', 'w', 'h') )
            # centro
            cx = x + w / 2
            cy = y + h / 2
            # nuevas coordenadas
            nw = args.size if w < args.size else w
            nh = args.size if h < args.size else h
            df.loc[idx, label + '_x'] = cx - nw / 2
            df.loc[idx, label + '_y'] = cy - nh / 2
            df.loc[idx, label + '_w'] = nw
            df.loc[idx, label + '_h'] = nh
            
df.to_csv(args.mycsvout, index=False)
