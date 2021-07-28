#!/bin/bash
#SBATCH --job-name=orthofinder
#SBATCH --partition=large-shared
#SBATCH --account=sio138
#SBATCH --ntasks-per-node=16
#SBATCH --nodes=1
#SBATCH -t 48:00:00
#SBATCH --output=output-%x.%j.out
#SBATCH --mem=50GB
source /expanse/lustre/projects/sio138/shared/bashrc_files/tools.bashrc

cd /expanse/lustre/projects/sio138/abigasin/orthofinder/orthofinder/sra/pepfiles


for f in *
do 
	python /expanse/lustre/projects/sio138/shared/tools/OrthoFinder/tools/primary_transcript.py $f 
done

orthofinder -f primary_transcripts/
