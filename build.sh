#!/usr/bin/env bash 

echo "开始打包pak"

basepath=$(cd `dirname $0`; pwd)

cd $basepath

./pak_tools -c=lang_unpack -f=./en.lproj/locale.pak

python3 translate.py

./pak_tools -c=lang_repack -f=./zh_cn.lproj/locale.json

rm -rf ./zh_cn.lproj/locale.json

echo "打包pak完成"
