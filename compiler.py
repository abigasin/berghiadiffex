#script to compile all 
import os
import numpy as np
import pandas as pd
class comp():
	def compiler(self,output):
		os.chdir(output)
		compiledfile = open('compiledhits.txt','w')
		upregf = open('upreg.txt','r')
		upregdata = upregf.readlines()
		ul = 0
		for u in upregdata:
			ul = ul+1
		for filename in os.listdir(os.getcwd()):
			if filename.startswith("TRINITY"):
				nam = str(os.getcwd())+'/'+filename
				f = open(nam,'r')
				all_lines = f.readlines()
				print("Writing hits for "+all_lines[0])
				compiledfile.write(all_lines[0])
				#genename = all_lines[0][6:]
				#print(genename)
				upreg=False
				for x in np.arange(ul):
					if upregdata[x][:-1] in all_lines[0]:
						upreg=True
						break
				if upreg == True:
					compiledfile.write('\nUpregulated\n')
				else:
					compiledfile.write('\nDownregulated\n')
				lines = 0
				for i in all_lines:
					lines = lines +1
				for k in np.arange(lines):
					if "Length=" in all_lines[k]:
						compiledfile.write(all_lines[k])
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

if __name__=="__main__":
	dat = comp()
	dat.compiler('/Volumes/LaCie/Documents/SURF2020/blastoutputs')