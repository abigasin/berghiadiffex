##Creating fastp files

import os
import numpy as np

mylist = os.listdir('/oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/fastq')
mylist.sort()

os.chdir('/oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/fastpfiles')

for i in np.arange(1,len(mylist),2):
	start = mylist[i].split('_')[0]
	filename = "%s.sh" % start
	f = open(filename, 'w')
	stats = ['#!/bin/bash\n', '#SBATCH --time=48:00:00\n', '#SBATCH --cpus-per-task=4\n', '#SBATCH --nodes=1\n', '#SBATCH --partition=shared\n', '#SBATCH -A ddp370\n',"source /home/sluglife/.bash_profile\n", "module load gnu\n"]
	lines = ['fastp --in1 /oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/fastq/', mylist[i-1], ' --out1 /oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/fastq/', start, '_R1_trimmed.fq --in2 /oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/fastq/', mylist[i], ' --out2 /oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/fastq/' ,start,'_R2_trimmed.fq']
#	lines2 = ['insilico_read_normalization.pl --seqType fq --JM 500G --left Berghia_alltissues_onerep_R1_trimmed.fq.gz --right Berghia_alltissues_onerep_R2_trimmed.fq.gz --max_cov 100 --CPU 32 --PARALLEL_STATS --pairs_together']
	f.writelines(stats)
	f.writelines(lines)
	f.close()
