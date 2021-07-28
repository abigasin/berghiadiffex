#!/bin/bash
#SBATCH --job-name=grant_transcriptome
#SBATCH --partition=shared
#SBATCH --account=sio138
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH -t 48:00:00

module load slurm

perl /expanse/lustre/projects/sio138/sluglife/berghia_transcriptomes/ref_transcriptome/allstages_withbrain/calculate_basic_denovo_transcriptome_assembly_statistics.pl /expanse/lustre/projects/sio138/abigasin/orthofinder/orthofinder/sra/grants_transcriptome/mantle.cf.fasta

#Transcriptome annotation
source /expanse/lustre/projects/sio138/shared/bashrc_files/tools.bashrc

TransDecoder.LongOrfs -t /expanse/lustre/projects/sio138/abigasin/orthofinder/orthofinder/sra/grants_transcriptome/mantle.cf.fasta
TransDecoder.Predict -t /expanse/lustre/projects/sio138/abigasin/orthofinder/orthofinder/sra/grants_transcriptome/mantle.cf.fasta

source /expanse/lustre/projects/sio138/shared/bashrc_files/conda.bashrc
conda activate busco
cd /expanse/lustre/projects/sio138/abigasin/orthofinder/orthofinder/sra/grants_transcriptome/

busco -m transcriptome -i mantle.cf.fasta -l /expanse/lustre/projects/sio138/shared/tools/busco_downloads/mollusca_odb10 -o mantle.cf.fasta_trinity.Trinity_mollusca.v4.0.5 -f -c 8
busco -m transcriptome -i mantle.cf.fasta -l /expanse/lustre/projects/sio138/shared/tools/busco_downloads/metazoa_odb10 -o mantle.cf.fasta_trinity.Trinity_mollusca.v4.0.5 -f -c 8
