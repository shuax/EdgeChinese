#!/usr/bin/env bash 

echo "开始解包pak包"

basepath=$(cd `dirname $0`; pwd)

cd $basepath

./pak_tools -c=lang_unpack -f=./en.lproj/locale.pak
./pak_tools -c=lang_unpack -f=./zh_CN.lproj/locale.pak

echo "解包pak包完成"

echo "开始生成词典"

python3 ./dict.py

echo "生成词典完成"