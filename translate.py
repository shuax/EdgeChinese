import json
import platform
import os
import pathlib

en_json = 'en-US.json'
cn_json = 'zh-CN.json'
en_path = 'en.lproj/'
cn_path = 'zh_CN.lproj/'
dict_json = 'chrome/en_cn_dict.json'
manual_json = 'manual.json'
not_translate_json = 'not_translate.json'
os = platform.uname()[0].lower()
if os == 'darwin':
    en_json = en_path+'/locale.json'
    cn_json = cn_path+'/locale.json'
    path = pathlib.Path(cn_path)
    if not path.exists():
        path.mkdir()


def is_chinese(s):
    try:
        s.encode('ascii')
        return False
    except Exception as e:
        return True


with open(dict_json, 'rb') as f:
    en_cn_dict = json.loads(f.read())

with open(manual_json, 'rb') as f:
    manual = json.loads(f.read())
    for k, v in manual.items():
        if not is_chinese(v):
            print(v)
            continue
        if k == v:
            print(v)
            continue
        # if 'InPrivate' in v:
        #     print(v)
        # if ',' in v and 'plural' not in v:
        #     print(v)
        # if ')' in v and 'plural' not in v and '<' not in v:
        #     print(v)
        # if '.' in v and 'plural' not in v and '<' not in v and '...' not in v:
        #     print(v)
        en_cn_dict[k] = v

# with open('zh-CN2.json', 'rb') as f:
    # zhcn = json.loads(f.read())
    # for x in zhcn['entry']:
    #     x['text']
    # for k, v in manual.items():
    #     en_cn_dict[k] = v

with open(en_json, 'rb') as f:
    en = json.loads(f.read())

not_translate = []

for entry in en['entry']:
    text = entry['text']
    if entry['text'].isdigit():
        continue
    if entry['text'].isupper():
        continue
    if entry['text'].startswith('https://'):
        continue
    if text in en_cn_dict:
        entry['text'] = en_cn_dict[text]
    else:
        text = text.replace('&', '')
        if text in en_cn_dict:
            entry['text'] = en_cn_dict[text]
        else:
            # if not is_chinese(entry['text']):
            # if len(entry['text']) > 20:
            not_translate.append(entry['text'])

with open(cn_json, 'wb') as f:
    f.write(json.dumps(en, ensure_ascii=False, indent=4).encode())

with open(not_translate_json, 'wb') as f:
    f.write(json.dumps(not_translate, ensure_ascii=False, indent=4).encode())
