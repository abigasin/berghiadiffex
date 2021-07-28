#!/bin/bash
#SBATCH --job-name=transdecoder
#SBATCH --partition=shared
#SBATCH --account=sio138
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH -t 48:00:00


module load slurm

#Transcriptome annotation
source /expanse/lustre/projects/sio138/shared/bashrc_files/tools.bashrc

for file in /expanse/lustre/projects/sio138/abigasin/orthofinder/orthofinder/sra/trinityoutput/*.Trinity.fasta
do
	echo $file
	TransDecoder.LongOrfs -t ${file}
	TransDecoder.Predict -t ${file}
done

