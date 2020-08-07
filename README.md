Code from differential gene expression analysis.

This code is intended to find the consensus between 
DESeq2, edgeR, and limma-voom then blast the genes 
of interest against the NCBI database.

_Usage:_
First run consexpression (the corrected code is provided, 
if you choose to use the official version, 
please use at your own risk.)
Edit the CONFIG\_tool.txt file in /consexpression/dao/ to fit your data.
run 
```python experiment.py /dao/CONFIG_tool.txt ``` 

Edit the CONFIG.txt file to the location of data and 
desired output locations.
