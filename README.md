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

Edit the ```CONFIG.txt``` file within the berghiadiffex to the location of consexpression data and 
desired blast results output locations.
In the configuration text file, ensure there are NO spaces after the comma and after the value.

consexpressionfiles - The location of the output for the consexpression program.
fastapath - the location of the tab-delimited file with the gene names and sequences.
output - the location where you want blast outputs to be saved.
database - which NCBI database to search against.
search - which type of blast search you want done (i.e. blastx)
gofile - tab-delimited gene annotations file from trinotate. 

then run
```python main.py /path/to/CONFIG.TXT```

In the original consexpression output folder, this program will add... 

```consensus.txt``` - has the consensus of differentially expressed genes across DESeq, edgeR, and limma-voom.
```upreg.txt``` - has the consensus of upregulated genes of the first tissue type listed in the ```CONFIG_tool.txt``` file
```compdata.csv``` - This will only exist if a trinotate file is listed. 
It will contain the consensus of diffex genes, whether or not they're upregulated based on edgeR, 
their gene ontology term, and other statistical values based on edgeR.

In the blastoutput folder specified in ```CONFIG.txt```, all result handles for the blast searches will be 
saved there. These result handles will also include the sequence of the transcript.
```compiledhits.txt``` will also be created, which contains the name, length, whether or not it is upregulated 
or downregulated and blast hits (or lack thereof) of the every diffex gene given in a single file. 


For further assistance on how to design primers for in-situ hybridization probes, please read 
```primerdesignhelp.txt```

The consexpression package is from https://costasilvati.github.io/consexpression/.

Costa-Silva J, Domingues D, Lopes FM. RNA-Seq differential expression analysis: An extended review and a software tool. PLoS One. 2017 Dec 21;12(12):e0190152. doi: 10.1371/journal.pone.0190152. PMID: 29267363; PMCID: PMC5739479.