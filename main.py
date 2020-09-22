import os
import pandas as pd
import numpy as np
import Bio
import sys
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Consensus import consensus
from blastgenes import blast
from compiler import comp
#main file to run
if __name__=="__main__":
	#finding consensus between all programs first
	cons = consensus()
	cons.readfile(sys.argv[1])
	print('Finding significant genes...')
	cons.find_sig(cons.output)
	print('Finding consensus...')
	cons.find_consensus()
	print('Finding upregulated genes...')
	cons.find_upreg()
	print('Finding GO terms and compiling data in csv...')
	if cons.go == '':
		print('No trinotate annotation file found, skipping this step...')
	else:
		cons.find_go()
	#blasting genes against ncbi database
	dat = blast()
	print('\n...\n...\n')
	print("Reading in config file...")
	dat.readfile(sys.argv[1])
	print("Finding sequences to blast...")
	dat.find_sequences(dat.fastapath,cons.consensus)
	print("Blasting against NCBI database...")
	dat.execute_blast(dat.records,dat.output,dat.newlist)
	compiler = comp()
	compiler.compiler(dat.output)