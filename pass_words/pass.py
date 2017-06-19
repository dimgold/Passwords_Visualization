import sys
import csv

passfile  = open('cleanedpass.csv', "rb")
wordsfile = open('words.csv', "rb")
j = 0
i = 0
dic1 = {}
dic2 = {}

for row1 in passfile:
    p = row1.split()[0]
    for char in p:
        if dic1.has_key(char):
            dic1[char] +=1
        else:
            dic1[char] = 1
        
    
for row2 in wordsfile:
    w = row2.split()[0]
    for char in w:
        if dic2.has_key(char):
            dic2[char] +=1
        else:
            dic2[char] = 1    
    


print dic1
print dic2



passfile.close()
wordsfile.close()