#SmartXML
from Bio.Blast import NCBIXML

result_handle = open ("BLASToutput.xml")
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)

with open("BLASToutputPARSED.xml", "w") as output:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            a = str(file)
            b = "sequence:" + str(alignment.title)
            c = "length:" + str(alignment.length)
            d = "e value:" + str(hsp.expect)
            output.write(a)
            output.write(b)
            output.write(c)
            output.write(d)
