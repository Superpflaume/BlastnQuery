from Bio.Blast import  NCBIWWW
    # for online access to NCBI Blast
from Bio.Blast import NCBIXML
    # to read the Blast-results
import glob
    # to find all files in one folder
import csv
    # to write a csv which can be displayed by MS Excel

x=1

for file in glob.glob("*.txt"):
        # find all TXT-files in the folder, therefor all FASTA-sequences
    with open("BlastnSeq"+str(x)+".xml", "w") as output_xml: # generate an empty XML-document, one for each sequences results
        fasta_sequence = open(file,"r").read() # open FASTA-file and save sequence in variable "fasta_sequence"
        if fasta_sequence.startswith(">"): # eliminate all empty files
            print file , "blasting..." # status update

            result_handle = NCBIWWW.qblast("blastn", "nr", fasta_sequence, hitlist_size=5) # upload the sequence to NCBI Blast database, perform a "blastn" search for "somewhat similar sequences" to get results for every sample, and download the first 5 hits (to keep the results managable)
            output_xml.write(result_handle.read()) # write the results in the previously opened XML file
            result_handle.close() # close the previous search

            x += 1 # count up for the next XML-file to be opened

with open("AutoBlastn.csv", "wb") as output_csv:
        # generate an empty CSV-file to store the desired information about all
        # sequences
    writer = csv.writer(output_csv, delimiter = ';')
        # define a method how the data is to be written in the document
    writer.writerow(['File ','Title', 'Length','E-value'])
        # put a header for the document
    for one_xml in glob.glob("*.xml"):
            # find all XML-files in the folder that were previously generated
        with open(one_xml, "r") as result_handle:
                # open one XML-file after another and save information in
                # "result_handle"
            blast_records = NCBIXML.parse(result_handle)
                # make information from XML-file accessible by line
            blast_record = next(blast_records)
                # move trough lines of XML-file

            for alignment in blast_record.alignments:
                    # any line in the XML-file that...
                for hsp in alignment.hsps:
                        # ... includes information on the hit such as...
                    writer.writerow([str(file), str(alignment.title),
                    str(alignment.length), str(hsp.expect)])
                        # name of the TXT-file that was blasted,
                        # title of alignment, length of alignment and e-values
                        # of alignment is to be written in the CSV-file.
