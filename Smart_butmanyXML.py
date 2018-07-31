#smartblast many xml

from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
import glob
import time
import csv
from itertools import izip

x=1

with open("BLASToutputPARSED"+str(x)+".xml", "w") as output:
    for file in glob.glob("*.txt"):
        fasta_sequence = open(file,"r").read()
        if fasta_sequence.startswith(">"):            
            print file , "blasting..."
            start = time.time()
            
            
            result_handle = NCBIWWW.qblast("blastn", "nr", fasta_sequence, hitlist_size=5)
            output.write(result_handle.read())
            result_handle.close()

            end = time.time()
            print(end - start)
            x += 1
