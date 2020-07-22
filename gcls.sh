#!/bin/sh
#SBATCH -N 1      # nodes requested
#SBATCH -n 10      # tasks requested
#SBATCH -c 2      # cores requested
#SBATCH --mem=64000  # memory in Mb
#SBATCH -o zfield_out # send stdout to outfile
#SBATCH -e zfield_err # send stderr to errfile
#SBATCH -t 23:00:00  # time requested in hour:minute:second
#SBATCH --job-name="zField:)"


srun --ntasks=1 zField J0416.7-5525 64.18666667 -55.41916667 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &

srun --ntasks=1 zField J0510.2-4519 77.64041667 -45.32277778 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &
srun --ntasks=1 zField J0516.6-5430 79.15583333 -54.50041667 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &

srun --ntasks=1 zField J0528.9-3927 82.23416667 -39.46361111 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &
srun --ntasks=1 zField J0542.8-4100 85.70791667 -40.99944444 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &

srun --ntasks=1 zField J0610.5-4848 92.63333333 -48.80722222 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &
srun --ntasks=1 zField J0637.3-4828 99.3256471 -48.4839993 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &

srun --ntasks=1 zField J0638.7-5358 99.70583333 -53.978 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &
#####################################
srun --ntasks=1 zField Abell_S295 41.39916667 -53.038 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &
srun --ntasks=1 zField MACSJ_0025.4-1222B 6.37242083 -12.37696111 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &

srun --ntasks=1 zField MACSJ0417.5-1154 64.39416667 -11.90888889 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &
srun --ntasks=1 zField J0117.8-5455 19.46041667 -54.92388889 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &

srun --ntasks=1 zField J0217.2-5244 34.3293818 -52.7182565 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &
srun --ntasks=1 zField J0225.9-4154 36.4623777 -41.9213823 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &

srun --ntasks=1 zField J0232.2-4420 38.077875 -44.34486111 -r 1.5 -c /data/mjh/shared-meerkat/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &
srun --ntasks=1 zField PLCK_G200.9-28.2 72.587083 -2.949333 -r 1.2 -c /home/mckabuza/zCluster/zCluster/DECaLSCache/ -o /data/mckabuza/MeerKAT/GCLS/zFieldOutput/ -t testTemplates/COSMOScustom2PlusAGNs -E 0.02 &
wait
