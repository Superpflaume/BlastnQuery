#SmartXML
from Bio.Blast import NCBIXML
import csv
from itertools import izip

result_handle = open ("BLASToutput.xml")
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)

header = ['File ;','Title;', 'Length;','E-value \n']
i = 0
with open("BLAST.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerow(i for i in header)
    #output.write(i for i in header)
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            fil = str(file) + ';' 
            tit = str(alignment.title)+ ';'
            leng = str(alignment.length)+ ';' 
            val = str(hsp.expect)+ ';' + '\n'

            output.write(fil)
            output.write(tit)
            output.write(leng)
            output.write(val)

    
    #writer.writerow(('File', 'Alignment', 'E-value'))
#writer.writerows(izip(fil, ali, e))
