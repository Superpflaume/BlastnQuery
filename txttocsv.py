#txttocsv
import csv
from itertools import izip

l=[]
fil=[]
ali=[]
e=[]
vals =[]


with open('output1.txt') as f:
    for line in f:
        val = line.strip()
        vals.append(val.split('\n'))
        fil = vals[0::3]
        ali = vals[1::3]
        e = vals[2::3]


with open('some.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('File', 'Alignment', 'E-value'))
    writer.writerows(izip(fil, ali, e))
    #writer.writerow(('File', 'Alignment', 'E-value'))
