#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:27:26 2020

@author: Kabelo McKabuza
"""

from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.table import Table
import matplotlib.pyplot as plt
import fnmatch
import os
from matplotlib import rcParams
import numpy as np

rcParams['font.size'] = '16'
#rcParams['font.family'] = 'Courier New'

zField_tables=[]
for file in os.listdir('./zFieldOutput'):
    if fnmatch.fnmatch(file, '*.fits'):
        zField_tables.append(file)

pybdsf_tables=[]
for file in os.listdir('./Catalogs'):
    if fnmatch.fnmatch(file, '*.fits'):
        pybdsf_tables.append(file)

matched_fits = []
for i in zField_tables:
    for j in pybdsf_tables:
        if i.split('_zField')[0] == j.split('.Fix')[0] or i.split('_zField')[0] == j.split('.1pln')[0] or i.split('_zField')[0] == j.split('_1pln')[0]:
            matched_fits.append(j)
            #print('zField Tables: \n' + i)
            #print('PyBDSF Tables: \n' + j)

            zField_decals = Table.read('./zFieldOutput/{}'.format(i))
            pybdsf_sources = Table.read('./Catalogs/{}'.format(j))

            pybdsf_sources['Total_flux']=pybdsf_sources['Total_flux'].to(u.uJy)
            pybdsf_sources['E_Total_flux']=pybdsf_sources['E_Total_flux'].to(u.uJy)
            pybdsf_sources['Peak_flux']=pybdsf_sources['Peak_flux'].to(u.uJy/u.beam)
            pybdsf_sources['E_Peak_flux']=pybdsf_sources['E_Peak_flux'].to(u.uJy/u.beam)
            pybdsf_sources.rename_columns(['Total_flux', 'Peak_flux', 'E_Total_flux', 'E_Peak_flux'],
                                          ('Total_flux (uJy)', 'Peak_flux (uJy/beam)', 'E_Total_flux (uJy)', 'E_Peak_flux (uJy/beam)'))

            zField_coord = SkyCoord(ra=zField_decals['RADeg']*u.degree, dec=zField_decals['decDeg']*u.degree)
            pybdsf_coord = SkyCoord(ra=pybdsf_sources['RA'], dec=pybdsf_sources['DEC'])

            max_sep = 10*u.arcsec
            idx, d2d, d3d = pybdsf_coord.match_to_catalog_sky(zField_coord)
            d2d = d2d.to(u.arcsec)
            sep_constraint = d2d <= max_sep

            pybdsf_matches = pybdsf_coord[sep_constraint]
            zField_matches = zField_coord[idx[sep_constraint]]

            table_entries=[]
            for keys in zField_decals.keys():
                table_entries.append(zField_decals[keys][idx[sep_constraint]])

            pybdsf_keys = ['RA', 'E_RA', 'DEC', 'E_DEC', 'Total_flux (uJy)', 'E_Total_flux (uJy)', 'Peak_flux (uJy/beam)', 'E_Peak_flux (uJy/beam)']
            names = zField_decals.keys()

            for key in pybdsf_keys:
                table_entries.append(pybdsf_sources[key][sep_constraint])
                names.append(key)

            matched = Table(table_entries, names=tuple(names))
            matched.write('./Matches/{}-DECaLS.fits'.format(j.split('.pybdsm')[0]), overwrite=True)

            fig = plt.figure(figsize=(10,10))

            plt.title('{}-DECaLS cross-match'.format(j.split('.1pln')[0]))
            plt.hist(d2d, histtype='step', range=(0,10), lw=2, label='Total matches: {}'.format(len(pybdsf_matches)))
            plt.legend(loc='best')
            plt.ylabel('No. of matches')
            plt.xlabel('Separation (arcsec)')
            plt.xticks(np.arange(1,11,1))
            plt.savefig('./Matches/{}.png'.format(j.split('.pybdsm')[0]))

print('zField catalogs: {}\n'.format(len(zField_tables)) +
      'Cross-matched: {}'.format(len(matched_fits)))
#print(sorted(matched_fits))