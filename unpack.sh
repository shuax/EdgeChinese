#!/usr/bin/env bash 

echo "开始解包pak包"

basepath=$(cd `dirname $0`; pwd)

cd $basepath

./pak_tools -c=lang_unpack -f=./en.lproj/locale.pak

echo "解包pak包完成"
