import sys
import csv
import passwordmeter

passfile  = open('cleanedpass.csv', "rb")
#wordsfile = open('words.csv', "rb")
#writer = open('pass_strenght.csv', 'w')
charsw = open('charsloc.csv', 'w')
fields = ['char','loc','dens']
line = str(fields)[1:-1].replace(', ', ',').replace('\'', '')
j = 0
i = 0
passchars = {}
wordchars = {}
passdic = {}
words= []
charsloc ={}

for row1 in passfile:
    p = row1.split()[0]
    for i in range(len(p)):
        if charsloc.has_key((p[i],i+1)):
            charsloc[(p[i],i+1)]+=1
        else:
            charsloc[(p[i],i+1)] = 1
            
for c in charsloc:
    fields = [c[0],c[1],charsloc[c]]
    line = str(fields)[1:-1].replace(', ', ',').replace('\'', '')
    charsw.write(line + '\n')









    #print line
    #writer.write(line + '\n')
    '''if passdic.has_key(p):
        passdic[p] +=1
    else:
        passdic[p] = 1'
    for char in p:
        if passchars.has_key(char):
            passchars[char] +=1
        else:
            passchars[char] = 1
        
    
for row2 in wordsfile:
    w = row2.split()[0]
    words.append(w)
    for char in w:
        if wordchars.has_key(char):
            wordchars[char] +=1
        else:
            wordchars[char] = 1    
    

print passdic
print words
#print passchars
#print wordchars
'''
            
charsw.close()
#writer.close()
passfile.close()
#wordsfile.close()
print 'Done'