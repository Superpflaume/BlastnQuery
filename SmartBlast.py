#smartblast

from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
import glob
import time
import csv
from itertools import izip

start = time.time()

with open("BLASToutput.csv", "w") as output:
    results = []
    fasta_files = []
    for file in glob.glob('*.txt'):
        with open (file,'r')as fasta_sequence:
            for first_line in fasta_sequence.read():
                if first_line.startswith('>')==True:
                    print file
                    sequence = fasta_sequence.read()
                    print sequence
                    result_handle = NCBIWWW.qblast("blastn", "nr", sequence, hitlist_size=5)
                    #blast_records = NCBIXML.read(result_handle)  # if you only have one seq in file

                    output.write(result_handle.read())




end = time.time()
print(end - start)
