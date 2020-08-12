Code from differential gene expression analysis.

This code is intended to find the consensus between 
DESeq2, edgeR, and limma-voom then blast the genes 
of interest against the NCBI database.

_Usage:_

Necessary tools:
Python, R

In R, have installed limma-voom, DESeq, and edgeR.

In python, have installed rpy2, pandas, numpy, matplotlib.

First run consexpression (the corrected code is provided, 
if you choose to use the official version, 
please use at your own risk.) Go to the consexpression folder in terminal.
Edit the CONFIG\_tool.txt file in /consexpression/dao/ to fit your data needs.
run 
```python experiment.py /dao/CONFIG_tool.txt ``` 

Edit the CONFIG.txt file to the location of data and 
desired output locations.
In the configuration text file, ensure there are NO spaces after the comma and after the value.

consexpressionfiles - The location of the output for the consexpression program.
fastapath - the location of the tab-delimited file with the gene names and sequences.
output - the location where you want blast outputs to be saved.
database - which NCBI database to search against, keep nr for now as the program only performs blastx.
gofile - tab-delimited gene annotations file. 



Then, go to the Berghiadiffex folder and edit CONFIG.txt to your needs. Currently, the program only performs blastx.
then run
```python main.py /path/to/CONFIG.TXT```


