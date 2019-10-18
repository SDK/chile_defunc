#!/usr/bin/env python

import pandas as pd
import os
import sys

filename = sys.argv[1]
df = pd.read_excel(filename)
ext = filename.split('.')[-1]
df.to_csv(filename.replace(ext,'csv'))
