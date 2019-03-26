import json

with open('chrome/en_cn_dict.json', 'rb') as f:
    en_cn_dict = json.loads(f.read())

with open('manual.json', 'rb') as f:
    manual = json.loads(f.read())
    for k, v in manual.items():
        en_cn_dict[k] = v

with open('zh-CN2.json', 'rb') as f:
    zhcn = json.loads(f.read())
    # for x in zhcn['entry']:
    #     x['text']
    # for k, v in manual.items():
    #     en_cn_dict[k] = v

with open('en-US.json', 'rb') as f:
    en = json.loads(f.read())

for entry in en['entry']:
    text = entry['text']
    if text in en_cn_dict:
        entry['text'] = en_cn_dict[text]
    else:
        text = text.replace('&','')
        if text in en_cn_dict:
            entry['text'] = en_cn_dict[text]

with open('zh-CN.json', 'wb') as f:
    f.write(json.dumps(en, ensure_ascii=False, indent=4).encode())