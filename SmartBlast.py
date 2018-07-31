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
            print file , "blasting..."
            result_handle = NCBIWWW.qblast("blastn", "nr", fasta_sequence, hitlist_size=5)

            output.write(result_handle.read())
            result_handle.close()
       
            print file, "done"

end = time.time()
print(end - start)
            
result_handle = open ("BLASToutput.xml")
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)

with open("BLAST.csv", "w") as output:
    output.write('File ;')
    output.write('Title;')
    output.write('Length;')
    output.write('E-value \n')
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
