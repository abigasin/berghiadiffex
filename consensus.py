import numpy as np
import pandas as pd
import os
os.chdir('/Volumes/LaCie/Documents/SURF2020/Output/')

###DESeq 
#Getting where pval < .01
deseq= pd.read_csv('consexpression_DESeq.csv',sep='\t')
deseqsig = deseq.loc[deseq['pval']<0.001]

###edgeR
edger = pd.read_csv('consexpression_edger.csv',sep='\t')
#Getting where FDR < 0.001
edgersig = edger.loc[edger['FDR']<0.001]

###limma-voom
limmavoom = pd.read_csv('consexpression_limmavoom.csv',sep='\t')
#Getting where pval <0.001
limmasig = limmavoom.loc[limmavoom['P.Value']<0.001]

###EBSeq
ebseq = pd.read_csv('consexpression_EBSeq.csv',sep='\t')
#Getting where x = DE
ebsig = ebseq.loc[ebseq['x']=='DE']

###NOISeq
#Currently non-functional

###BaySeq
#Currently non-functional

#Getting consensus
deseqgenes = deseqsig['id'].tolist()
edgergenes = edgersig.index.tolist()
limmagenes = limmasig.index.tolist()
ebseqgenes = ebsig.index.tolist()
#noigenes = noisig.index.tolist()

data1 = set(deseqgenes).intersection(edgergenes)
data2 = set(data1).intersection(limmagenes)
#data3 = set(data2).intersection(ebseqgenes)
#data4=set(data3).intersection(noigenes)
consensus = np.array(list(data2))

file = open("consensusDCPC.txt",'w')
for i in consensus:
    file.write(''.join(i)+'\n')
file.close()

#This line gives us the number of upregulated genes of the most significant points

upreg = edgersig.loc[edgersig['logFC']<0]
upreg = upreg[upreg.index.isin(consensus)]
upreggenes = np.array(edger[edger.index.isin(upreg.index)].index)

fileupreg = open("DCupreg.txt",'w')
for i in upreggenes:
    fileupreg.write(''.join(i)+'\n')
fileupreg.close()