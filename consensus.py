import numpy as np
import pandas as pd
import os

class consensus():
	def readfile(self,dat):
		df = pd.read_csv(dat)
		self.output = df.loc[df['Variable']=='consexpressionfiles']['Value'].iat[0]
		self.output2 = df.loc[df['Variable']=='output']['Value'].iat[0]
	def find_sig(self,output):
		os.chdir(output)
		###DESeq 
		#Getting where pval < .01
		deseq= pd.read_csv('consexpression_DESeq.csv',sep='\t')
		self.deseqsig = deseq.loc[deseq['pval']<0.001]
		###edgeR
		self.edger = pd.read_csv('consexpression_edger.csv',sep='\t')
		#Getting where FDR < 0.001
		self.edgersig = self.edger.loc[self.edger['FDR']<0.001]
		###limma-voom
		limmavoom = pd.read_csv('consexpression_limmavoom.csv',sep='\t')
		#Getting where pval <0.001
		self.limmasig = limmavoom.loc[limmavoom['P.Value']<0.001]
		###EBSeq
		#ebseq = pd.read_csv('consexpression_EBSeq.csv',sep='\t')
		#Getting where x = DE
		#ebsig = ebseq.loc[ebseq['x']=='DE']
		###NOISeq
		#Currently non-functional
		###BaySeq
		#Currently non-functional

	def find_consensus(self):
			
		#Getting consensus
		deseqgenes = self.deseqsig['id'].tolist()
		edgergenes = self.edgersig.index.tolist()
		limmagenes = self.limmasig.index.tolist()
		#ebseqgenes = self.ebsig.index.tolist()
		#noigenes = noisig.index.tolist()
		data1 = set(deseqgenes).intersection(edgergenes)
		data2 = set(data1).intersection(limmagenes)
		#data3 = set(data2).intersection(ebseqgenes)
		#data4=set(data3).intersection(noigenes)
		self.consensus = np.array(list(data2))
		file = open("consensus.txt",'w')
		for i in self.consensus:
			file.write(''.join(i)+'\n')
		file.close()
	def find_upreg(self):
		#gives us the number of upregulated genes of the most significant points
		upreg = self.edgersig.loc[self.edgersig['logFC']<0]
		upreg = upreg[upreg.index.isin(self.consensus)]
		self.upreggenes = np.array(self.edger[self.edger.index.isin(upreg.index)].index)
		os.chdir(self.output2)
		fileupreg = open("upreg.txt",'w')
		for i in self.upreggenes:
			fileupreg.write(''.join(i)+'\n')
		fileupreg.close()
		
if __name__=="__main__":
	dat = consensus()
	dat.readfile('/Volumes/LaCie/Documents/SURF2020/Berghiadiffex/CONFIG.txt')
	print('Finding significant genes...')
	dat.find_sig('/Volumes/LaCie/Documents/SURF2020/Output')
	print('Finding consensus...')
	dat.find_consensus()
	print('Finding upregulated genes...')
	dat.find_upreg()
	