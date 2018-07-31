#smartblast

from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
import glob
import time
import csv
from itertools import izip

start = time.time()

with open("BLASToutputPARSED.xml", "w") as output:
    for file in glob.glob("*.txt"):
        fasta_sequence = open(file,"r").read()
        if fasta_sequence.startswith(">"):            
            print file , "blasting..."
            result_handle = NCBIWWW.qblast("blastn", "nr", fasta_sequence, hitlist_size=5)

            output.write(result_handle.read())
            result_handle.close()
       
            print file, "done"

            end = time.time()
            print(end - start)
            
result_handle = open ("BLASToutputPARSED.xml","r")
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)

with open("BLAST.csv", "w") as output:
    writer = csv.writer(output, delimiter = ";")
    writer.writerow(["File ","Title", "Length","E-value"])
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            output.write(str(file) + ";")
            output.write(str(alignment.title)+ ";")
            output.write(str(alignment.length)+ ";")
            output.write(str(hsp.expect) + "\n")
        

