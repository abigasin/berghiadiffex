import numpy as np
import pandas as pd
import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import os
os.chdir('/Volumes/LaCie/Documents/SURF2020/blastoutput')


fastapath = '/Volumes/LaCie/Documents/SURF2020/Berghia_trinitygg_transdecoderlongestorfs_cdhit95_noaliens_subset.fasta'

#What genes do you what to look at?
genes = pd.read_csv('/Volumes/LaCie/Documents/SURF2020/Output/consensusDCPC.txt', header = None)

records = SeqIO.parse(fastapath, "fasta")
transcripts = np.array([])
for i in records:
    transcripts = np.append(transcripts, i.id)
    
transcripts = pd.Series(transcripts)
newlist = np.array([])
for i in genes[0]:
    bool = transcripts.str.contains(i,regex=False)
    transcripts_needed = transcripts.loc[bool]
    newlist = np.append(newlist, transcripts_needed.values)
    
records = SeqIO.index(fastapath, "fasta")

for i in np.arange(len(newlist)):
    print("Blasting gene " + newlist[i]+ " against the NR database.")
    with open('{0}_result_handle.txt'.format(newlist[i]),'w') as f:
    	f.write('Gene: '+ newlist[i]+'\n\n\n')
    	result_handle = NCBIWWW.qblast("blastn","nt",records[newlist[0]].seq,format_type = "Text")
    	f.write(result_handle.read())