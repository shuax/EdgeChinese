import json

with open('en-US.json', 'rb') as f:
    en = json.loads(f.read())

with open('zh-CN.json', 'rb') as f:
    cn = json.loads(f.read())

en_dict = {}
cn_dict = {}
en_cn_dict = {}
for x in en['entry']:
    en_dict[x['id']] = x['text']
for x in cn['entry']:
    cn_dict[x['id']] = x['text']
for i, value in en_dict.items():
    if value.isdigit():
        continue
    if i in cn_dict:
        en_cn_dict[value] = cn_dict[i]
# print(en_cn_dict)

with open('en_cn_dict.json', 'wb') as f:
    f.write(json.dumps(en_cn_dict, ensure_ascii=False, indent=4).encode())