#sequenceingsPrimers

from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
import glob
import time
import csv
from itertools import izip

start = time.time()

file_string = ""    

fasta_files = []
for file in glob.glob("*.txt"):
    with open (file,'r')as fl:
        for aline in fl.readlines():
            if aline.startswith('>')==True:
                fasta_files.append(file)
print fasta_files


with open("output.txt", "w") as File:
    results = []
    for i in fasta_files:
        f_file = open(i)
        fasta_string = f_file.read()  # or make the names fasta1.fasta and just do open(i).read
        f_file.close()
        result_handle = NCBIWWW.qblast("blastn", "nr", fasta_string, hitlist_size=5)

        blast_records = NCBIXML.read(result_handle)  # if you only have one seq in file

        for alignment in blast_records.alignments:
            for hsp in alignment.hsps:
                file_string += "File:" + str(i) + "\n"
                file_string += "alignment:" + str(alignment.title)+"\n"
                file_string += "e-value:" + str(hsp.expect)+"\n"
        results.append(file_string)
        file_string = ""
        print i
    File.writelines(results)
#txttocsv


l=[]
fil=[]
ali=[]
e=[]
vals =[]


with open('output.txt','r') as f:
    for line in f:
        val = line.strip()
        vals.append(val.split('\n'))
        fil = vals[0::3]
        ali = vals[1::3]
        e = vals[2::3]


with open('blast.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('File', 'Alignment', 'E-value'))
    writer.writerows(izip(fil, ali, e))

    
end = time.time()
print(end - start)
