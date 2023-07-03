# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:51:36 2023

@author: MFP-PC1
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from segpy.reader import create_reader
import matplotlib.pyplot as plt
import scipy
import numpy as np
from scipy.io import savemat

with open('D:\IS project\Seismic_data.sgy', 'rb') as file:
    # The seg_y_dataset is a lazy-reader, so keep the file open throughout.
    seismic = create_reader(file, endian='>')  # Non-standard Rev 1 little-endian
    print(seismic.num_traces())
sel_trace=[]
'''Multi trace Selection'''
inline=seismic.inline_numbers()
xline=seismic.xline_numbers()

print(inline,xline)
print(len(inline))
print(len(xline))
inline=np.array(inline)
xline=np.array(xline)
seis_vol=[]


for i in range(len(inline)-50):
    inline_start_index=inline[i]
    synthetic_seismic=np.zeros([len(seismic.trace_samples(1)),len(xline)])
    for j in range(len(xline)):
        xline_start_index=xline[j]
        tpl=(inline_start_index,xline_start_index)
        trace_index=seismic.trace_index(tpl)
        trace=seismic.trace_samples(trace_index)
        trace=np.array(trace) 
        t=np.arange(0,len(trace),1)
        synthetic_seismic[:,j]=trace
    seis_vol.append(synthetic_seismic)
print(seis_vol)
print(type(seis_vol))
seis_vol = np.array(seis_vol)
savemat("segpy.mat",{'arr': seis_vol})
