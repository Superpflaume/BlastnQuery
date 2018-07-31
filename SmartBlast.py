#smartblast

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
            #result_handle.close()

            end = time.time()
            print(end - start)
            x += 1
            
#result_handle = open ("BLASToutputPARSED.xml","r")
#blast_records = NCBIXML.parse(result_handle)
            blast_records = NCBIXML.read(result_handle)
            blast_record = next(blast_records)

            with open("BLAST.csv", "w") as output_csv:
                writer = csv.writer(output_csv, delimiter = ";")
                writer.writerow(["File ","Title", "Length of alignment","E-value"])
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        output_csv.write(str(file) + ";")
                        output_csv.write(str(alignment.title)+ ";")
                        output_csv.write(str(alignment.length)+ ";")
                        output_csv.write(str(hsp.expect) + "\n")
        

