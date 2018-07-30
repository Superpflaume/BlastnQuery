#smartblast

from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
import glob
import time
import csv
from itertools import izip

start = time.time()

with open("BLASToutput.csv", "w") as output:
    for file in glob.glob('*.txt'):
        fasta_sequence = open(file,'r').read()
        if fasta_sequence.startswith('>')==True:
            print file
            
            result_handle = NCBIWWW.qblast("blastn", "nr", fasta_sequence, hitlist_size=5)
            #blast_records = ''
            #blast_records = NCBIXML.read(result_handle)
            #print blast_records
            output.write(result_handle.read())
            result_handle.close()
            #fasta_sequence.close()
            print "next"



end = time.time()
print(end - start)
