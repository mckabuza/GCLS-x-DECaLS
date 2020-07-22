#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 23:03:08 2020

@author: Kabelo McKabuza
"""

from astropy.io import fits
import glob

image_file = []
for file in glob.glob("*.fits"):
    image_file.append(file)

for image in image_file:
    image = str(image)
    hdu_list = fits.open(image)
    hdu = hdu_list[0].data[0,0,:,:]

    fits.writeto('./axis_fixed/{}'.format(image), hdu, hdu_list[0].header, overwrite=True)
