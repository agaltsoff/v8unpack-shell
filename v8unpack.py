import argparse

parser = argparse.ArgumentParser(description='v8unpack source to destination directory. Destination defaults to source.unpacked')

parser.add_argument('-src', required= True, metavar= 'SOURCE', help='source directory')
parser.add_argument('-dst', metavar= 'DESTINATION', help='destination directory')

args = parser.parse_args()

import subprocess
import os

src= args.src
dst= args.dst if args.dst is not None else args.src + '.unpacked'

for root, dirs, files in os.walk(src):
    for fn in files:
        ffn= os.path.join(root, fn)
        ddn= os.path.join(dst, os.path.relpath(ffn, src))
        print(ffn)
        os.makedirs(ddn)
        subprocess.call('v8unpack.exe -P "%s" "%s"'%(ffn, ddn))

        
