#!/usr/bin/env python
#thanks to:
#https://gist.github.com/bertspaan/8220892

import simpledbf as sdbf 
import os
import sys

filename = sys.argv[1]
print(filename)
if filename.endswith('.dbf') or filename.endswith('.DBF'):
    print("Converting %s to csv" % filename)
    csv_fn = filename[:-4]+ ".csv"
    with open(csv_fn,'wb') as csvfile:
        dbf = sdbf.Dbf5(filename)
        dbf.to_csv(csv_fn)
        print("Done...")
else:
  print("Filename does not end with .dbf")