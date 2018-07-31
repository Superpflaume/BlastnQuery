#SmartXML

from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
import glob
import time
import csv
from itertools import izip



with open("BLAST2.csv", "wb") as output_csv:
    writer = csv.writer(output_csv, delimiter = ';')
    writer.writerow(['File ','Title', 'Length','E-value'])
    for xml in glob.glob("*.xml"):
        with open(xml, "r") as result_handle:
            blast_records = NCBIXML.parse(result_handle)
            blast_record = next(blast_records)

            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    writer.writerow([str("file"), str(alignment.title), str(alignment.length), str(hsp.expect)])
