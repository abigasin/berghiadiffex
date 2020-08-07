import numpy as np
import pandas as pd
import Bio
import sys
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import os

class blast():
	def __init__(self):
		self.genespath = None
		self.output = None
		self.genes = None
		self.records = None
		self.newlist = None
	def readfile(self,dat):
		df = pd.read_csv(dat)
		self.output = df.loc[df['Variable']=='output']['Value'].iat[0]
		print("output location is " + self.output)
		self.fastapath = df.loc[df['Variable']=='fastapath'].Value.iat[0]
		self.db= df.loc[df['Variable']=='database'].Value.iat[0]
		#What genes do you what to look at?
		#self.genespath = df.loc[df['Variable']=='genespath'].Value.iat[0]
		#self.genes = pd.read_csv(self.genespath, header = None)
	def find_sequences(self,fastapath,genes):
		print('You have '+str(len(genes))+' genes of interest.')
		self.records = SeqIO.parse(self.fastapath, "fasta")
		transcripts = np.array([])
		for i in self.records:
			transcripts = np.append(transcripts, i.id)
		transcripts = pd.Series(transcripts)
		self.newlist = np.array([])
		for i in genes:
			bool=transcripts.str.contains(i,regex=False)
			transcripts_needed = transcripts.loc[bool]
			self.newlist = np.append(self.newlist, transcripts_needed.values)
		print('You have '+str(len(self.newlist))+' sequences of interest.')
	def execute_blast(self,records,output,newlist):
   		os.chdir(output)
   		self.records = SeqIO.index(self.fastapath, "fasta")
   		for i in np.arange(len(self.newlist)):
   			print("Blasting gene " + self.newlist[i]+ " against the "+ self.db+" database.")
   			result_handle = NCBIWWW.qblast('blastx',self.db,self.records[self.newlist[i]].seq,format_type='Text',hitlist_size=15,expect=0.0001,entrez_query='metazoa[Organism]')
   			with open('{0}_result_handle.txt'.format(self.newlist[i]),'w') as f:
   				f.write('Gene: '+ self.newlist[i]+'\n\n\n')
   				f.write('Seq:\n'+self.records[newlist[i]].format('fasta'))
   				f.write(result_handle.read())
if __name__=="__main__":
	dat = blast()
	print('\n...\n...\n...\n...\n...\n')
	print("Reading in config file...")
	dat.readfile(sys.argv[1])
	print("Finding sequences to blast...")
	#dat.find_sequences(dat.fastapath,self.genes[0])
	print("Blasting against NCBI database...")
	dat.execute_blast(dat.records,dat.output,dat.newlist)