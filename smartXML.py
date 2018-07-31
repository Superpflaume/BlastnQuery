#SmartXML
from Bio.Blast import NCBIXML
import csv
from itertools import izip

result_handle = open ("BLASToutput.xml")
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)

with open("BLAST2.csv", "w") as output:
    writer = csv.writer(output, delimiter = ';')
    writer.writerow(['File ','Title', 'Length','E-value'])
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            writer.writerow([str(file), str(alignment.title), str(alignment.length), str(hsp.expect)])
        
