import json

relation_list = list()
chrmention_list = list()
result_list = list()
fail_list = list()
vis = dict()
duplicated_list = list()
count = 0
with open('relation.json','r',encoding='utf-8') as f1:
    for r in f1.readlines():
        data = json.loads(r)
        relation_list.append(data)
with open('chrmention.json','r',encoding='utf-8') as f2:
    for chr in f2.readlines():
        data = json.loads(chr)
        chrmention_list.append(data)
    for relation in relation_list:
        flag = 0
        for chrmention in chrmention_list:
            if(vis.get(relation['rid']) is None):
                vis[relation['rid']] = 1
            else:
                duplicated_list.append(relation['rid'])
                count += 1
            if(relation['rid'] == chrmention['rid']):
                flag = 1
                relation['chrmention'] = chrmention['chrmention']
                result_list.append(relation)
                break
        if(flag == 0):
            fail_list.append(relation)
    with open('result.json','w',encoding='utf-8')as fw:
        for item in result_list:
            json.dump(item,fw,ensure_ascii=False)
            fw.write("\n")
    with open('fail.json','w',encoding='utf-8') as fw:
        for item in fail_list:
            json.dump(item,fw,ensure_ascii=False)
            fw.write("\n")