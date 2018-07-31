#supersmartblast

from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
import glob
import time
import csv
from itertools import izip

x=1

for file in glob.glob("*.txt"):
    with open("Blastn_XML"+str(x)+".xml", "w") as output_xml:
        fasta_sequence = open(file,"r").read()
        if fasta_sequence.startswith(">"):
            print file , "blasting..."

            result_handle = NCBIWWW.qblast("blastn", "nr", fasta_sequence, hitlist_size=5)
            output_xml.write(result_handle.read())
            result_handle.close()

            x += 1

with open("AutoBlastn.csv", "wb") as output_csv:
    writer = csv.writer(output_csv, delimiter = ';')
    writer.writerow(['File ','Title', 'Length','E-value'])
    for one_xml in glob.glob("*.xml"):
        with open(one_xml, "r") as result_handle:
            blast_records = NCBIXML.read(result_handle)
            blast_record = next(blast_records)

            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    writer.writerow([str("file"), str(alignment.title), str(alignment.length), str(hsp.expect)])
