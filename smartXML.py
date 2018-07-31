#SmartXML
from Bio.Blast import NCBIXML
import csv
from itertools import izip

result_handle = open ("BLASToutput.xml")
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)

with open("BLAST.csv", "w") as output:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            fil = str(file) + ';' 
            tit = str(alignment.title)+ ';'
            leng = str(alignment.length)+ ';' 
            val = str(hsp.expect)+ ';' + '\n'

            writer = csv.writer(output)
            writer.writerow(('File', 'Title', 'Length', 'E-value'))

            output.write(fil)
            output.write(tit)
            output.write(leng)
            output.write(val)
