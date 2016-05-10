### go R

ht=aggregate(x$Answers, by=list(x$TopicID), FUN=sum)

ht=aggregate(x$Answers, by=list(x$TopicID, x$Year), FUN=mean)

ggplot(ht,aes(x=factor(Group.2), y=factor(Group.1), fill=x))+geom_tile()+theme_bw()+scale_fill_gradient2(midpoint=5, low="#3333cc", high="#ff3300", mid='#ffffff')+theme(axis.text.x = element_text(angle = 45, hjust = 1))






x=read.table('TOPICS.COUNTS.2.tsv', header=T, sep="\t")

names=as.vector(y$Topic.Name)

## Questions
#htx=aggregate(x$Questions, by=list(x$TopicID), FUN=sum)
#values=100*htx[,'x']/sum(htx[,'x'])
#rates=rep('Questions',length(values))

#X=cbind(names,rates,values)


## Answers
#htx1=aggregate(x[x$Answers>=1,]$Questions, by=list(x[x$Answers>=1,]$TopicID), FUN=sum)
#values=100*htx1[,'x']/htx[,'x']
#rates=rep('Answers',length(values))
#Y=cbind(names,rates,values)
#X=rbind(X,Y)



## REPLIED questions
htx1=aggregate(x[x$Answers>=1,]$Questions, by=list(x[x$Answers>=1,]$TopicID), FUN=sum)
values=100*htx1[,'x']/htx[,'x']
rates=rep('Replied',length(values))
#Y=cbind(names,rates,values)
#X=rbind(X,Y)
X=cbind(names,rates,values)


## RELEVANT questions
htx1=aggregate(x[x$Answers>=1 & x$UpCount>=1,]$Questions, by=list(x[x$Answers>=1 & x$UpCount>=1,]$TopicID), FUN=sum)
values=100*htx1[,'x']/htx[,'x']
rates=rep('Relevant',length(values))
Y=cbind(names,rates,values)
X=rbind(X,Y)


## unanswered
htx1=aggregate(x[x$Answers>=1 & x$UpCount==0,]$Questions, by=list(x[x$Answers>=1 & x$UpCount==0,]$TopicID), FUN=sum)
values=100*htx1[,'x']/htx[,'x']
rates=rep('Unanswered',length(values))
Y=cbind(names,rates,values)
X=rbind(X,Y)


## Favorite
htx1=aggregate(x[x$Answers>=0 & x$Favorite>0,]$Questions, by=list(x[x$Answers>=0 & x$Favorite>0,]$TopicID), FUN=sum)
values=100*htx1[,'x']/htx[,'x']
rates=rep('Favorite',length(values))
Y=cbind(names,rates,values)
X=rbind(X,Y)


## noresponse
htx1=aggregate(x[x$Answers==0,]$Questions, by=list(x[x$Answers==0,]$TopicID), FUN=sum)
values=100*htx1[,'x']/htx[,'x']
rates=rep('NoResponse',length(values))
Y=cbind(names,rates,values)
X=rbind(X,Y)


## UNRELATED questions
htx1=aggregate(x[x$UpCount<0,]$Questions, by=list(x[x$UpCount<0,]$TopicID), FUN=sum)
values=100*htx1[,'x']/htx[,'x']
rates=rep('Unrelated',length(values))
Y=cbind(names,rates,values)
X=rbind(X,Y)



library(gplots) 
rg <- colorpanel(100, 'black', 'red', 'white')

write.csv(X,'X.csv',quote=F)

X=read.csv('X.csv',header=T)
M=acast(X, names~rates, value.var='values')
M <- t(as.matrix(scale(t(M))))
#M = M/rowSums(M)
my.hclust <- function(d) hclust(d, method="ward.D")
pdf("heatmap.pdf",width=6,height=6,paper='special')
heatmap(M, Colv=F, scale='none', hclustfun=my.hclust, col=rg)
dev.off()

















# Start from here!

x=read.csv('Topic.Matrix.Rates.csv')
mtscaled <- as.matrix(scale(x[,-c(1,2,3)]))




y=read.csv('topics.share.csv', header=T)


rownames(mtscaled)=y$Topic.Name
pdf("topics.ratios.pdf",width=10,height=6,paper='special') 
heatmap(mtscaled, Colv=F, scale='none')
dev.off()








### new

topicnames=as.vector(y$Topic.Name)
x=read.table('TOPICS.COUNTS.2.tsv', header=T)

tags=x$TopicID
Tnames=as.vector('')
for(i in tags){
    Tnames=append(Tnames, topicnames[i+1])
}
x['TopicName']=Tnames[-1]

section="UpCount"

ht=aggregate(x[x[,section]<0,section], by=list(x[x[,section]<0,]$TopicName, x[x[,section]<0,]$Year), FUN=sum)
#ggplot(ht,aes(x=factor(Group.2), y=factor(Group.1), fill=x))+geom_tile()+theme_bw()+scale_fill_gradient2(midpoint=5, low="#3333cc", high="#ff3300", mid='#ffffff')+theme(axis.text.x = element_text(angle = 45, hjust = 1))


library(reshape2)
M=acast(ht, Group.1~Group.2, value.var='x')
M <- as.matrix(scale(M))
my.hclust <- function(d) hclust(d, method="ward.D")
#heatmap(M, Colv=F, scale='none', hclustfun=my.hclust)




M=acast(ht, Group.1~Group.2, value.var='x')
M[is.na(M)] <- 0
M = M/rowSums(M)
#M <- as.matrix(scale(M))
mM=melt(M)

pdf(paste(section,".2.pdf", sep=""),width=6,height=6,paper='special')
ggplot(mM)+geom_tile(aes(x=factor(Var2), y=factor(Var1), fill=value))+theme_bw()+scale_fill_gradient2(midpoint=0.2, low="#000000", high="#ff3300", mid='#ffffff')+theme(axis.text.x = element_text(angle = 45, hjust = 1))+xlab('Years')+ylab('Topics')
dev.off()








