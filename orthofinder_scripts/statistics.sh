#!/bin/bash
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH -t 48:00:00

module load slurm

for file in /expanse/lustre/projects/sio138/abigasin/orthofinder/orthofinder/sra/trinityoutput/*.Trinity.fasta
do
	echo $file
	perl /expanse/lustre/projects/sio138/sluglife/berghia_transcriptomes/ref_transcriptome/allstages_withbrain/calculate_basic_denovo_transcriptome_assembly_statistics.pl $file
done