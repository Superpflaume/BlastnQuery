#smartblast

from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
import glob
import time
import csv
from itertools import izip

start = time.time()

with open("BLASToutputPARSED.xml", "w") as output:
    for file in glob.glob('*.txt'):
        fasta_sequence = open(file,'r').read()
        if fasta_sequence.startswith('>')==True:            
            result_handle = NCBIWWW.qblast("blastn", "nr", fasta_sequence, hitlist_size=5)

            blast_records = NCBIXML.read(result_handle)

            for alignment in blast_records.alignments:
                for hsp in alignment.hsps:
                    a = str(file)
                    b = "sequence:" + str(alignment.title)
                    c = "length:" + str(alignment.length)
                    d = "e value:" + str(hsp.expect)
                    output.write(a)
                    output.write(b)
                    output.write(c)
                    output.write(d)

            result_handle.close()
       
            print"done:", file

end = time.time()
print(end - start)
            


