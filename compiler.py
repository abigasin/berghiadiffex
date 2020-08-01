#script to compile all 
import os
import numpy as np
import pandas as pd

os.chdir('/Volumes/LaCie/Documents/SURF2020/blastoutputs')
compiledfile = open('compiledhits.txt','w')

for filename in os.listdir(os.getcwd()):
    if filename.startswith("TRINITY"):
    	nam = str(os.getcwd())+'/'+filename
    	f = open(nam,'r')
    	all_lines = f.readlines()
    	print("Writing hits for "+all_lines[0])
    	compiledfile.write(all_lines[0])
    	lines = -1
    	for i in all_lines:
    		lines = lines +1
    	for k in np.arange(lines):
    		if "Sequences producing significant" in all_lines[k]:
    			for j in np.arange(k-1,k+20):
    				if "ALIGNMENTS" in all_lines[j]:
    					break
    				#elif "PREDICTED" in all_lines[j] or "hypothetical" in all_lines[j]:
    				#	pass
    				else: 
    					compiledfile.write(all_lines[j])
    			compiledfile.write('\n\n\n')
    			f.close()
    			break
    		elif "No significant similarity" in all_lines[k]:
    			compiledfile.write("No significant similarity found.\n\n\n")


###Removing predicted and hypothetical
compiledfileNoPH = open('compiledfileNoPH.txt','w')    			
for filename in os.listdir(os.getcwd()):
    if filename.startswith("TRINITY"):
    	nam = str(os.getcwd())+'/'+filename
    	f = open(nam,'r')
    	all_lines = f.readlines()
    	print("Writing hits for "+all_lines[0])
    	compiledfileNoPH.write(all_lines[0])
    	lines = -1
    	for i in all_lines:
    		lines = lines +1
    	for k in np.arange(lines):
    		if "Sequences producing significant" in all_lines[k]:
    			for j in np.arange(k-1,k+20):
    				if "ALIGNMENTS" in all_lines[j]:
    					break
    				elif "PREDICTED" in all_lines[j] or "hypothetical" in all_lines[j]:
    					pass
    				else: 
    					compiledfileNoPH.write(all_lines[j])
    			compiledfileNoPH.write('\n\n\n')
    			f.close()
    			break
    		elif "No significant similarity" in all_lines[k]:
    			compiledfileNoPH.write("No significant similarity found.\n\n\n")