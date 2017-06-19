
datap = read.table("pass.txt")
head(datap)
dim(datap)
 
install.packages("RMySQL")
library(RMySQL)

mydb = dbConnect(MySQL(), user='root', password='1234', dbname='password', host='localhost')
mydb = dbConnect(MySQL(), user='eztest', password='eztpass', dbname='password', host='173.194.228.96')
dbListTables(mydb)
dbListFields(mydb, 'passdata')
rs = dbSendQuery(mydb, 'SELECT 
    word, ss_type, gloss, Pass, locate(word,Pass) as location, length(word) as wordlen, length(Pass) as passlen
FROM
    wn_synset
        join
    wn_gloss ON wn_synset.synset_id = wn_gloss.synset_id
join 
(select passdata.Pass
from passdata) as p 
where length(word)>=3 and locate(word,Pass) > 0 and length(pass)>=6')



#dbSendQuery(mydb, 'drop table if exists some_table, some_other_table')
#dbWriteTable(mydb, name='passdata', value=data)

#rs = dbSendQuery(mydb, 'select * from entries')
#res = fetch(rs, n=-1)

addsubs <- function(data,start,end){
  for (i in 1:(length(data[,1]))){
    sub <- substr(data[i,1],start,end)
    
    if(value <= del[i]) {return (cat[i])
    }
  }
  return(cat[length(cat)])
}

lower


 raw = read.table("quatroslocs.csv", header = TRUE, sep =",")
 head(raw)

boxplot(location~quatro,data= raw)
g <- ggplot(raw, aes(quatro, location))


passplus = read.table("/pass_words/.csv", header = FALSE, sep =",")