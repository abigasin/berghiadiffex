import numpy as np
import pandas as pd
import Bio
import sys
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import os


def readinpaths(self,file){

	df = pd.read_csv(file)
	self.output = df.loc[df['Variable']=='output']['Value'].iat[0]
	print("output location is " + output)
	
	
	self.fastapath = df.loc[df['Variable']=='fastapath'].Value.iat[0]
	
	#What genes do you what to look at?
	genespath = df.loc[df['Variable']=='genespath'].Value.iat[0]
	genes = pd.read_csv(genespath, header = None)
	
}




def find_sequences(self,fastapath){

	print('You have '+str(len(genes[0]))+' genes of interest.')

	self.records = SeqIO.parse(fastapath, "fasta")
	transcripts = np.array([])
	for i in records:
    transcripts = np.append(transcripts, i.id)
    
    
	transcripts = pd.Series(transcripts)
	self.newlist = np.array([])
	for i in genes[0]:
    bool = transcripts.str.contains(i,regex=False)
    transcripts_needed = transcripts.loc[bool]
    self.newlist = np.append(self.newlist, transcripts_needed.values)
   
	print('You have '+str(len(self.newlist))+' sequences of interest.')
 }
 
 
 def blast_sequences(self,records,output){
   	os.chdir(output)
	records = SeqIO.index(fastapath, "fasta")

	for i in np.arange(len(newlist)):
    	print("Blasting gene " + newlist[i]+ " against the NR database.")
    	with open('{0}_result_handle.txt'.format(newlist[i]),'w') as f:
    		f.write('Gene: '+ newlist[i]+'\n\n\n')
    		result_handle = NCBIWWW.qblast("blastx","nr",records[newlist[0]].seq,format_type = "Text")
    		f.write(result_handle.read())
    	
}