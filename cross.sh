#!/bin/sh
#SBATCH -N 1      # nodes requested
#SBATCH -n 10      # tasks requested
#SBATCH -c 10      # cores requested
#SBATCH --mem=64000  # memory in Mb
#SBATCH -o cross_out # send stdout to outfile
#SBATCH -e cross_err # send stderr to errfile
#SBATCH -t 23:00:00  # time requested in hour:minute:second
#SBATCH --job-name="X-Match"

python3 cross_matching.py
