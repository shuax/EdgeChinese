# EdgeChinese
新版edge汉化工具

# 依赖
pak_tools.exe 可以解包打包pak文件，我写的

python3

# 原理
使用词典，翻译英文到中文。

# 成品
我会把汉化好的成品打包发布，另外集成了Edge++增强软件，在这里下载

https://tools.shuax.com/edge/

# 使用

*特别注意，不同版本pak不通用！即使是同一个版本的64位和32位也不通用！所以每个版本都要重新生成*

1、放入这个版本的en-us.pak

2、运行build.bat得到zh-CN.pak

放回zh-CN.pak即可得到汉化版。还不行就把原始的en-us.pak删掉。


# 解释
为了避免全部手工翻译，我最开始用了chrome金丝雀的资源来制作词典。 

进入chrome目录，使用unpack.bat解包en-us.pak，zh-CN.pak为en-US.json，zh-CN.json。

然后运行dict.py就会生成en_cn_dict.json这个词典文件。

注意对比的pak文件一定要是相同版本的。

然后回到根目录。

translate.py会根据词典en_cn_dict.json自动的把en-US.json翻译成zh-CN.json。

因为词典不会100%全，所以我还准备了一个手动词典manual.json，可以手动翻译不全的部分。

经过多次添加以后，词典就会越来越全。

未翻译部分会写入not_translate.json，方便查看翻译有多少缺失。

放入最新版edge的en-us.pak，运行build.bat会执行三个动作。

1. 解包en-us.pak为en-us.json
2. 调用translate.py把en-us.json汉化为zh-CN.json
3. 打包zh-CN.json成zh-CN.pak
