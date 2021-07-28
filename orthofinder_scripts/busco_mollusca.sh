#!/bin/bash
#SBATCH --job-name=busco_mollusca
#SBATCH --partition=shared
#SBATCH --account=sio138
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH -t 48:00:00

module load slurm

#BUSCO statistics
source /expanse/lustre/projects/sio138/shared/bashrc_files/conda.bashrc
conda activate busco
cd /expanse/lustre/projects/sio138/abigasin/orthofinder/orthofinder/sra/trinityoutput/
for file in *.Trinity.fasta
do
	echo $file
	busco -m transcriptome -i ${file} -l /expanse/lustre/projects/sio138/shared/tools/busco_downloads/mollusca_odb10 -o ${file}_trinity.Trinity_mollusca.v4.0.5 -f -c 8
done