# EdgeChinese
新版edge汉化工具

# 主要工具
pak_tools.exe 可以解包打包pak的语言包，我写的
python3

# 原理
生成词典，翻译英文到中文。

# 使用方法
准备生成词典。

首先关注chrome目录。最开始我是用的chrome的资源。

首先使用unpack.bat解包en-us.pak，zh-CN.pak为en-US.json，zh-CN.json

然后运行dict.py就会生成en_cn_dict.json这个词典文件

后来随着edge更新，汉化包的迭代，这里面的资源变成相对老版本edge的资源了。

注意对比的pak文件一定要是相同版本的。

然后回到根目录。

放入最新版edge的en-us.pak并使用unpack.bat解包为en-US.json。

运行translate.py会根据词典en_cn_dict.json自动的把en-US.json翻译成zh-CN.json。

因为词典不会100%全，所以我还准备了一个手动的词典manual.json，手动添加不全的部分。

经过多次迭代以后，词典就会越来越全，manual.json变得不那么重要。

运行build.bat可以把zh-CN.json打包成zh-CN.pak，这个放回edge文件夹就支持中文了。
