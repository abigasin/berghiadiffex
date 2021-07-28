import os
import numpy as np

mylist = os.listdir('/oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/trimmed')
mylist.sort()

os.chdir('/oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/trinityscripts')

for i in np.arange(1,len(mylist),2):
	start = mylist[i].split('_')[0]
	filename = "%s_trinity.sh" % start
	f = open(filename, 'w')
	stats = ['#!/bin/bash\n', '#SBATCH --job-name=trinity \n#SBATCH --time=48:00:00\n', '#SBATCH --cpus-per-task=16\n', 
				'#SBATCH --nodes=1\n', '#SBATCH --partition=large-shared \n#SBATCH --chdir=/scratch/$USER/$SLURM_JOBID\n', 
				'#SBATCH -A ddp370\n',"source /home/sluglife/.bash_profile\n", "module load gnu\nmodule load bowtie2 \nmodule load gnu/7.2.0\n\n"]
	lines = ['Trinity --seqType fq --max_memory 200G --left /oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/trimmed/',start,'_R1_trimmed.fq --right /oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/trimmed/',
				start,'_R2_trimmed.fq --CPU 16 --bflyHeapSpaceMax 10G --trimmomatic --output ',start,'_trinity --full_cleanup --verbose\n',
				'cp ', start, "* /oasis/projects/nsf/ddp370/abigasin/orthofinder/sra/trinityoutput"]
	f.writelines(stats)
	f.writelines(lines)
	f.close()