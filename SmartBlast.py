#smartblast

from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
import glob
import time
import csv
from itertools import izip

start = time.time()

with open("BLASToutput.xml", "w") as output:
    for file in glob.glob('*.txt'):
        fasta_sequence = open(file,'r').read()
        if fasta_sequence.startswith('>')==True:            
            print file
            result_handle = NCBIWWW.qblast("blastn", "nr", fasta_sequence, hitlist_size=5)
    
            output.write(result_handle.read())
                #changeneeded
            result_handle.close()
       
            print"done:", file

            
result_handle = open("BLASToutput.xml")
blast_records = NCBIXML.parse(result_handle)

for alignment in blast_records.alignments:
    for hsp in alignment.hsps:
        print("****Alignment****")
        print("sequence:", alignment.title)
        print("length:", alignment.length)
        print("e value:", hsp.expect)

end = time.time()
print(end - start)
