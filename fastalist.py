import glob

x = 1
txtfiles = []
for file in glob.glob("*.txt"):
    txtfiles.append(file)
print txtfiles

concat = ''.join([open(f).read() for f in txtfiles])
print concat

Filee = open("fasta_files"+str(x)+".txt","w")
Filee.write(concat)
