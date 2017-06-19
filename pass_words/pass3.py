import csv

for d in range(12):
    passfile  = open('cleanedpass.csv', "rb")
    LOCS = []
    print LOCS
    for row1 in passfile:
        p = row1.split()[0]
        if len(p)>d+1:
            LOCS.append(p[d])
          
    
    print LOCS[:50] 
    passfile.close()
    text_file = open("out/"+str(d+1)+".txt", "w")
    text_file.write(" ".join(LOCS))
    text_file.close()
    print d

