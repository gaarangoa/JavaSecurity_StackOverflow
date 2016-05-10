import json

x=json.load(open('items_all_info.json'))

data={}
for i in x:
    try:
        data[i['link']]=[i['active'][0].split()[0].split("-")[0], i['asked'][0].split()[0].split("-")[0], i['views'][1].split()[0]]
    except:
        pass

dataset={}
for i in  open('dataset.db.csv'):
    i=i.split("\t")
    dataset[i[1]]=i

fo=open('time_profile.tsv','w')

for i in data:
    try:
        fo.write('\t'.join([i]+data[i]+dataset[i]))
    except:
        pass

# question_id active  asked   views   nothing qid Questions   Answers UpCount Favorite    DownCount   TopicID Year    Month   Day Hour    Minute  Second  Topic