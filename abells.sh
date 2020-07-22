#!/bin/sh
#SBATCH -N 1      # nodes requested
#SBATCH -n 1      # tasks requested
#SBATCH -c 20      # cores requested
#SBATCH --mem=64000  # memory in Mb
#SBATCH -o abells_out # send stdout to outfile
#SBATCH -e abells_err # send stderr to errfile
#SBATCH -t 23:00:00  # time requested in hour:minute:second
#SBATCH --job-name="fits image axes"

python PyBDSF.py
