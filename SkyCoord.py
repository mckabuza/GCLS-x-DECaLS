#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:53:00 2020

@author: kabelo
"""

from astropy.coordinates import SkyCoord
import pandas as pd

sources = ['Abell 141', 'Abell S295', 'MACS J0025.4-1222', 'MACS J0417.5-1154', 'RXC J0510.7-0801',
           'RXC J0520.7-1328', 'RXC J0117.8-5455', 'RXC J0217.2-5244', 'RXC J0225.9-4154', 'RXC J0232.2-4420', 'RXC J0303.7-7752',
           'MCXC J0406.7-7116', 'MCXC J0416.7-5525', 'MCXC J0510.2-4519', 'MCXC J0516.6-5430', 'MCXC J0528.9-3927',
           'RDCS J0542-4100', 'MCXC J0610.5-4848', 'RXC J0637.3-4828', 'RXC J0638.7-5358', 'RXC J1423.7-5412']
# 'PLCK G200.9-28.2',
RADeg = []
decDeg = []
for source in sources:
    location = SkyCoord.from_name(source)
    RADeg.append(location.ra.deg)
    decDeg.append(location.dec.deg)
#print(location)


data = pd.DataFrame({'Cluster': sources, 'RADeg': RADeg, 'decDeg': decDeg})

data.to_csv(r'./GCLS_source_locations.csv', index=False)


