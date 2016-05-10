import numpy as np
import json

matrix={}
questions=[]
M=[]#[['Q']+[str(i) for i in range(30)]]
for i in open('topics.matrix'):
    i=i.split()
    item=[float(j) for j in i[1:]]
    matrix[i[0]]=item
    M.append(item)
    questions.append(i[0])

index_q=np.argmax(M, axis=1)

q_t=[]
for ix,i in enumerate(questions):
    q_t.append([i, index_q[ix], M[ix][index_q[ix]]])

fo=open('qt.csv','w')

for i in q_t:
    fo.write("\t".join([str(j) for j in i])+"\n")

fo.close()


topics={}
for i in q_t:
    try:
        topics[i[1]].append(i[0])
    except:
        topics[i[1]]=[i[0]]

qtop={}
for i in q_t:
    qtop[i[0]]=i[1]

#topics is a dictionary where the id is the topic id and the values are the list of questions related to that topic


data=json.load(open('Q_and_A.json'))

data_time=json.load(open('items_with_time.json'))
dt={}
for i in data_time:
    dt[i['link'].split("/")[2]]=i#"\t".join(i['time'][0].split()[0].split('-'))+"\t"+"\t".join(i['time'][0].split()[1].split(':'))
    

questions_text={}
for i in data:
    questions_text[i['link']]=i['question']+" ".join(i['answers'])

topics_text={}
for i in topics:
    for j in topics[i]:
        try:
            topics_text[i].append(questions_text[j])
        except:
            topics_text[i]=[questions_text[j]]



DATA={}
for i in data:
    try:
        vector=[i['num_answers'], i['up_count'], i['favorite'], i['down_count'], [str(qtop[i['link']])], [dt[i['link']]]]
        DATA[i['link']]=[j[0] if len(j)>0 else '0' for j in vector]
    except:
        pass


fo=open('TOPICS.COUNTS','w')
fo.write('QID\tQuestions\tAnswers\tUpCount\tFavorite\tDownCount\tTopicID\tYear\tMonth\tDaty\tHour\tMinute\tSecond\n')
for i in DATA:
    fo.write("\t".join([i]+['1']+DATA[i])+'\n')

fo.close()






































data_time=json.load(open('items_with_time.json'))
dt={}
for i in data_time:
    k=i['link'].split("/")
    dt[k[2]]=k[2]
 
fo='keys'



