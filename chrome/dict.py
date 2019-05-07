import json

def is_chinese(s):
    try:
        s.encode('ascii')
        return False
    except Exception as e:
        return True

with open('en-US.json', 'rb') as f:
    en = json.loads(f.read())

with open('zh-CN.json', 'rb') as f:
    cn = json.loads(f.read())

en_dict = {}
for x in en['entry']:
    en_dict[x['id']] = x['text']

cn_dict = {}
for x in cn['entry']:
    if 'chrome' in x['text'].lower():
        continue
    if not is_chinese(x['text']):
        print(x['text'])
        continue
    cn_dict[x['id']] = x['text']

en_cn_dict = {}
for i, value in en_dict.items():
    if value.isdigit():
        continue
    if i in cn_dict:
        en_cn_dict[value] = cn_dict[i]
# print(en_cn_dict)

with open('en_cn_dict.json', 'wb') as f:
    f.write(json.dumps(en_cn_dict, ensure_ascii=False, indent=4).encode())