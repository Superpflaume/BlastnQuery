#sequenceingsPrimersC

from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
import glob
import time

start = time.time()
  
x = 1
fasta_files = []
for file in glob.glob("*.txt"):
    fasta_files.append(file)
print fasta_files

for i in fasta_files:
    File = open("output"+str(x)+".txt","w")
    fasta_string = open(i).read() #or make the names fasta1.fasta and just do open(i).read
    result_handle = NCBIWWW.qblast("blastn", "nr", fasta_string, hitlist_size=5)

    print result_handle
    #blast_records = NCBIXML.parse(result_handle) 
    blast_records = NCBIXML.read(result_handle)# if you only have one seq in file
    print blast_records
    
    E_VALUE_THRESH = 0.001
    #for blast_record in blast_records:
    for alignment in blast_records.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                File.write("alignment:",alignment.title)
                File.write("e-value:",hsp.expect)
    x += 1
    print "file" 

end = time.time()
print(end - start)

