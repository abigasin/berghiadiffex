import numpy as np
import pandas as pd
import os
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

class consensus():
	def readfile(self,dat):
		df = pd.read_csv(dat)
		self.output = df.loc[df['Variable']=='consexpressionfiles']['Value'].iat[0]
		self.output2 = df.loc[df['Variable']=='output']['Value'].iat[0]
		self.go = df.loc[df['Variable']=='gofile']['Value'].iat[0]
	def find_sig(self,output):
		os.chdir(output)
		###DESeq 
		#Getting where pval < .01
		deseq= pd.read_csv('consexpression_DESeq.csv',sep='\t')
		deseq = deseq.dropna()
		self.deseqsig = deseq.loc[deseq['pval']<0.001]
		if len(np.asarray(self.deseqsig['id']))<10 :
			self.deseqsig = deseq.loc[deseq['pval']<0.05]
		###edgeR
		self.edger = pd.read_csv('consexpression_edger.csv',sep='\t')
		#Getting where FDR < 0.001
		self.edgersig = self.edger.loc[self.edger['FDR']<0.001]
		if len(np.asarray(self.edgersig['FDR'])) < 10:
			self.edgersig = self.edger.loc[self.edger['PValue']<0.001]
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
		
		#make venn diagram
		x = venn3([set(deseqgenes),set(edgergenes),set(limmagenes)],set_labels=('DESeq','edgeR',
		'limma-voom'))
		plt.title('Consensus of Differentially Expressed Genes')
		plt.savefig('consensus.png')
		plt.close()
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
	def find_go(self):
		os.chdir(self.output)
		go = pd.read_csv(self.go,sep='\t')
		go = go[go['#gene_id'].isin(self.consensus)]
		go = go[['#gene_id','gene_ontology_BLASTX']]
		for i in np.arange(len(np.asarray(go['#gene_id']))):
			go['gene_ontology_BLASTX'].iloc[i]=go['gene_ontology_BLASTX'].iloc[i].split('`',1)[0]
			go['gene_ontology_BLASTX'].iloc[i]=go['gene_ontology_BLASTX'].iloc[i][30:]
		prop = go['gene_ontology_BLASTX'].value_counts()
		prop = prop.to_frame()
		self.prop = prop.rename(index={'':'Unknown'})
		#print(prop)
		#finding upregulated 
		goupreg = go[go['#gene_id'].isin(self.upreggenes)]
		goupreg = goupreg['gene_ontology_BLASTX'].value_counts()
		goupreg = goupreg.to_frame()
		self.goupreg = goupreg.rename(index={'':'Unknown'})
		#finding downregulated
		godownreg = go[np.logical_not(go['#gene_id'].isin(self.upreggenes))]
		godownreg = godownreg['gene_ontology_BLASTX'].value_counts()
		godownreg = godownreg.to_frame()
		self.godownreg = godownreg.rename(index={'':'Unknown'})
		'''plt.rcParams['figure.figsize']=[10,6]
		prop.iloc[1:].plot(kind='barh',subplots=True,legend=False,fontsize=6)
		plt.title('GO Annotations Proportions in Differentially Expressed Genes Without Unknown')
		plt.invert_yaxis()
		plt.tight_layout()
		plt.savefig('GOannotations_{0}.png'.format(self.count))
		plt.close()
		#plt.subplots_adjust(left = .1,right = .9)
		plt.rcParams['figure.figsize']=[10,6]
		prop.plot(kind='barh',subplots=True,legend=False,fontsize=6)
		plt.title('GO Annotations Proportions in Differentially Expressed Genes')
		plt.tight_layout()
		plt.invert_yaxis()
		plt.title('GO Annotations Proportions in Differentially Expressed Genes')
		plt.savefig('GOannotations1.png')
		plt.close()
		#print(go.iloc[1]['gene_ontology_BLASTX'])'''
		
	def create_plots(self,kind,prop,nam):
		self.count = self.count+1
		plt.rcParams['figure.figsize']=[10,6]
		prop.iloc[1:].plot(kind=kind,subplots=True,legend=False,fontsize=6)
		plt.title('GO Annotations Proportions in Differentially Expressed Genes Without Unknown {0}'.format(nam))
		plt.tight_layout()
		plt.gca().invert_yaxis()
		plt.xlabel('Percent')
		plt.savefig('GOannotations_{0}.png'.format(nam))
		plt.close()
		plt.rcParams['figure.figsize']=[10,6]
		prop.plot(kind='barh',subplots=True,legend=False,fontsize=6)
		plt.tight_layout()
		plt.gca().invert_yaxis()
		plt.title('GO Annotations Proportions in Differentially Expressed Genes {0}'.format(nam))
		plt.xlabel('Percent')
		plt.savefig('GOannotations_{0}_2.png'.format(nam))
		plt.close()
		
if __name__=="__main__":
	dat = consensus()
	dat.readfile('/Volumes/LaCie/Documents/SURF2020/Berghiadiffex/CONFIG.txt')
	print('Finding significant genes...')
	dat.find_sig('/Volumes/LaCie/Documents/SURF2020/Output')
	print('Finding consensus...')
	dat.find_consensus()
	print('Finding upregulated genes...')
	dat.find_upreg()
	dat.count = 0
	dat.find_go()
	dat.create_plots('barh', dat.prop,'all_genes')
	dat.create_plots('barh', dat.goupreg,'upreg')
	dat.create_plots('barh',dat.godownreg,'downreg')
	