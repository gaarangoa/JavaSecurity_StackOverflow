


x=json.load(open('Q_and_A.json'))

fav=[int(i['favorite'][0]) if len(i['favorite'])>0 else 0 for i in x]
counts=[int(i['up_count'][0]) if len(i['up_count'])>0 else 0 for i in x]

down_count=[i if i<0 else 0 for i in counts]
up_count=[i if i>0 else 0 for i in counts]

answers=[int(i['num_answers'][0]) if len(i['num_answers'])>0 else 0 for i in x]

accepted=[]
for i in x:
    try:
        if len(i['num_answers'])>0 and int(i['up_count'][0])>1:
            accepted.append(int(i['num_answers'][0]))
        else:
            accepted.append(0)
    except:
        accepted.append(0)


fo=open('counts.tsv','w')
for i in accepted:
    fo.write(str(i)+'\taccepted\n')


for i in down_count:
    fo.write(str(i)+'\tdown_count\n')


for i in up_count:
    fo.write(str(i)+'\tup_count\n')


for i in fav:
    fo.write(str(i)+'\tfavorite\n')

fo.close()



