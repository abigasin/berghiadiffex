import numpy as np
import pandas as pd
import os

#DEseq 
def deseqsig(self)
	deseq= pd.read_csv('consexpression_DESeq.csv',sep='\t')
	deseq.head()
	#Getting where pval < .01
	deseqsig = deseq.loc[deseq['pval']<0.001]
