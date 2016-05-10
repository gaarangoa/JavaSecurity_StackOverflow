
data={}
for i in open('TOPICS.COUNTS.2.tsv'):
    i=i.replace("\n",'').split("\t")
    data[i[1]]=i


tags=json.load(open('items_with_time.json'))

data2={}
for i in tags:
    id=i['link'].split('/')[2]
    data2[id]=i


fo=open('tags.scores.topics.json','w')

data3=[]
for i in data:
    try:
        data3.append(data[i] + ["\t".join(data2[i]['tags'])])
    except:
        pass

json.dump(data3, fo)

fo.close()





# network

edges=[]
for i in data3:
    if len(i[-1])>0:
        for tag in i[-1].split("\t"):
            edges.append([i[-2], tag])

import networkx as nx

G=nx.DiGraph()

for i in edges:
    try:
        G[i[0]][i[1]]['weight']+=1
    except:
        G.add_edge(i[0],i[1],weight=1)


links=[]
for i in G.edges():
    links.append([i[0],i[1],G[i[0]][i[1]]['weight']])

json.dump(links,open('graph.json','w'))

fo = open('edges.tsv', 'w')

for i in links:
    fo.write("\t".join([str(j) for j in i])+"\n")

fo.close()




####


qa=json.load(open('Q_and_A.json'))

Q={}

for i in qa:
    Q[i['link']]=i['question']+" ".join(i['answers'])
    
data4=[]
for i in data3:
    data4.append(i+[Q[i[1]]])
    
fo=open('dataset.db.csv', 'w')

for i in data4:
    fo.write("\t".join(i[:-2])+"\n")

fo.close()



