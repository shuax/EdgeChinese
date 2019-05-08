import json
import platform

en_json = 'en-US.json'
cn_json = 'zh-CN.json'
dict_json = 'en_cn_dict.json'
os = platform.uname()[0].lower()

if os == 'darwin':
    en_json = 'en.lproj/locale.json'
    cn_json = 'zh_CN.lproj/locale.json'

def is_chinese(s):
    try:
        s.encode('ascii')
        return False
    except Exception as e:
        return True

with open(en_json, 'rb') as f:
    en = json.loads(f.read())

with open(cn_json, 'rb') as f:
    cn = json.loads(f.read())

en_dict = {}
for x in en['entry']:
    en_dict[x['id']] = x['text']

cn_dict = {}
for x in cn['entry']:
    if not is_chinese(x['text']):
        print(x['text'])
        continue
    cn_dict[x['id']] = x['text']

en_cn_dict = {}
for i, value in en_dict.items():
    if value.isdigit():
        continue
    if i in cn_dict:
        if 'chrome' in cn_dict[i].lower() and 'chrome' not in value.lower():
            continue
        en_cn_dict[value] = cn_dict[i]
# print(en_cn_dict)

print('write ./'+dict_json)

with open(dict_json, 'wb') as f:
    f.write(json.dumps(en_cn_dict, ensure_ascii=False, indent=4).encode())
