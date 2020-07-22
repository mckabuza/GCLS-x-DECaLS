#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:04:50 2020

@author: kabelo
"""

import bdsf
import glob

input_images = []
for image in glob.glob("*.fits"):
    input_images.append(image)

for input_image in input_images:
    img = bdsf.process_image(input_image, rms_box=(20,10))

    img.write_catalog('./AbellOutput/',format='fits', catalog_type='srl')
    img.export_image('./AbellOutput/',img_type='gaus_resid')
    img.export_image('./AbellOutput/',img_type='gaus_model', outfile=input_image+'.model')

































